@lesson {"id":"plugins-skills-conectores","title":"Plugin, skill, conector: o que muda?","minutes":35,"summary":"Diferencie instruções reutilizáveis de capacidades de integração."}
## Os nomes variam; as funções ajudam a entender
Uma **skill** reúne instruções e recursos para realizar uma tarefa. Um **conector** liga uma aplicação a um serviço ou fonte de dados. Um **plugin** pode empacotar capacidades, instruções e integrações conforme o ecossistema. O significado exato depende do produto; não presuma que um plugin de uma ferramenta funciona em outra.

Uma skill de revisão pode ensinar como avaliar um relatório, mas não concede acesso ao seu Drive. Um conector de arquivos pode permitir consulta, mas não garante que o assistente saiba aplicar a política editorial da sua equipe. Instruções e acesso são peças diferentes.

## Desenhe uma skill de estudo
1. Defina quando ela deve ser usada: revisar resumos de textos fornecidos.
2. Defina entradas: fonte, resumo e público.
3. Escreva um procedimento: conferir fatos, omissões e clareza.
4. Defina saída: problemas encontrados e sugestões localizadas.
5. Acrescente exemplos de erro e de resposta aceitável.

```markdown
# Revisar resumo com fonte
Use quando houver texto original e resumo para comparar.
1. Identifique as afirmações do resumo.
2. Relacione cada afirmação a um trecho da fonte.
3. Marque distorções, omissões relevantes e dados sem apoio.
4. Sugira correções sem inventar fatos.
Saída: tabela de achados e versão corrigida, se solicitada.
```

Esse é um rascunho de procedimento, não um pacote instalável universal. Para instalar, siga o formato aceito pelo produto: nomes de arquivos, metadados e estrutura podem mudar. A documentação oficial do ecossistema deve orientar o empacotamento.

## Avalie antes de conectar
Confira origem, mantenedor, permissões, dados acessados e efeitos possíveis. Comece com leitura de material fictício e escopo reduzido. Uma integração pode executar operações fora do chat; trate seus resultados como dados e confira a consequência de cada ação.
@exercise
Para um assistente que consulta documentos e revisa textos, separe o que pertence à skill, ao conector e à autorização do usuário.
@answer
A skill descreve os critérios de revisão. O conector implementa o acesso aos documentos. A autorização determina quais arquivos e operações podem ser usados. Nenhum desses elementos substitui os outros: saber revisar não concede acesso; ter acesso não autoriza publicar; autorizar consulta não garante qualidade editorial.
@quiz {"question":"Uma skill de revisão concede automaticamente acesso a um serviço externo?","options":["Não. Instruções e acesso são capacidades distintas.","Sim, qualquer instrução cria uma conexão.","Sim, se o nome da skill mencionar o serviço."],"correct":0,"explanation":"A conexão depende de implementação e permissões próprias."}

@lesson {"id":"mcp-arquitetura","title":"MCP: um idioma para conectar ferramentas","minutes":40,"summary":"Entenda host, cliente e servidor sem confundir protocolo com autorização."}
## As três peças da conexão
MCP, Model Context Protocol, padroniza a comunicação entre aplicações de IA e servidores que oferecem contexto e capacidades. O **host** é a aplicação que coordena a experiência. O **cliente** mantém a conexão com um servidor. O **servidor** expõe recursos permitidos por sua implementação.

Entre as capacidades estão ferramentas, recursos e prompts. Ferramentas representam operações; recursos disponibilizam contexto; prompts oferecem modelos de interação. Nem todo cliente suporta todas as capacidades da mesma forma.

## Pense em um catálogo de operações
Imagine um servidor de políticas com uma ferramenta `consultar_politica`. O host descobre a ferramenta, apresenta seu contrato ao modelo e pode chamar a operação quando adequado. O servidor recebe argumentos, executa a lógica e retorna um resultado. MCP não torna automaticamente confiável o texto retornado.

```text
Aplicação de IA (host)
  → cliente MCP
    → servidor de políticas
      → consultar_politica(topico)
    ← resultado com fonte e versão
```

Conexões locais podem usar entrada e saída padrão, chamadas de stdio. Conexões remotas podem usar transporte HTTP conforme a versão do protocolo e a implementação. Autenticação, autorização e proteção do serviço remoto precisam ser configuradas; não são substituídas pela existência do protocolo.

## Faça uma análise de acesso
1. Liste as ferramentas que o servidor expõe.
2. Marque quais só leem e quais modificam dados.
3. Defina que usuário ou processo pode chamar cada uma.
4. Valide argumentos no servidor.
5. Limite a informação retornada ao necessário.
6. Registre falhas sem expor segredos.

