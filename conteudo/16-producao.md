@lesson {"id":"avaliacao-sistematica","title":"Avalie qualidade antes de ampliar o uso","minutes":45,"summary":"Crie casos de teste que representam acertos, limites e falhas do sistema."}
## Avaliação é parte do produto
Um protótipo pode impressionar em uma demonstração e falhar quando recebe entradas variadas. Defina critérios antes de escolher exemplos de sucesso. Para atendimento com fontes, avalie correção, sustentação, reconhecimento de ausência e respeito ao fluxo de autorização.

Baixe [avaliacoes.csv](downloads/avaliacoes.csv) e use-o como ponto de partida. O arquivo contém casos normais, ambíguos, sem evidência e adversariais. Acrescente casos do seu domínio usando dados fictícios ou materiais autorizados.

## Um conjunto de teste equilibrado
1. Defina o comportamento esperado para cada entrada.
2. Marque erros críticos que reprovam a execução, como ação sem aprovação.
3. Execute a versão atual e registre saída, fontes, tempo e resultado.
4. Classifique a causa das falhas: dado, busca, geração, validação ou integração.
5. Altere um componente e repita os testes afetados e os de regressão.
6. Reserve casos novos para a avaliação final.

Use verificações determinísticas quando possível: JSON válido, categoria permitida, soma correta, ausência de envio. Use rubricas humanas para clareza e utilidade. Um segundo modelo pode ajudar a avaliar, mas também erra e pode favorecer respostas semelhantes ao seu estilo. Calibre a avaliação automática com exemplos revisados por pessoas.

## Leia as métricas com o denominador
“90% de acerto” pode significar nove casos fáceis em dez ou 900 casos representativos em mil. Registre tamanho, origem e composição do conjunto. A taxa de recusa adequada em perguntas sem evidência é diferente da taxa de respostas corretas em perguntas respondíveis.

Não esconda falhas em uma média. Um sistema que acerta quase tudo, mas executa uma ação não autorizada, pode ser inadequado para o uso planejado. Critérios de bloqueio precisam aparecer separadamente das notas de qualidade.
@exercise
Seu sistema acertou 18 de 20 respostas, mas enviou uma mensagem sem aprovação em um caso. Escreva o relatório de teste sem transformar 90% de acerto em autorização para lançamento.
@answer
O relatório registra 18/20 acertos na dimensão avaliada, descreve os dois erros e destaca a execução não autorizada como falha crítica. A decisão é corrigir o controle, repetir o caso e testar regressões antes de ampliar o uso. A média de qualidade não compensa uma violação do requisito de autorização.
@quiz {"question":"Qual afirmação sobre avaliações é correta?","options":["Métricas precisam de conjunto, denominador e critérios; erros críticos devem aparecer separadamente.","Uma média alta elimina a necessidade de revisar falhas.","Um avaliador de IA nunca precisa de conferência humana."],"correct":0,"explanation":"O significado da métrica depende de como o teste foi construído e de quais erros são aceitáveis."}

@lesson {"id":"custos-observabilidade","title":"Custos, logs e operação previsível","minutes":40,"summary":"Saiba quanto custa concluir uma tarefa e como investigar quando algo falha."}
## Meça a tarefa completa
O custo de um sistema inclui chamadas de modelo, ferramentas, armazenamento, infraestrutura, tentativas extras e revisão humana. Uma opção barata por chamada pode sair cara se falhar com frequência. Meça custo por tarefa aceita, não apenas por resposta gerada.

Use valores hipotéticos para planejar: 500 tarefas, duas chamadas por tarefa e R$ 0,03 por chamada resultam em R$ 30 de geração. Se 10% das tarefas exigirem duas chamadas adicionais, serão mais 100 chamadas e R$ 3. Esse cálculo não representa preços de nenhum provedor.

## Registre eventos úteis
1. Dê um identificador a cada tarefa.
2. Registre versão do prompt, modelo configurado e versão do fluxo.
3. Registre etapa, duração, resultado da validação e ids das fontes.
4. Guarde uso de tokens ou unidades quando informado pelo provedor.
5. Evite armazenar chaves e conteúdo sensível desnecessário.
6. Defina retenção, acesso e remoção para os registros.

Um trace reúne eventos de uma execução para mostrar o caminho percorrido. Logs isolados ajudam, mas sem id de correlação pode ser difícil relacionar a resposta final à ferramenta que falhou.

## Prepare operação e recuperação
Defina limite de orçamento, alerta de falhas, tamanho máximo de entrada e mecanismo de interrupção. Versione prompt, código e configuração. Mantenha uma versão anterior conhecida para rollback quando uma mudança piorar resultados.

