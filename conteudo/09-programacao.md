@lesson {"id":"python-json-terminal","title":"O mínimo de Python, JSON e terminal","minutes":45,"summary":"Execute seu primeiro programa e entenda as estruturas que conectam automações."}
## Três peças do laboratório
O terminal permite executar programas por comandos. Python é a linguagem dos exemplos locais. JSON é um formato de troca de dados, com objetos, listas, textos, números, booleanos e `null`. JSON e Python têm sintaxes parecidas, mas não são a mesma coisa: Python usa `True`, enquanto JSON usa `true`.

Instale Python 3.11 ou superior pela fonte oficial. Abra um terminal e execute `python --version`. Se o comando não for encontrado no Windows, verifique a instalação e tente `py --version`. Não é preciso modificar políticas de execução para os exercícios deste curso.

## Crie e execute um arquivo
1. Crie uma pasta de estudo e abra-a em um editor de texto ou código.
2. Salve o trecho abaixo como `receita.py`, em UTF-8.
3. Abra o terminal nessa pasta.
4. Execute `python receita.py`.
5. Confira o resultado e altere a quantidade para repetir o experimento.

```python
import json

texto = '{"id":"A1","quantidade":2,"preco":120,"status":"pago"}'
pedido = json.loads(texto)
if pedido["status"] == "pago":
    receita = pedido["quantidade"] * pedido["preco"]
    print(f"Receita: R$ {receita:.2f}")
else:
    print("Pedido fora do cálculo")
```

`json.loads` converte texto JSON em estruturas do Python. Colchetes acessam valores por chave. O `if` escolhe um caminho conforme uma condição. A indentação faz parte da sintaxe: as linhas recuadas pertencem ao bloco. O resultado esperado é `Receita: R$ 240.00`.

## Leia erros de baixo para cima
Se aparecer uma mensagem de erro, leia o tipo e a última linha, depois localize o arquivo e a linha citada. `KeyError` pode indicar uma chave ausente; `JSONDecodeError`, um texto JSON inválido. Copie para a IA apenas o trecho necessário, sem credenciais, e peça explicar a causa antes de sugerir alteração.
@exercise
Mude `status` para `cancelado` e execute. Depois remova a chave `quantidade` mantendo status pago. Compare o comportamento e explique por que o segundo caso não é simplesmente receita zero.
@answer
O cancelado imprime “Pedido fora do cálculo”. Sem quantidade e com status pago, o programa tenta acessar uma chave inexistente e gera `KeyError`. Dado ausente não significa zero; é preciso validar a entrada e encaminhar a exceção. Essa distinção será importante nas automações.
@quiz {"question":"O que faz json.loads neste exemplo?","options":["Transforma texto JSON em uma estrutura que o Python consegue acessar.","Envia o pedido para uma IA.","Publica o arquivo no GitHub."],"correct":0,"explanation":"A conversão é local e não envolve serviço externo nem modelo de IA."}

@lesson {"id":"programar-com-assistente","title":"Peça código, mas também peça evidências","minutes":40,"summary":"Transforme um problema em uma mudança pequena que você consegue testar."}
## Escreva um contrato simples
Antes de pedir código, diga o que entra e o que deve sair. Para receita: entra uma lista de pedidos; saem total e exceções. Cancelados não contam; ids repetidos não contam duas vezes; quantidade ausente vai para revisão. Esse contrato evita que o assistente “resolva” o problema com suposições invisíveis.

Um pedido de programação deve incluir ambiente, exemplo e restrições. Você pode usar ChatGPT, Claude, Gemini, Codex, Claude Code ou um assistente no editor. A capacidade de editar ou executar depende do ambiente; em um chat comum, você ainda precisa salvar e rodar o código.

## Um pedido verificável
```prompt
Crie uma função Python que receba uma lista de pedidos.
Some apenas status pago, sem duplicar ids.
Quantidade ausente deve gerar uma exceção registrada, não virar zero.
Retorne total e lista de exceções. Use apenas a biblioteca padrão.
Inclua exemplos: pedido válido, cancelado, duplicado e incompleto.
Explique como executar e o resultado esperado de cada exemplo.
```

1. Leia a função e localize cada regra do contrato.
2. Execute um exemplo pequeno cujo resultado você sabe calcular.
3. Faça um teste por regra e um teste que combine duas regras.
4. Se falhar, informe entrada, esperado e observado.
5. Revise a alteração proposta antes de substituir o arquivo.

