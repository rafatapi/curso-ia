@lesson {"id":"ler-imagens","title":"Leia imagens sem inventar detalhes","minutes":30,"summary":"Separe observação, transcrição e interpretação em tarefas visuais."}
## Uma imagem tem informação e limites
Uma fotografia de uma tabela não é a própria tabela. Resolução, ângulo, reflexo e recorte influenciam o que pode ser lido. Sistemas de visão podem confundir caracteres, posição e relações espaciais. Não use uma leitura automática como única validação de um valor importante.

Separe três camadas: **observação** do que aparece, **transcrição** do texto e **interpretação** do significado. “Há uma barra maior” é observação. “A barra representa 120 vendas” exige leitura da escala. “A campanha causou o aumento” é uma conclusão que a imagem sozinha pode não sustentar.

## Um procedimento de leitura
1. Escolha uma imagem própria de uma tabela com cinco linhas.
2. Confira se cabeçalhos, unidades e valores estão legíveis.
3. Peça apenas a transcrição, preservando linhas e colunas.
4. Compare cada célula com a imagem.
5. Corrija a tabela e só então solicite uma análise.

```prompt
Transcreva a tabela da imagem, sem completar dados cortados.
Preserve unidades e cabeçalhos.
Use [ilegível] para valores incertos.
Depois liste ambiguidades que eu preciso conferir.
Não tire conclusões antes de eu validar a transcrição.
```

## O recorte muda a conclusão
Um gráfico sem eixo vertical pode exagerar visualmente uma diferença. Um trecho de documento sem nota de rodapé pode esconder uma condição. Peça para identificar informações que faltam para uma interpretação responsável.

Para descrição acessível, priorize a função da imagem no contexto. Em um gráfico, descreva tendência e valores relevantes; em uma foto decorativa, uma descrição curta pode ser suficiente. Não atribua emoções, intenções ou características pessoais que a imagem não estabelece.
@exercise
Crie uma tabela com valores 12, 18 e 30, tire uma captura e recorte o cabeçalho. Peça uma interpretação. Quais informações o assistente deveria solicitar?
@answer
Ele pode transcrever os valores, mas não sabe a variável, a unidade ou o período sem o cabeçalho. Não deve chamar os valores de reais, vendas ou porcentagens por suposição. Uma resposta adequada separa os números observados das informações necessárias para interpretá-los.
@quiz {"question":"Qual deve vir primeiro na análise de uma tabela fotografada?","options":["Uma recomendação de negócio.","A transcrição conferida de células e unidades.","Uma estimativa de valores cortados."],"correct":1,"explanation":"Erros de leitura contaminam os cálculos e conclusões seguintes."}

@lesson {"id":"gerar-imagens","title":"Crie imagens com um briefing claro","minutes":35,"summary":"Descreva composição, uso e restrições para orientar a geração e a edição."}
## Especifique a peça e seu uso
Um briefing visual deve informar assunto, composição, estilo, formato e finalidade. “Uma imagem bonita de tecnologia” deixa decisões demais abertas. Para a capa de uma aula, pense em espaço para título, contraste e leitura em tamanho pequeno.

Vamos criar uma ilustração conceitual de uma mesa de estudo, sem marcas e sem pessoas identificáveis. Você pode usar um recurso de imagem disponível em um assistente ou outra ferramenta. Não é obrigatório contratar um serviço: o exercício de especificação pode ser feito antes da geração.

## Escreva e revise o briefing
1. Defina o destino: capa horizontal de uma aula.
2. Escolha o elemento principal: caderno, lápis e tela com formas abstratas.
3. Defina a composição e a área que deve ficar livre.
4. Informe estilo e paleta com poucas referências coerentes.
5. Gere uma versão e confira detalhes, texto e aderência ao uso.
6. Faça uma edição pontual, explicando o que precisa mudar e o que deve permanecer.

```prompt
Ilustração editorial horizontal de uma mesa de estudo sobre IA.
Caderno aberto e lápis à direita; espaço livre à esquerda para título.
Paleta verde-escuro, branco e amarelo suave; formas simples.
Sem palavras, logotipos ou marcas. Composição legível em miniatura.
```

