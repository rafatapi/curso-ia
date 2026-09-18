/* Executa a lógica dos nós Code com dados fictícios, sem iniciar n8n. */
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const root=fs.existsSync(path.join(process.cwd(),'downloads'))?process.cwd():path.resolve(__dirname,'..');
function load(name){return JSON.parse(fs.readFileSync(path.join(root,'downloads',name),'utf8'));}
function run(w,name,items=[]){const node=w.nodes.find(n=>n.name===name);assert(node);const context=vm.createContext({$input:{all:()=>items}});return JSON.parse(JSON.stringify(vm.runInContext('(function(){'+node.parameters.jsCode+'})()',context,{timeout:1000})));}
const rules=load('n8n-triagem-regras.json'),ai=load('n8n-validacao-ia.json');
for(const w of [rules,ai]){
  const names=new Set(w.nodes.map(n=>n.name));assert.equal(names.size,w.nodes.length);assert.equal(w.active,false);
  for(const [source,conn] of Object.entries(w.connections)){assert(names.has(source));for(const port of conn.main)for(const target of port)assert(names.has(target.node));}
  for(const node of w.nodes){assert(!node.credentials);if(node.type.endsWith('.code'))new vm.Script('(function(){'+node.parameters.jsCode+'})()');}
}
let result=run(rules,'Classificar por regras',run(rules,'Pedidos de exemplo'));
assert.deepEqual(result.map(x=>x.json.categoria),['financeiro','acesso','revisao']);
for(const mensagem of ['',null,'Paguei o boleto mas meu login falhou'])assert.equal(run(rules,'Classificar por regras',[{json:{id:'T',mensagem}}])[0].json.revisao,true);
result=run(ai,'Validar contrato',run(ai,'Saídas simuladas de IA'));
assert.deepEqual(result.map(x=>x.json.revisao),[false,true,true]);
const invalid=[null,[],{categoria:'urgente',motivo:'teste',revisao:false},{categoria:'acesso',motivo:5,revisao:false},{categoria:'acesso',motivo:'ok',revisao:'false'},{categoria:'acesso',motivo:'ok',revisao:false,extra:1}];
for(const value of invalid){const item={json:{id:'T',mensagem:'teste',resposta_ia:JSON.stringify(value)}};assert.equal(run(ai,'Validar contrato',[item])[0].json.formato_valido,false);}
const special={json:{id:'T',mensagem:'teste',resposta_ia:JSON.stringify({categoria:'revisao',motivo:'ambíguo',revisao:false})}};
assert.equal(run(ai,'Validar contrato',[special])[0].json.revisao,true);
for(const w of [rules,ai])for(const name of ['Fila de revisão','Propostas classificadas'])assert.equal(run(w,name,[{json:{id:'T'}}])[0].json.acao_externa_executada,false);
console.log('OK: conexões e sintaxe dos 2 workflows; lógica de classificação, ambiguidade, validação e ausência de efeitos externos.');
console.log('Esta verificação executa nós Code isoladamente; não substitui importação/execução em uma instância do n8n.');
