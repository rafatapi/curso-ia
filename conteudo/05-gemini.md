@lesson {"id":"gemini-primeira-conversa","title":"Comece no Gemini e compare resultados","minutes":30,"summary":"Use o mesmo problema para conhecer outra forma de trabalhar com IA."}
## Mantenha a tarefa, troque o assistente
Abra [Gemini](https://gemini.google.com) e confira a conta em uso. Contas pessoais, escolares e de trabalho podem ter recursos diferentes. Para comparar produtos, use uma tarefa de texto que esteja disponível em ambos; não atribua ao modelo uma diferença causada por uma ferramenta adicional.

Retome a oficina de 60 minutos para 12 iniciantes, com três atividades e dez minutos de perguntas. Envie exatamente os mesmos fatos usados no ChatGPT. Registre o produto, a data e, quando visível, o modelo selecionado. Esses detalhes ajudam a interpretar a comparação depois.

## Compare por critérios
1. Peça uma agenda com objetivos, tempos e materiais.
2. Some os tempos e confira os pré-requisitos.
3. Conte os fatos inventados, como preço ou certificado.
4. Avalie a facilidade de adaptar a resposta.
5. Faça uma segunda execução em conversa nova antes de concluir.

Um produto pode responder melhor em uma tarefa e pior em outra. Não transforme uma única experiência em um ranking universal. O que interessa é a utilidade no seu conjunto de tarefas, considerando custo, recursos, privacidade e tempo de revisão.

## Use imagens quando a tarefa pedir
Se o recurso estiver disponível, adicione uma imagem própria de uma tabela simples. Peça primeiro a transcrição, depois a interpretação. Separar as etapas permite descobrir se uma conclusão errada surgiu da leitura da imagem ou do raciocínio posterior.

```prompt
Leia esta imagem e transcreva os valores em uma tabela.
Marque [ilegível] onde não tiver segurança.
Não estime valores ausentes.
Depois de eu conferir a transcrição, faremos os cálculos.
```

Para imagens pequenas, textos cortados ou gráficos sem escala clara, o melhor resultado pode ser uma limitação explícita. Uma resposta incompleta e honesta é mais útil que números inventados.
@exercise
Compare uma resposta do Gemini e uma do assistente que você já usa. Dê 0 a 2 pontos para adequação ao público, respeito ao tempo, fidelidade aos fatos e clareza. Registre também o tempo que gastou revisando.
@answer
Uma comparação útil mostra as notas e exemplos concretos: “somou 65 minutos”, “usou uma fórmula não ensinada” ou “preservou todos os fatos”. O vencedor do exercício é o mais adequado à tarefa avaliada. Uma diferença de nota em apenas duas respostas não demonstra superioridade geral do produto.
@quiz {"question":"Como comparar dois assistentes de maneira mais justa?","options":["Dar fontes diferentes para cada um.","Escolher pelo tamanho da resposta.","Usar os mesmos fatos, critérios e condições, registrando diferenças de ferramentas."],"correct":2,"explanation":"Comparações precisam controlar a tarefa e reconhecer quando um ambiente tem ferramentas que o outro não possui."}

@lesson {"id":"gemini-gems","title":"Instruções reutilizáveis e integrações","minutes":30,"summary":"Crie um assistente com um objetivo definido e entenda o alcance das conexões."}
## Personalize uma tarefa, não uma personalidade vaga
Recursos de assistentes personalizados, como Gems quando disponíveis, permitem reutilizar instruções. Escolha uma função pequena: revisar planos de aula, preparar perguntas ou resumir notas. “Resolver toda a minha vida” é amplo demais para avaliar.

Vamos criar um revisor de planos de aula. Ele deve verificar se objetivos, atividades e avaliação estão alinhados. Forneça uma rubrica explícita e um exemplo fictício. Se o recurso de personalização não aparecer na sua conta, mantenha as instruções em um arquivo e use-as em conversas novas.

## Configure e teste
1. Escolha um nome que descreva a tarefa, como “Revisor de aula introdutória”.
2. Defina entradas: público, duração, objetivos e atividades.
3. Defina saída: inconsistências, sugestão de ajuste e perguntas pendentes.
4. Inclua a regra de não inventar informações ausentes.
5. Teste um plano completo e outro sem duração.

```prompt
Revise planos de aula para iniciantes.
Confira alinhamento entre objetivo, atividade e avaliação.
Não reescreva o plano inteiro sem necessidade.
Liste no máximo cinco problemas, com justificativa e ajuste sugerido.
Se faltarem público ou duração, pergunte antes de avaliar a viabilidade.
```

## Conexões têm fronteiras
Uma integração com outro aplicativo pode permitir consultar ou atuar sobre dados, conforme as permissões. Antes de conectar, entenda qual conta será usada e o que fica acessível. Uma capacidade de consulta não implica autorização para enviar mensagens ou modificar documentos.

Faça o primeiro teste com um documento fictício e uma tarefa de leitura. Confira a fonte aberta e a resposta. Para ações de escrita, estabeleça antes o que deve mudar e como você verificará a alteração. A presença de uma integração não dispensa esse cuidado operacional.
@exercise
Teste o revisor com um plano de 30 minutos que contém quatro atividades de dez minutos cada. Depois retire a duração. O que deve acontecer em cada caso?
@answer
No primeiro caso, o revisor deve apontar que 40 minutos de atividades excedem os 30 disponíveis, antes de considerar abertura ou encerramento. No segundo, deve pedir a duração em vez de presumir que o plano cabe. Esse par de testes verifica tanto detecção de inconsistência quanto tratamento de informação ausente.
@quiz {"question":"Qual é uma boa primeira tarefa ao conectar um aplicativo?","options":["Uma consulta limitada a material fictício, conferindo a conta e o alcance do acesso.","Enviar mensagens para todos os contatos para testar.","Presumir que qualquer integração é somente leitura."],"correct":0,"explanation":"Um teste pequeno e verificável ajuda a entender o alcance da conexão antes de depender dela."}

@lesson {"id":"notebooklm-fontes","title":"NotebookLM e estudo apoiado em fontes","minutes":35,"summary":"Monte um caderno de pesquisa e acompanhe de onde cada resposta veio."}
## Comece por um conjunto de fontes
O fluxo de estudo associado ao NotebookLM organiza materiais em um caderno e permite explorá-los com assistência de IA. Nomes e integração com o ecossistema Gemini podem mudar; a central oficial de ajuda acompanha essas alterações. O método desta aula permanece: selecionar fontes, perguntar, abrir a evidência e conferir.

Escolha dois textos curtos e públicos sobre o mesmo assunto, de autores diferentes. Evite começar com dezenas de arquivos: você precisa conhecer o material para avaliar a resposta. Registre título, data e origem de cada fonte.

## Construa seu caderno
1. Abra o produto pela central oficial indicada nas fontes e crie um caderno, se disponível em sua conta.
2. Adicione os dois materiais em um formato aceito e confirme se foram processados.
3. Peça os conceitos em comum, com referência à fonte de cada afirmação.
4. Abra as referências apresentadas e leia o trecho completo.
5. Pergunte onde os textos divergem e se a divergência é de fato, definição ou opinião.
6. Faça uma pergunta cuja resposta não aparece em nenhum dos documentos.

## Citação não é comprovação automática
Uma referência pode apontar para uma seção relacionada, mas não sustentar a conclusão inteira. Confira o contexto, a data e as condições. Se um documento fala de um caso específico, a resposta não deve transformar esse caso em uma regra geral.

Resumos, perguntas e formatos de estudo gerados são materiais auxiliares. Mesmo quando uma função produz áudio ou outro formato, confira o conteúdo na fonte. Uma narração fluente não corrige uma interpretação incorreta.

Se você não tiver acesso ao produto, faça a atividade em qualquer assistente colando dois trechos identificados como Fonte A e Fonte B. O objetivo é aprender a relação entre alegação e evidência, não depender de um botão específico.
@exercise
Use dois textos fictícios: A recomenda encontros semanais de 30 minutos; B descreve encontros quinzenais de 60 minutos. Peça semelhanças e diferenças, sem concluir que um método é superior.
@answer
Ambos descrevem encontros periódicos. Eles diferem em frequência e duração. Em quatro semanas, o tempo nominal pode ser igual se houver quatro encontros no plano A e dois no B, mas isso não prova o mesmo resultado de aprendizagem. Não há evidência suficiente para declarar superioridade de um formato.
@quiz {"question":"Uma resposta tem uma citação. Qual é o próximo passo?","options":["Aceitar sem ler porque a presença do link basta.","Abrir o trecho e verificar se sustenta a afirmação nas condições apresentadas.","Remover a referência para simplificar o texto."],"correct":1,"explanation":"A relação entre afirmação e evidência precisa ser conferida; referências podem ser incompletas ou interpretadas incorretamente."}