## Teste comportamento, não aparência
Um teste útil falha quando a regra importante deixa de funcionar. Verificar apenas se uma função existe é fraco. Para um pedido válido de duas unidades a R$ 120, o teste deve exigir total R$ 240. Para um duplicado, deve exigir que o total não dobre.

Não execute dependências ou comandos sem entender a finalidade. Peça a solução mais simples compatível com o exercício. Uma tarefa de somar pedidos não precisa de um banco de dados nem de uma biblioteca de IA.
@exercise
Escreva quatro testes em linguagem natural para a função. Depois peça ao assistente para convertê-los em testes executáveis e confira se as entradas representam as situações descritas.
@answer
Exemplos: válido 2 × 120 resulta em 240; cancelado resulta em 0; duas cópias do mesmo id resultam em 240 e uma exceção; quantidade ausente resulta em 0 para esse registro e uma exceção. Combine um válido e um incompleto para garantir que uma falha não impede o processamento dos demais.
@quiz {"question":"Qual relato ajuda mais a corrigir um erro?","options":["“Não funcionou, arrume tudo.”","Entrada usada, resultado esperado, resultado observado e mensagem de erro relevante.","Somente uma captura do ícone do programa."],"correct":1,"explanation":"Um caso reproduzível permite localizar a falha e verificar a correção."}

@lesson {"id":"git-e-publicacao","title":"Git, revisão e GitHub Pages","minutes":40,"summary":"Guarde versões e publique uma página estática sem expor credenciais."}
## Versões tornam mudanças reversíveis
Git registra versões dos arquivos. Um repositório local fica no computador; um remoto, como GitHub, permite compartilhar e guardar uma cópia. `commit` cria uma versão local; `push` envia commits para o remoto. Nenhum dos dois garante que o código está correto: testes e revisão continuam necessários.

Antes de versionar, confira a pasta atual e crie um `.gitignore` para arquivos que não devem entrar, como ambientes locais e segredos. Se uma credencial já foi publicada, ignorar o arquivo depois não remove o vazamento; a credencial precisa ser revogada e o incidente tratado.

## Um fluxo de revisão
```text
git status
git diff
git add index.html styles.css app.js
git diff --staged
git commit -m "Melhora a navegação do curso"
```

1. Use `status` para ver arquivos alterados.
2. Leia o `diff` antes de adicionar as mudanças.
3. Adicione apenas os arquivos pretendidos.
4. Confira o que entrará no commit.
5. Crie uma mensagem que explique o resultado.

## Publique o que é estático
GitHub Pages hospeda HTML, CSS, JavaScript e outros arquivos estáticos. Ele não é um servidor Python nem um lugar seguro para uma chave de API. Tudo que chega ao navegador pode ser inspecionado pelo visitante.

Para este curso, crie um repositório, envie os arquivos e escolha a origem de publicação em Settings → Pages conforme o guia oficial. O README do projeto descreve o caminho pela branch principal. Links relativos e navegação por fragmentos permitem funcionar também em um endereço como `usuario.github.io/curso-ia/`.

Antes de divulgar, teste a página publicada, abra uma aula diretamente pelo link e recarregue. Confira imagens, downloads e navegação em celular. Publicar não termina a verificação: o endereço final pode revelar problemas que não apareciam localmente.
@exercise
Explique onde ficariam o site do curso, uma chave de API e um script Python de atendimento em uma arquitetura real. Desenhe o caminho de uma solicitação e indique qual componente precisa controlar o acesso.
@answer
O site estático pode ficar no GitHub Pages. A chave deve ficar em um ambiente de servidor ou cofre de credenciais, não no JavaScript público. O script Python precisa de um ambiente que execute Python, local ou hospedado. O navegador chama seu backend com controles apropriados; o backend usa a chave para chamar o provedor.
@quiz {"question":"Onde uma chave de API não deve ficar?","options":["Em um cofre de credenciais do servidor.","Em uma variável de ambiente de um backend protegido.","No JavaScript público de uma página GitHub Pages."],"correct":2,"explanation":"Arquivos enviados ao navegador são acessíveis ao visitante. Ofuscação não transforma uma chave pública em segredo."}
