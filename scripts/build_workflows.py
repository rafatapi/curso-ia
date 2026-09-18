"""Gera workflows educativos com nós nativos e dados fictícios."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def node(name, kind, version, position, parameters, identifier):
    return {'parameters': parameters, 'id': identifier, 'name': name, 'type': 'n8n-nodes-base.' + kind, 'typeVersion': version, 'position': position}


def code(name, text, position, identifier):
    return node(name, 'code', 2, position, {'mode': 'runOnceForAllItems', 'jsCode': text}, identifier)


def workflow(name, seed_name, seed_code, transform_name, transform_code):
    nodes = [
        node('Executar manualmente', 'manualTrigger', 1, [0, 240], {}, 'manual'),
        code(seed_name, seed_code, [240, 240], 'dados'),
        code(transform_name, transform_code, [480, 240], 'transformacao'),
        node('Precisa de revisão?', 'if', 2.2, [720, 240], {
            'conditions': {'options': {'caseSensitive': True, 'leftValue': '', 'typeValidation': 'strict', 'version': 2},
                           'conditions': [{'id': 'revisao', 'leftValue': '={{ $json.revisao }}', 'rightValue': True, 'operator': {'type': 'boolean', 'operation': 'true', 'singleValue': True}}], 'combinator': 'and'}, 'options': {}}, 'condicao'),
        code('Fila de revisão', "return $input.all().map(item => ({json: {...item.json, estado: 'aguardando_revisao', acao_externa_executada: false}}));", [980, 120], 'revisao'),
        code('Propostas classificadas', "return $input.all().map(item => ({json: {...item.json, estado: 'proposta_classificada', acao_externa_executada: false}}));", [980, 360], 'classificados'),
        node('Como usar', 'stickyNote', 1, [200, -80], {'content': '## IA na prática — laboratório\nExecute manualmente e inspecione cada nó.\nDados fictícios. Nenhuma credencial. Nenhuma chamada externa.\nOs estados finais são propostas; não são aprovações nem envios.\nLeia os módulos 14 e 15 antes de conectar serviços.', 'height': 230, 'width': 690}, 'nota')
    ]
    def link(target):
        return {'node': target, 'type': 'main', 'index': 0}
    connections = {
        'Executar manualmente': {'main': [[link(seed_name)]]},
        seed_name: {'main': [[link(transform_name)]]},
        transform_name: {'main': [[link('Precisa de revisão?')]]},
        'Precisa de revisão?': {'main': [[link('Fila de revisão')], [link('Propostas classificadas')]]}
    }
    return {'name': name, 'nodes': nodes, 'pinData': {}, 'connections': connections, 'active': False, 'settings': {'executionOrder': 'v1', 'timezone': 'America/Sao_Paulo'}, 'tags': []}


RULE_SEED = """return [
  {json: {id: 'A1', mensagem: 'Preciso da segunda via do boleto'}},
  {json: {id: 'A2', mensagem: 'Esqueci minha senha de acesso'}},
  {json: {id: 'A3', mensagem: 'Olá, preciso de uma informação'}}
];"""

RULE_CODE = """return $input.all().map(item => {
  const id = typeof item.json.id === 'string' ? item.json.id.trim() : '';
  const mensagem = typeof item.json.mensagem === 'string' ? item.json.mensagem.trim() : '';
  const texto = mensagem.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase();
  const financeiro = /boleto|pagamento|cobranca/.test(texto);
  const acesso = /senha|login|acesso/.test(texto);
  let categoria = 'revisao';
  let motivo = 'Mensagem vazia, inválida ou intenção não reconhecida';
  if (id && mensagem && mensagem.length <= 2000) {
    if (financeiro && acesso) motivo = 'Múltiplas intenções';
    else if (financeiro) {categoria = 'financeiro'; motivo = 'Palavra de cobrança encontrada';}
    else if (acesso) {categoria = 'acesso'; motivo = 'Palavra de acesso encontrada';}
  }
  return {json: {id, mensagem, categoria, motivo, revisao: categoria === 'revisao'}};
});"""

AI_SEED = """// Respostas fictícias: este nó NÃO chama um modelo.
return [
  {json: {id: 'S1', mensagem: 'Esqueci minha senha', resposta_ia: '{"categoria":"acesso","motivo":"Falha de login","revisao":false}'}},
  {json: {id: 'S2', mensagem: 'Preciso de ajuda', resposta_ia: '{"categoria":"urgente","motivo":"Indefinido","revisao":false}'}},
  {json: {id: 'S3', mensagem: 'Qual é o prazo?', resposta_ia: 'isto não é JSON'}}
];"""

AI_CODE = """const categorias = new Set(['financeiro', 'acesso', 'outros', 'revisao']);
return $input.all().map(item => {
  const id = typeof item.json.id === 'string' ? item.json.id.trim() : '';
  try {
    if (!id) throw new Error('id ausente');
    if (typeof item.json.mensagem !== 'string' || !item.json.mensagem.trim() || item.json.mensagem.length > 2000) throw new Error('mensagem inválida');
    if (typeof item.json.resposta_ia !== 'string' || item.json.resposta_ia.length > 5000) throw new Error('resposta inválida ou grande demais');
    const r = JSON.parse(item.json.resposta_ia);
    if (!r || typeof r !== 'object' || Array.isArray(r)) throw new Error('objeto esperado');
    const chaves = Object.keys(r).sort().join(',');
    if (chaves !== 'categoria,motivo,revisao') throw new Error('campos inesperados ou ausentes');
    if (!categorias.has(r.categoria)) throw new Error('categoria não permitida');
    if (typeof r.motivo !== 'string' || !r.motivo.trim() || r.motivo.length > 300) throw new Error('motivo inválido');
    if (typeof r.revisao !== 'boolean') throw new Error('revisao deve ser booleano');
    return {json: {id, categoria: r.categoria, motivo: r.motivo, revisao: r.revisao || r.categoria === 'revisao', formato_valido: true}};
  } catch (erro) {
    // Mensagens estáveis; não repassa o corpo do modelo para o erro.
    return {json: {id, categoria: 'revisao', motivo: 'Saída inválida; confira entrada e contrato', revisao: true, formato_valido: false}};
  }
});"""


if __name__ == '__main__':
    workflows = {
        'n8n-triagem-regras.json': workflow('IA na prática - Triagem por regras', 'Pedidos de exemplo', RULE_SEED, 'Classificar por regras', RULE_CODE),
        'n8n-validacao-ia.json': workflow('IA na prática - Validar saída simulada de IA', 'Saídas simuladas de IA', AI_SEED, 'Validar contrato', AI_CODE)
    }
    for filename, data in workflows.items():
        (ROOT / 'downloads' / filename).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Dois workflows gerados, sem credenciais nem chamadas externas.')
