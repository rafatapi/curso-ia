@lesson {"id":"o-que-e-ia","title":"Inteligência artificial, sem mistério","minutes":25,"summary":"Entenda o que a IA faz, como aprende e onde entra no seu dia a dia."}
## Um mapa antes das ferramentas
Inteligência artificial é o campo que constrói sistemas capazes de realizar tarefas como reconhecer padrões, fazer previsões e produzir respostas. Não é um único aplicativo. Um filtro de spam, um sistema de recomendação e um assistente de texto podem usar técnicas diferentes de IA.

**Aprendizado de máquina** é uma abordagem: em vez de escrever uma regra para cada situação, fornecemos exemplos para um sistema ajustar seus parâmetros. No treinamento de um classificador de spam, mensagens conhecidas ajudam a aprender padrões. Na inferência, o modelo treinado recebe uma mensagem nova e calcula uma previsão.

**Deep learning** utiliza redes neurais com várias camadas. **IA generativa** produz conteúdo, como texto, imagem e áudio. Um **LLM** é um modelo de linguagem de grande porte. Ele aprende regularidades a partir de dados e gera sequências de tokens. Essa capacidade não garante que a informação produzida seja verdadeira.

## Modelo, aplicativo e ferramenta
Pense em três peças: o modelo produz uma resposta; o aplicativo organiza sua conversa; as ferramentas permitem ações adicionais, como consultar uma página ou executar código. ChatGPT, Claude e Gemini são nomes associados a produtos e famílias de modelos, com capacidades que dependem do ambiente usado.

Um modelo sem uma ferramenta de consulta não ganha acesso à sua agenda só porque você pediu. Um assistente com essa integração ainda precisa da conexão e das permissões apropriadas. Ao aprender a separar essas peças, você entende melhor o que está realmente disponível.

## Seu primeiro experimento
1. Abra o assistente de sua preferência e inicie uma conversa vazia.
2. Peça: “Explique aprendizado de máquina usando o exemplo de separar frutas, em até 100 palavras”.
3. Peça uma segunda explicação para alguém que já programa.
4. Compare vocabulário, exemplos e pressupostos. O assunto permanece, mas a apresentação muda.

> Nesta trilha, use dados fictícios. Não é preciso compartilhar informações pessoais para aprender.

@exercise
Classifique três situações: uma fórmula que soma valores, um sistema treinado para detectar spam e um assistente que redige um resumo. Qual usa regras explícitas? Qual faz previsão? Qual gera conteúdo? Escreva uma frase justificando cada escolha.
@answer
A soma com uma fórmula é uma operação determinística: o procedimento está definido. O classificador de spam usa padrões aprendidos para prever uma classe. O assistente de resumo gera texto com base na entrada. As categorias podem se combinar em um produto: uma IA pode chamar uma calculadora para obter uma soma exata. O importante é identificar qual componente resolve cada parte.
@quiz {"question":"Qual afirmação descreve melhor um modelo de linguagem?","options":["É um banco de dados que sempre encontra fatos exatos.","Gera sequências a partir de padrões aprendidos e pode cometer erros.","Tem acesso automático à internet e aos seus arquivos."],"correct":1,"explanation":"Gerar uma resposta plausível é diferente de verificar um fato. Busca, arquivos e outras ações dependem das ferramentas e permissões do aplicativo."}

@lesson {"id":"tokens-contexto","title":"Tokens, contexto e alucinações","minutes":30,"summary":"Descubra por que uma resposta pode soar certa e ainda estar errada."}
## As peças de uma conversa
Um token é uma unidade de representação do modelo: pode corresponder a uma palavra, parte de palavra ou sinal. Não existe uma conversão fixa de palavras para tokens válida para todos os idiomas e modelos. Os provedores normalmente contabilizam tokens de entrada e saída para limites e cobrança de APIs.

**Janela de contexto** é a quantidade de informação que o modelo consegue considerar em uma interação, conforme seus limites. Instruções, histórico, arquivos e respostas de ferramentas podem ocupar espaço. Uma janela grande não garante atenção perfeita a cada detalhe. É melhor organizar a informação do que despejar documentos sem objetivo.

Contexto da conversa, memória persistente e conhecimento aprendido no treinamento são coisas diferentes. Uma aplicação pode guardar preferências entre conversas; isso não significa que o modelo foi retreinado com cada mensagem. Também não significa que lembrará tudo.

## Quando o texto inventa uma certeza
Chamamos de alucinação uma resposta sem suporte confiável, como uma referência que não existe ou uma data inventada. Pedir “tenha certeza” não elimina esse problema. Três práticas ajudam: fornecer a fonte, permitir “não encontrei” e conferir as alegações importantes fora da resposta.

