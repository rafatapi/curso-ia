@lesson {"id":"copilot-perplexity","title":"Copilot, Perplexity e a escolha por tarefa","minutes":30,"summary":"Compare categorias de produtos sem transformar marcas em respostas universais."}
## O mesmo nome pode representar produtos diferentes
O ecossistema Copilot inclui experiências com finalidades e integrações distintas. Microsoft Copilot, recursos do Microsoft 365 e GitHub Copilot não são simplesmente a mesma ferramenta em telas diferentes. Confira o produto, a licença e o contexto em que está trabalhando.

Perplexity é frequentemente usado como ponto de partida para pesquisa com fontes. Ainda assim, uma resposta com referências precisa de verificação. ChatGPT, Claude e Gemini também podem oferecer ferramentas de pesquisa conforme o ambiente. Compare capacidades disponíveis na sua conta, não uma lista genérica de publicidade.

## Construa uma matriz de decisão
Escolha uma tarefa de escrita, uma de pesquisa e uma de programação. Para cada produto que você consegue acessar, registre: entrada aceita, ferramentas usadas, qualidade da saída, facilidade de revisão, restrições e custo aplicável. Não é necessário assinar vários serviços para fazer uma comparação inicial.

1. Prepare um texto fictício para resumir em cinco tópicos.
2. Prepare uma pergunta factual que exija consultar uma fonte oficial.
3. Prepare uma função pequena com um erro conhecido.
4. Execute apenas as tarefas compatíveis com cada ambiente.
5. Registre quando um recurso não está disponível, em vez de atribuir nota zero ao modelo.

## Escolha o menor conjunto que atende
Se uma ferramenta já resolve bem suas tarefas, aprender outra deve ter um motivo: uma integração necessária, uma capacidade diferente ou uma comparação de qualidade. O custo total inclui assinatura, revisão, troca de contexto e manutenção dos fluxos.

Evite colocar dados reais em vários serviços apenas para comparar respostas. Use o mesmo conjunto fictício. Assim, você pode repetir o teste quando os produtos mudarem sem expor novas informações.
@exercise
Crie uma tabela de três ferramentas por três tarefas. Marque “testado”, “não disponível” ou “não testado”, em vez de preencher com impressões. Escolha uma ferramenta principal e justifique em três critérios.
@answer
Uma decisão defensável pode priorizar integração com seu trabalho, qualidade nos testes e menor tempo de revisão. “É a melhor IA” não é um critério verificável. Se você não testou programação em uma ferramenta, registre a lacuna. A matriz é um retrato das suas condições, não uma classificação universal.
@quiz {"question":"O que torna uma escolha de ferramenta defensável?","options":["Um ranking sem data ou método.","Testes em tarefas relevantes e registro das condições de uso.","A quantidade de funcionalidades anunciadas, sem experimentá-las."],"correct":1,"explanation":"A escolha deve considerar o que você precisa e consegue verificar no ambiente disponível."}

@lesson {"id":"modelos-locais","title":"Modelos locais com Ollama","minutes":40,"summary":"Entenda o que muda quando o modelo roda na sua máquina."}
## Local não significa ilimitado
Executar um modelo localmente pode oferecer mais controle sobre onde a inferência acontece. Em troca, você precisa de armazenamento, memória e capacidade de processamento compatíveis. Tamanho do arquivo não é o único requisito: a execução também precisa de memória para contexto e operações.

Pesos abertos e software de código aberto não são expressões equivalentes. Confira a licença específica do modelo, suas restrições e o uso pretendido. Uma ferramenta pode oferecer tanto execução local quanto serviços em nuvem; confirme qual modalidade foi escolhida.

## Um primeiro teste com Ollama
1. Consulte o guia oficial do Ollama e instale a versão adequada ao seu sistema.
2. Abra um terminal novo e execute `ollama --version` para confirmar a instalação.
3. Escolha, no catálogo oficial, um modelo pequeno compatível com seu computador e confira licença e tamanho.
4. Execute `ollama run NOME_DO_MODELO`, substituindo o marcador pelo nome exato escolhido. A primeira execução pode baixar arquivos grandes.
5. Envie um pedido curto com dados fictícios.
6. Execute `ollama list` para listar modelos instalados e `ollama ps` para observar os carregados.