## Faça a revisão em tamanho real
Uma imagem pode funcionar ampliada e falhar como miniatura. Confira contraste, recorte e posição do assunto no tamanho de uso. Se houver texto gerado dentro da imagem, revise letra por letra. Para título e informação que precisam de acessibilidade, prefira texto real sobreposto na página, acompanhado de descrição adequada.

Use referências próprias, licenciadas ou permitidas. Registre a origem dos materiais e confira os termos do serviço para o uso pretendido. Uma imagem gerada não deve ser apresentada como registro fotográfico de um evento que nunca aconteceu.
@exercise
Escreva uma solicitação de edição para manter a mesa e os objetos, mas liberar mais espaço à esquerda. Defina dois critérios para aceitar a nova versão.
@answer
Uma instrução possível: “Mantenha estilo, paleta e objetos; desloque o conjunto para o terço direito e deixe metade esquerda sem elementos de destaque”. Critérios: existe área suficiente para o título e os objetos principais continuam reconhecíveis. Não peça mudanças contraditórias, como preencher toda a imagem e preservar grande área vazia.
@quiz {"question":"Qual informação é essencial em um briefing visual?","options":["Apenas a palavra “bonito”.", "Uma lista infinita de estilos incompatíveis.","Finalidade, assunto, composição, formato e restrições."],"correct":2,"explanation":"O briefing conecta a imagem ao uso real e cria critérios objetivos de revisão."}

@lesson {"id":"audio-video","title":"Do áudio ao roteiro de vídeo","minutes":40,"summary":"Construa um fluxo de transcrição, revisão e produção de conteúdo."}
## Separe as etapas de produção
Transcrever é converter fala em texto. Resumir é selecionar informação. Criar um roteiro é reorganizar essa informação para outro formato. Fazer tudo em um único pedido dificulta descobrir onde um erro apareceu.

Grave um áudio próprio de um minuto explicando um conceito. Use uma ferramenta de transcrição disponível e compare o texto com o original. Nomes, números e siglas merecem atenção especial. Se uma palavra estiver incompreensível, marque a incerteza em vez de completar por contexto.

## Transforme com rastreabilidade
1. Revise a transcrição e preserve uma cópia do original.
2. Marque três ideias que não podem desaparecer no resumo.
3. Peça um roteiro de 60 segundos com abertura, explicação e encerramento.
4. Separe narração, cena e texto na tela.
5. Leia em voz alta e ajuste a duração real.
6. Confira legendas e informação factual antes de publicar.

```prompt
Transforme a transcrição revisada em um roteiro de até 60 segundos.
Preserve as três ideias indicadas e não acrescente fatos externos.
Entregue cena, narração e texto na tela.
Use frases curtas e marque os pontos que exigem ilustração.
```

## Um roteiro não é um vídeo pronto
Ferramentas de geração de vídeo podem criar clipes com inconsistências entre cenas, objetos e movimentos. Planeje cenas curtas e revise continuidade. O áudio final precisa combinar com o ritmo visual, e legendas precisam corresponder ao que foi realmente dito.

Use voz e imagem de pessoas com consentimento adequado. Não apresente imitação de uma pessoa como se fosse uma gravação autêntica dela. Para praticar, sua própria voz, personagens fictícios ou narração neutra resolvem o exercício.

Uma boa entrega registra origem do áudio, transcrição revisada, roteiro e alterações editoriais. Isso permite corrigir um erro sem reconstruir todo o processo.
@exercise
Pegue uma explicação de 150 palavras e transforme em roteiro de um minuto. Cronometre sua leitura. Se ultrapassar o tempo, remova redundâncias sem excluir a ideia central.
@answer
Não existe uma quantidade universal de palavras por minuto: velocidade e pausas variam. O teste é ler e medir. Uma revisão adequada reduz repetições, simplifica frases e preserva as três ideias escolhidas. Cortar apenas o encerramento pode deixar o roteiro sem conclusão útil.
@quiz {"question":"Qual fluxo facilita localizar erros?","options":["Transcrever, conferir, resumir, roteirizar e revisar a produção.","Gerar tudo de uma vez e publicar sem assistir.","Usar a duração estimada sem ler o roteiro."],"correct":0,"explanation":"Etapas verificáveis permitem identificar se a falha veio da transcrição, da seleção de conteúdo ou da produção."}