Considere uma política fictícia: “O curso oferece suporte por e-mail de segunda a sexta. O prazo médio é dois dias úteis”. Se você perguntar sobre suporte por telefone, a resposta correta é que a fonte não informa. Inventar um número de telefone seria um erro, mesmo que pareça útil.

## Faça a resposta mostrar seus limites
1. Cole apenas a política acima em uma conversa nova.
2. Peça uma resposta sobre telefone, limitada à política.
3. Solicite a frase exata que sustenta a conclusão.
4. Compare a frase com a fonte original; uma citação também pode ser fabricada.

```prompt
Responda usando apenas a política fornecida.
Se ela não responder à pergunta, diga “não informado”.
Separe: resposta, trecho de apoio e informação ausente.
Pergunta: existe suporte por telefone?
```
@exercise
Acrescente “Atendimento telefônico somente para empresas” à política. Faça novamente a pergunta e registre como a resposta deve mudar. Depois pergunte sobre o número do telefone.
@answer
A nova fonte permite afirmar que existe atendimento telefônico para empresas. Ainda não permite inventar um número. A resposta sobre o número deve continuar “não informado”. O exercício distingue evidência parcial de ausência completa de evidência: um sistema confiável responde o que sabe e explicita o que falta.
@quiz {"question":"Um arquivo enorme dentro da janela de contexto garante uma resposta correta?","options":["Não. Caber no contexto não garante compreensão, recuperação ou verificação perfeita.","Sim, desde que seja um PDF.","Sim, se a conversa for longa."],"correct":0,"explanation":"Limites de contexto são limites de capacidade. Organização da entrada e conferência da resposta continuam necessárias."}

@lesson {"id":"avaliar-e-proteger","title":"Critério, privacidade e uso responsável","minutes":30,"summary":"Crie um método para avaliar respostas antes de depender delas."}
## Troque impressão por critério
Uma resposta longa pode ser incompleta. Uma resposta convincente pode estar errada. Antes de usar IA, defina o que significaria acertar. Para resumir uma reunião, avalie se preserva decisões, responsáveis e prazos. Para gerar uma campanha, avalie tom, restrições e adequação ao público. Critérios diferentes exigem testes diferentes.

Use uma rubrica de 0 a 2 em quatro dimensões: **correção**, **completude**, **formato** e **fidelidade à fonte**. Zero significa falha; um, atendimento parcial; dois, atendimento satisfatório. O total ajuda a comparar versões, mas não compensa um erro crítico: um prazo inventado pode reprovar uma resposta mesmo com bom estilo.

## Prepare dados antes de enviar
Minimização significa usar apenas os dados necessários. Troque nomes reais por identificadores e remova informações que não contribuem para a tarefa. Pseudonimizar não equivale automaticamente a anonimizar: o restante do texto pode permitir identificar a pessoa.

Antes de usar um documento real, confira as regras da sua organização e as configurações do serviço. Retenção, uso de dados e acesso variam por produto, plano e conta. Este curso ensina práticas operacionais; questões jurídicas específicas precisam de avaliação especializada.

## Um ritual de revisão
1. Defina a saída e o critério de aceitação antes de abrir o chat.
2. Remova dados desnecessários da entrada.
3. Identifique quais afirmações da resposta dependem de uma fonte externa.
4. Confira números e links no original.
5. Revise consequências antes de enviar ou executar algo.

Viés é outra fonte de falha: um modelo pode reproduzir estereótipos ou tratar casos semelhantes de forma desigual. Para detectar isso, repita o teste alterando características irrelevantes para a decisão e compare os resultados. Não automatize decisões importantes sobre pessoas apenas com uma resposta gerada.
@exercise
Imagine que um resumo de reunião acertou o assunto, omitiu o responsável e inventou uma entrega para sexta-feira. Dê uma nota em cada critério e decida se você enviaria esse resumo.
@answer
Uma avaliação possível: correção 0 pelo prazo inventado; completude 1 pela omissão; formato 2 se respeitou o pedido; fidelidade 0 pela informação sem fonte. Total 3/8. Mais importante que a nota é a decisão: não enviar antes de corrigir prazo e responsável a partir da ata. Registrar a falha ajuda a melhorar o próximo prompt e o conjunto de testes.
@quiz {"question":"Qual é a melhor preparação para usar uma ata interna em um assistente?","options":["Enviar tudo, porque mais informação sempre melhora a resposta.","Apagar só o título do arquivo.","Verificar autorização e regras do serviço, remover dados desnecessários e revisar a saída."],"correct":2,"explanation":"A preparação deve considerar necessidade dos dados, autorização e revisão. Remover um nome isoladamente pode não impedir identificação."}
