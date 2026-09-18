@lesson {"id":"http-e-credenciais","title":"Entenda uma chamada de API","minutes":40,"summary":"Leia endpoint, método, cabeçalhos e corpo sem tratar a integração como mágica."}
## O contrato de uma requisição
Uma API expõe operações para outros programas. Em HTTP, uma requisição tem endereço, método, cabeçalhos e, em muitos casos, corpo. O endereço identifica o recurso; `POST` costuma enviar dados para processamento; cabeçalhos descrevem formato e autenticação; o corpo contém a solicitação.

O servidor responde com um status e um corpo. `200` costuma indicar sucesso; `400`, erro na solicitação; `401`, problema de autenticação; `403`, falta de permissão; `429`, limite de uso; `5xx`, falha do lado do serviço. O significado exato e os detalhes devem ser conferidos na documentação do provedor.

## Separe conta de chat e conta de API
Não presuma que sua assinatura de um aplicativo inclui chamadas programáticas. Consulte o painel de API do provedor, configure limites e confira a cobrança antes do teste. Modelos disponíveis, limites e parâmetros podem ser diferentes do produto de conversa.

1. Escolha um provedor para o laboratório.
2. Leia o início rápido oficial e confirme o modelo disponível na sua conta.
3. Crie uma chave com o menor alcance necessário.
4. Guarde-a como variável de ambiente ou credencial do serviço que executará a chamada.
5. Defina um orçamento pequeno e limite de saída.

## Desenhe o caminho dos dados
```text
Seu programa → HTTPS → API do provedor
             ← status + resposta JSON
```

Um frontend público não deve conter a chave. Em uma aplicação web, o pedido passa por um backend que valida a entrada, autentica o usuário e controla uso. Nos exercícios, o script local faz esse papel de cliente de servidor; ele não deve ser embutido na página do curso.

Uma chave vazada precisa ser revogada. Não copie segredos para prints, prompts, commits ou relatórios de erro. Para pedir ajuda, compartilhe o status e uma mensagem sanitizada, com a chave removida.
@exercise
Identifique as partes deste pedido fictício: POST para `/classificar`, cabeçalho `Content-Type: application/json`, corpo `{"mensagem":"esqueci minha senha"}`. Onde estaria a credencial em uma API que usa Bearer?
@answer
O método é POST; o caminho indica a operação; Content-Type informa o formato; o corpo contém os dados. Em uma API com Bearer, a credencial vai no cabeçalho Authorization. O exemplo é conceitual e não representa um endpoint real deste site. Outros provedores podem usar cabeçalhos próprios, como x-api-key.
@quiz {"question":"O status 401 normalmente indica o quê?","options":["Um problema de autenticação que deve ser investigado.","Que a resposta está correta.","Que o modelo precisa de um prompt mais longo."],"correct":0,"explanation":"Verifique a credencial e o método de autenticação na documentação. Repetir o mesmo pedido sem corrigir a causa geralmente não resolve."}

@lesson {"id":"primeira-api","title":"Faça uma chamada com OpenAI, Claude ou Gemini","minutes":50,"summary":"Execute um cliente pequeno e compare o contrato dos três provedores."}
## Um cliente, três adaptadores
Baixe [chamada_api.py](downloads/chamada_api.py). O programa usa apenas a biblioteca padrão do Python e separa a construção do pedido da leitura da resposta. Os endpoints e cabeçalhos variam: OpenAI usa Responses; Claude usa Messages; o exemplo Gemini usa generateContent. Consulte as referências antes de adaptar para outro modelo ou API.

O nome do modelo é configurado por você. Isso evita depender de um identificador fixo que pode mudar ou não estar disponível na sua conta. Escolha um modelo de texto compatível com o endpoint do adaptador e seus parâmetros.

## Primeiro teste sem rede
1. Salve o arquivo em uma pasta de estudo.
2. Abra o terminal nessa pasta.
3. Execute `python chamada_api.py --dry-run`.
4. Confira o endereço, os nomes dos cabeçalhos e o corpo. Nenhuma chave é exibida e nenhuma chamada é feita.

## Chamada real no PowerShell
Configure provedor, modelo e chave somente na sessão do terminal. Para digitar a chave sem mostrá-la, use a função de leitura abaixo. Chamadas reais podem gerar cobrança.

```powershell
$env:AI_PROVIDER = "openai"
$env:AI_MODEL = "SUBSTITUA_PELO_MODELO_DA_SUA_CONTA"
$chaveCurso = Read-Host "Chave de API" -AsSecureString
$env:AI_API_KEY = [System.Net.NetworkCredential]::new("", $chaveCurso).Password
python chamada_api.py
Remove-Item Env:AI_API_KEY
```