Não há promessa de desempenho idêntico ao de um serviço hospedado. Compare latência, qualidade e consumo com a mesma tarefa. Se o computador ficar sem memória, reduza o tamanho do modelo ou o contexto em vez de insistir com entradas enormes.

## Verifique a fronteira dos dados
Para um teste local, confirme que está usando um modelo local, sem ferramenta de busca, integração ou rota de nuvem. Uma interface local conectada a uma API remota continua enviando pedidos ao provedor. “A janela está no meu computador” não prova que o processamento está.

O objetivo desta aula é entender a arquitetura. A instalação é opcional: você pode desenhar o caminho dos dados em cada cenário e comparar os requisitos antes de baixar qualquer modelo.
@exercise
Desenhe dois fluxos: navegador → serviço de IA; e aplicação local → modelo local. Acrescente um terceiro em que uma aplicação local chama uma API externa. Em quais casos os dados saem da máquina?
@answer
No primeiro e no terceiro, o pedido é enviado ao serviço remoto. No segundo, a inferência pode ficar local se nenhum componente externo for usado. Instalação, atualizações, telemetria e ferramentas precisam ser analisadas separadamente. O local da interface e o local da inferência são decisões distintas.
@quiz {"question":"Uma interface instalada no computador garante processamento local?","options":["Sim, sempre.","Sim, se tiver modo escuro.","Não. Ela pode usar uma API remota ou uma modalidade de nuvem."],"correct":2,"explanation":"É preciso verificar a configuração e o caminho real dos pedidos."}

@lesson {"id":"benchmark-pessoal","title":"Monte seu próprio teste comparativo","minutes":35,"summary":"Crie um benchmark pequeno que reflita seu trabalho de verdade."}
## Transforme a comparação em um experimento
Um benchmark é um conjunto de tarefas e critérios para comparar sistemas. O seu pode ser pequeno: dez entradas representativas são um começo melhor que uma pergunta divertida escolhida ao acaso. Inclua casos fáceis e difíceis, com respostas esperadas quando possível.

Divida os casos em resumo, extração, classificação e apoio à criação. Para criação, não existe gabarito único; use uma rubrica de aderência ao briefing, clareza e ausência de fatos inventados. Para extração, compare campos específicos com a fonte.

## Registre o que influencia o resultado
1. Dê um identificador a cada caso.
2. Salve o prompt, o material e o resultado esperado.
3. Registre produto, modelo visível, data e ferramentas habilitadas.
4. Execute mais de uma vez quando houver variação relevante.
5. Anote tempo de resposta e tempo de correção humana separadamente.
6. Se possível, avalie as saídas sem ver a marca do produto.

O melhor resultado final pode vir de uma ferramenta que exige menos ajustes, mesmo que responda um pouco mais devagar. Uma resposta rápida e incorreta gera trabalho adicional. Avalie a tarefa concluída, não apenas o tempo até o primeiro texto aparecer.

## Evite adaptar o teste até ele confirmar sua preferência
Separe alguns casos para uma verificação final, sem usá-los durante o ajuste dos prompts. Isso ajuda a detectar quando você melhorou apenas para os exemplos conhecidos. Atualize o conjunto quando seu trabalho mudar e guarde o histórico da comparação.

Você não precisa declarar um campeão. Pode concluir: “uso A para resumo de documentos, B para uma integração específica e revisão manual para casos de alto impacto”. Essa decisão é mais útil que um ranking único.
@exercise
Crie dez casos: três de resumo, três de extração, dois de classificação e dois criativos. Separe dois para o teste final. Defina um erro crítico que reprova a saída independentemente da nota total.
@answer
Um erro crítico pode ser inventar uma data de evento, atribuir uma fala à pessoa errada ou expor um dado que deveria ser omitido. O teste final precisa usar casos guardados antes da melhoria dos prompts. Documente também limitações do conjunto: poucas amostras não representam todos os assuntos e idiomas.
@quiz {"question":"Por que reservar casos que não foram usados para ajustar o prompt?","options":["Para verificar se a melhora se estende a exemplos novos.","Para esconder os erros.","Para garantir que qualquer modelo será perfeito."],"correct":0,"explanation":"Casos novos ajudam a detectar adaptação excessiva aos exemplos conhecidos, sem garantir desempenho universal."}