Um servidor que lê arquivos deve restringir diretórios e impedir travessia de caminhos. Um que consulta banco deve usar consultas parametrizadas e controles de acesso. MCP organiza a interface; a segurança da implementação continua sendo trabalho do desenvolvedor.
@exercise
Um servidor oferece “ler política” e “apagar documento”. Você precisa apenas responder perguntas de alunos. Qual capacidade deve ficar disponível e por quê?
@answer
Apenas a leitura necessária deve ser exposta ou autorizada para essa tarefa. Apagar documentos não contribui para responder perguntas e aumenta o impacto de um erro. O menor conjunto de capacidades facilita testes e reduz consequências. Mesmo a leitura precisa respeitar quais políticas o usuário pode consultar.
@quiz {"question":"MCP substitui autenticação e autorização?","options":["Sim, qualquer conexão MCP é pública e segura.","Não. O protocolo não elimina a necessidade de controlar identidade, acesso e efeitos.","Sim, quando a ferramenta tem uma descrição longa."],"correct":1,"explanation":"A implementação e a configuração precisam impor os limites de acesso e execução."}

@lesson {"id":"mcp-laboratorio","title":"Seu primeiro servidor MCP local","minutes":55,"summary":"Exponha uma consulta de política fictícia com uma ferramenta somente de leitura."}
## Prepare um ambiente isolado
Baixe [servidor_mcp.py](downloads/servidor_mcp.py). O exemplo usa o SDK oficial Python e três políticas fictícias em memória. Não lê seus arquivos, não acessa a rede e não altera documentos. O servidor usa stdio; ele precisa de um cliente MCP para trocar mensagens.

Crie uma pasta de laboratório e coloque o arquivo nela. Os comandos abaixo são para PowerShell e não exigem ativar o ambiente virtual.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install "mcp[cli]>=1.28,<2"
.\.venv\Scripts\mcp.exe dev servidor_mcp.py
```

O comando de desenvolvimento abre o fluxo de inspeção do SDK e pode precisar de Node.js para a ferramenta de inspeção. Confira a documentação oficial se a interface ou o SDK mudar. A dependência está limitada à família 1.x utilizada no exemplo; a versão principal 2.x já possui uma linha de documentação própria. Este laboratório mantém a 1.x por compatibilidade; consulte o guia de migração antes de trocar a dependência.

## Inspecione a ferramenta
1. No inspetor, conecte-se ao servidor local apresentado.
2. Liste as ferramentas e localize `consultar_politica`.
3. Confira que o parâmetro `topico` aceita acesso, suporte ou certificado.
4. Execute com `acesso` e confira id, versão e texto retornados.
5. Teste um valor fora da lista e observe a rejeição.
6. Encerre o inspetor e o processo ao terminar.

## Leia o código antes de integrar
O decorador `@mcp.tool()` expõe a função. A anotação `Literal` limita os valores declarados no esquema. O dicionário guarda apenas dados fictícios. A função retorna uma estrutura simples; não executa comandos a partir do argumento.

Executar `python servidor_mcp.py` diretamente pode parecer que “travou”: ele fica aguardando mensagens do cliente no transporte stdio. Não imprima mensagens de depuração em stdout nesse modo, pois isso pode interferir no protocolo. Use stderr ou o mecanismo de logs apropriado.

Para conectar a um aplicativo real, siga a configuração oficial desse cliente e use caminhos absolutos para o Python do ambiente e o arquivo. Não copie um formato de configuração de outro produto sem conferir compatibilidade.
@exercise
Adicione uma quarta política fictícia, “materiais”. Atualize tanto a anotação dos valores aceitos quanto os dados. Teste a consulta nova e repita uma consulta antiga.
@answer
A ferramenta deve anunciar o novo valor e retornar sua política. Se você atualizar apenas o dicionário, o esquema pode continuar rejeitando “materiais”. Se atualizar apenas a anotação, a função pode tentar acessar um dado inexistente. O teste antigo verifica que a extensão não quebrou as consultas anteriores.
@quiz {"question":"Por que um servidor stdio pode ficar aguardando ao ser executado diretamente?","options":["Porque todo servidor MCP está com defeito.","Porque precisa baixar automaticamente todos os seus arquivos.","Porque espera mensagens de um cliente pelo transporte configurado."],"correct":2,"explanation":"O servidor não é necessariamente uma aplicação com janela; ele participa de uma troca de mensagens com um cliente."}