Para Claude, mude o provedor para `anthropic`; para Gemini, use `gemini`. Defina também o modelo correspondente. Se a chave Claude abranger vários workspaces, configure AI_WORKSPACE_ID com o workspace de teste; o adaptador inclui esse cabeçalho quando informado. O script faz um pedido curto, usa timeout e mostra texto retornado e dados de uso quando presentes. Ele não implementa conversa persistente, streaming ou ferramentas.

## Confira a resposta completa
Uma resposta de API não é só texto. Pode conter status, blocos, motivos de parada e uso. O script extrai texto dos formatos esperados, mas informa quando ele está ausente. Um limite de saída pode interromper a geração; uma recusa ou falha não deve virar resposta vazia tratada como sucesso.

Se houver erro, confira primeiro provedor e modelo, depois credencial, limites e parâmetros. Não aumente permissões ou repita indefinidamente para tentar “forçar” o funcionamento.
@exercise
Execute o modo dry-run para os três provedores, sem chave. Liste o que muda no endpoint, na autenticação e no corpo. A execução real é opcional.
@answer
OpenAI envia `model` e `input` para Responses com Authorization Bearer. Claude envia `model`, `max_tokens` e `messages`, com x-api-key e versão da API. Gemini coloca o modelo no caminho, usa x-goog-api-key e envia `contents`. A intenção pode ser igual, mas os contratos não são intercambiáveis.
@quiz {"question":"Por que o exemplo pede que você configure o modelo?","options":["Porque qualquer texto é um modelo válido.","Porque disponibilidade e identificadores devem corresponder à conta e ao endpoint escolhido.","Porque a chave de API é o nome do modelo."],"correct":1,"explanation":"O adaptador e o modelo precisam ser compatíveis. Um nome inventado ou de outro provedor não funciona."}

@lesson {"id":"json-erros-custos","title":"Saídas estruturadas, erros e custos","minutes":45,"summary":"Construa uma fronteira entre o texto do modelo e a lógica do seu sistema."}
## Formato válido não significa decisão correta
Uma automação precisa de dados previsíveis. Defina um esquema com campos, tipos e valores permitidos. Quando o provedor e o modelo oferecerem saída estruturada, use o recurso apropriado ao contrato da API. Mesmo assim, confira recusas, interrupções e regras de negócio.

Para a triagem, podemos exigir categoria entre financeiro, acesso, outros e revisao; motivo como texto curto; e necessidade de revisão como booleano. O esquema limita a forma, mas não prova que uma mensagem foi classificada corretamente.

```json
{
  "categoria": "acesso",
  "motivo": "Usuário relata falha de login",
  "revisao": false
}
```

1. Converta o texto para JSON com tratamento de erro.
2. Verifique se é um objeto, não uma lista.
3. Confira campos, tipos e categorias permitidas.
4. Aplique regras de negócio independentes do modelo.
5. Encaminhe qualquer falha para revisão; não execute a ação final.

## Trate falhas conforme a causa
Não repita automaticamente erros de autenticação. Para limites e falhas transitórias, use tentativas limitadas, espera crescente e variação aleatória, respeitando orientações do provedor. Uma operação que pode gerar efeitos precisa de idempotência antes de ser repetida.

Timeout é um limite de espera, não prova de que o servidor não processou o pedido. Se a operação cria algo, consulte o estado antes de repetir. Para geração de texto, a repetição ainda pode gerar custo adicional.

## Estime antes de multiplicar
A fórmula didática é: tokens de entrada × preço de entrada, mais tokens de saída × preço de saída, respeitando a unidade publicada. Acrescente ferramentas e outros custos quando aplicáveis. Use preços atuais do provedor, sem misturar valores por mil e por milhão.

Se uma chamada custa hipoteticamente R$ 0,02, 1.000 chamadas custam R$ 20,00 antes de tentativas extras. O valor é um exemplo aritmético, não uma tabela de preço real. Registre custo por tarefa concluída, incluindo falhas e revisão.
@exercise
Valide esta saída: `{"categoria":"urgente","motivo":12,"revisao":"não"}`. Liste os três problemas e defina um destino seguro.
@answer
“urgente” não está entre as categorias; motivo deveria ser texto; revisao deveria ser booleano. O destino é revisão com registro do erro, sem interpretar a string “não” como autorização para executar. Corrigir silenciosamente campos pode esconder um problema de contrato ou alterar a intenção da resposta.
@quiz {"question":"Uma saída que segue o esquema JSON está necessariamente correta?","options":["Sim, formato garante a verdade.","Sim, se o JSON não tem espaços.","Não. Ainda é preciso verificar conteúdo e regras de negócio."],"correct":2,"explanation":"Validade estrutural e validade semântica são verificações diferentes."}