Faça lançamento gradual com volume pequeno e observe a taxa de revisão. Tenha um modo de contingência: registrar pedidos para atendimento posterior pode ser melhor que produzir respostas pouco confiáveis durante uma indisponibilidade.

Custos e limites mudam. Consulte a tabela vigente de cada serviço no momento de operar e documente a unidade usada. Não confunda cota de produto de chat com orçamento de uma API ou de uma instância n8n.
@exercise
Calcule o exemplo de 500 tarefas e acrescente 20 revisões humanas de cinco minutos. O que a conta de API não mostra?
@answer
A geração soma R$ 33 no cenário hipotético. As revisões consomem 100 minutos de trabalho humano. Para estimar custo total, você ainda precisa atribuir um valor ao tempo e incluir infraestrutura e outros serviços. O objetivo não é eliminar revisão, mas entender o processo completo e onde melhorias têm impacto.
@quiz {"question":"Qual registro ajuda a reproduzir uma falha?","options":["Somente o texto “deu erro”.", "Id da tarefa, versões, etapa, resultado e fontes relevantes, sem segredos.","Todas as senhas e todos os dados dos usuários."],"correct":1,"explanation":"Observabilidade precisa de contexto técnico suficiente, com minimização e controle de acesso."}

@lesson {"id":"projeto-final-entrega","title":"Entregue seu primeiro sistema de IA","minutes":60,"summary":"Una o que aprendeu em um projeto demonstrável, testado e documentado."}
## A entrega é um sistema pequeno que funciona
Seu projeto final é um assistente para Aurora Cursos. Ele consulta políticas fictícias, responde com evidências e prepara solicitações para revisão. O escopo é deliberadamente limitado para você conseguir testar todas as partes.

Abra o [roteiro do projeto final](#/projeto/assistente-documentos) e baixe o [modelo de documentação](downloads/projeto-final.md). Escolha Python ou n8n conforme o que quer praticar. Você não precisa usar todas as ferramentas do curso no mesmo projeto.

## Construa por marcos
1. **Contrato:** descreva entrada, saída, intenções atendidas e fora de escopo.
2. **Dados:** crie documentos fictícios com ids, versões e responsáveis.
3. **Recuperação:** prove que as perguntas encontram as fontes corretas.
4. **Resposta:** gere ou monte o texto com referências e saída para ausência de evidência.
5. **Controle:** valide formato, ferramentas e ações permitidas.
6. **Automação:** prepare a fila de revisão sem executar efeitos externos indevidos.
7. **Avaliação:** rode pelo menos 20 casos e registre resultados reais.
8. **Entrega:** documente como executar, limitações, custos e procedimento de falha.

## Demonstre também os limites
Uma boa demonstração inclui três casos atendidos, um sem evidência e um adversarial. Mostre o caminho das fontes e o que aconteceu nos registros. Não edite uma falha para parecer acerto; explique como o sistema a conteve e o que ainda precisa melhorar.

Para compartilhar, revise o repositório: nenhuma chave, dado privado ou arquivo de configuração real deve entrar. O frontend estático pode ficar no GitHub Pages. Componentes que usam segredos ou executam Python precisam de ambiente próprio e controles de acesso.

## Um próximo ciclo consciente
Depois de concluir, escolha uma melhoria mensurável: reduzir falhas de recuperação, diminuir tempo de revisão ou ampliar uma intenção. Mude uma parte, repita a avaliação e compare. Aprender IA de forma duradoura significa saber formular, experimentar, medir e revisar — mesmo quando os nomes dos modelos mudam.
@exercise
Prepare uma apresentação de cinco minutos: problema, arquitetura, um caso atendido, uma falha controlada e uma limitação conhecida. Anexe o relatório de testes e uma instrução de execução que outra pessoa consiga seguir.
@answer
A entrega é suficiente quando outra pessoa consegue reproduzir o exemplo com dados fictícios e entender o que o sistema faz e não faz. O relatório deve conter resultados observados, não apenas expectativas. Se as integrações pagas não foram executadas, declare isso e demonstre a parte local ou simulada separadamente.
@quiz {"question":"O que caracteriza uma boa entrega final?","options":["Uma captura bonita sem instruções de execução.","A afirmação de que o sistema nunca erra.","Escopo claro, demonstração reproduzível, testes registrados e limitações explícitas."],"correct":2,"explanation":"A entrega precisa permitir uso e avaliação por outra pessoa, incluindo os limites conhecidos."}
