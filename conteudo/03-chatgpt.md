@lesson {"id":"chatgpt-primeiro-fluxo","title":"Sua primeira tarefa no ChatGPT","minutes":30,"summary":"Vá de uma conversa vazia a uma entrega revisada, com etapas claras."}
## Comece pelo resultado
Vamos planejar uma oficina fictícia de introdução a planilhas para 12 pessoas. O resultado esperado é uma agenda de 60 minutos com três atividades e tempo para perguntas. Esse objetivo concreto permite avaliar a resposta.

Entre no [ChatGPT](https://chatgpt.com), confira a conta e abra uma conversa nova. Identifique o campo de mensagem e os recursos disponíveis na sua interface. Modelos, botões e limites podem variar; a tarefa abaixo funciona com texto e não depende de uma opção paga específica.

## Construa em três rodadas
1. Envie os fatos: público iniciante, 12 participantes, 60 minutos, três atividades, dez minutos finais para dúvidas.
2. Peça uma agenda com duração por etapa e materiais necessários.
3. Some os tempos fora da resposta e marque atividades que exigem pré-requisitos não informados.
4. Peça uma revisão focalizada: “A segunda atividade exige fórmulas que ainda não ensinei. Substitua por uma atividade de organização de dados”.
5. Solicite a versão final, mantendo os limites anteriores.

```prompt
Planeje uma oficina de planilhas de 60 minutos para 12 iniciantes.
Inclua três atividades e reserve 10 minutos finais para perguntas.
Mostre etapa, objetivo, duração e material.
Não suponha que as pessoas conhecem fórmulas.
Ao final, informe a soma dos tempos para eu conferir.
```

## Use o histórico com intenção
Uma correção em seguida aproveita o contexto da conversa. Se o assunto mudar completamente, iniciar outra conversa ajuda a evitar instruções antigas interferindo. Para retomar um trabalho longo, produza um resumo de decisões, restrições e pendências; confira esse resumo antes de usá-lo como novo contexto.

Não confunda uma proposta de agenda com eventos criados no calendário. Só há ação externa quando uma ferramenta conectada efetivamente executa e confirma essa operação. Neste exercício, você está gerando um plano.
@exercise
Reduza a oficina para 45 minutos sem eliminar os dez minutos de perguntas. Peça a alteração, confira a soma e registre quais conteúdos precisaram sair.
@answer
Uma agenda possível é: abertura 5 min, organização de dados 10 min, ordenação 10 min, resumo visual 10 min e dúvidas 10 min. Total 45. Não há uma única agenda correta; os critérios são tempo total, três atividades e adequação ao público. Um plano que mantenha todo o conteúdo com tempos inviáveis precisa ser revisado.
@quiz {"question":"O ChatGPT entregou uma agenda em texto. Isso significa que criou eventos no seu calendário?","options":["Sim, qualquer data vira um evento automaticamente.","Não. Uma ação externa depende de ferramenta, conexão, autorização e confirmação de execução.","Sim, se a resposta usar uma tabela."],"correct":1,"explanation":"Planejamento em texto e execução de ações são capacidades distintas."}

@lesson {"id":"chatgpt-arquivos","title":"Arquivos, tabelas e respostas conferíveis","minutes":35,"summary":"Use documentos como entrada e confira se a conclusão realmente vem deles."}
## Dê uma pergunta ao arquivo
Anexar um documento e pedir “analise” deixa o objetivo aberto. Uma análise útil começa com a decisão que você quer apoiar. Para o CSV fictício da biblioteca, a pergunta pode ser: “Qual foi a receita válida por categoria e quais linhas foram excluídas?”.

Se sua conta oferecer anexos, baixe [vendas.csv](downloads/vendas.csv) e envie pelo controle de arquivo. Se não oferecer, abra o CSV em um editor e cole seu conteúdo na mensagem. Os dados são pequenos o suficiente para esse caminho.

## Faça uma inspeção antes da análise
1. Peça os nomes das colunas e o número de registros, sem calcular conclusões ainda.
2. Explique que preço é unitário e quantidade pode estar ausente.
3. Defina duplicidade por id e separe cancelamentos.
4. Peça uma tabela das linhas excluídas e o motivo de cada exclusão.
5. Só então peça a soma e os subtotais.

O assistente pode usar execução de código, dependendo do ambiente. Quando houver cálculo programático, peça o procedimento para conferência. Quando houver apenas texto, não presuma que as operações foram executadas. Em ambos os casos, compare com um cálculo independente.

## Cuidado com documentos que não são texto
Um PDF digitalizado pode conter imagens de páginas. Tabelas mescladas, cabeçalhos repetidos e notas de rodapé podem ser extraídos incorretamente. Para uma informação importante, confira a página original. Se a resposta não consegue indicar onde encontrou um dado, trate a conclusão como pendente de validação.

Para praticar sem arquivos, use esta entrada: pedido A, duas unidades a R$ 40; pedido B, três unidades a R$ 20. A receita total é R$ 140. Esse controle pequeno revela se o método soma preços unitários ou multiplica corretamente.
@exercise
Envie os dois pedidos do exemplo e acrescente um pedido C cancelado de R$ 100. Solicite a receita de pedidos válidos e uma justificativa das exclusões.
@answer
A receita válida continua R$ 140, considerando que A e B são válidos. O pedido C não entra no cálculo por estar cancelado. A resposta deve mostrar 2 × 40 + 3 × 20, em vez de apenas declarar um total. Para o arquivo completo, o projeto de relatório traz o gabarito de controle.
@quiz {"question":"Qual sequência reduz erros na análise de uma planilha?","options":["Gerar um gráfico primeiro e escolher depois as regras de limpeza.","Somar apenas a coluna de preço unitário.","Inspecionar colunas, definir regras, separar exceções e conferir os cálculos."],"correct":2,"explanation":"Sem entender unidade, status e duplicidade, um total pode parecer preciso e estar conceitualmente errado."}

@lesson {"id":"chatgpt-reutilizavel","title":"Organize um trabalho recorrente","minutes":30,"summary":"Transforme uma boa conversa em um procedimento reutilizável."}
## Conversa útil, processo repetível
Se você escreve toda semana um resumo de aula, pode guardar uma instrução que descreve público, estrutura e critérios. Recursos de projeto, personalização e assistentes configurados variam por conta e versão. A ideia central funciona também como um arquivo de texto que você cola no início de uma conversa.

Separe três tipos de informação: regras estáveis, material de referência e dados da tarefa atual. “Use linguagem para iniciantes” é uma regra estável. Uma ementa é referência. O tema da semana é um dado da execução. Misturar tudo dificulta atualizar o processo.

## Monte um kit de trabalho
1. Crie um documento chamado “Instruções do resumo semanal”.
2. Defina objetivo, público, estrutura e situações em que o assistente deve perguntar.
3. Acrescente uma amostra de saída aprovada, sem dados privados.
4. Abra uma conversa nova e teste com um tema diferente.
5. Se usar um recurso de projeto disponível, coloque o kit ali e confirme quais instruções e arquivos estão sendo utilizados.

```prompt
Você ajuda a preparar resumos de aulas introdutórias.
Use somente o material da aula fornecido nesta conversa.
Entregue: ideia central, três conceitos, um exemplo e duas perguntas.
Explique termos técnicos na primeira ocorrência.
Se o material não informar um fato, não complete por suposição.
Antes da versão final, confira se cada conceito aparece no material.
```

## Memória não substitui documentação
Não dependa de o produto lembrar um detalhe importante. Registre critérios explícitos e confira as configurações de memória e dados da sua conta. Guardar preferências é diferente de manter uma base confiável de fatos. Para um trabalho compartilhado, versão e revisão das instruções tornam o processo mais previsível.

Não inclua uma chave de API no kit, em arquivos de conhecimento ou em mensagens. Credenciais pertencem aos mecanismos seguros da aplicação que fará a integração, assunto dos módulos avançados.
@exercise
Adapte o kit para revisar convites de eventos. Teste com um convite sem local e outro com dois horários diferentes. Registre o comportamento esperado antes de executar.
@answer
No convite sem local, o assistente deve pedir o local ou usar um marcador explícito. No convite com horários conflitantes, deve indicar o conflito e pedir resolução, em vez de escolher um silenciosamente. O kit precisa incluir uma regra para campos ausentes e outra para dados contraditórios. Essas regras tornam a revisão reutilizável.
@quiz {"question":"O que deve ficar em uma instrução reutilizável?","options":["Objetivo, critérios, formato e regras para exceções.","Senhas pessoais para facilitar futuras tarefas.","Qualquer fato presumido que o modelo possa completar."],"correct":0,"explanation":"Um procedimento reutilizável descreve o trabalho. Segredos e suposições não verificadas não devem fazer parte dele."}
