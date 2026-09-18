@lesson {"id":"pesquisa-verificavel","title":"Pesquise com uma trilha de evidências","minutes":35,"summary":"Transforme uma pergunta ampla em uma pesquisa que pode ser conferida."}
## Delimite antes de buscar
Uma pesquisa útil tem pergunta, período, local e critério de fonte. “Pesquise IA na educação” é grande demais. “Quais orientações uma instituição publicou sobre uso de IA em avaliações em determinado ano?” permite localizar documentos e conferir o resultado.

Use fontes primárias quando disponíveis: documentação do produto, publicação da instituição e estudo original. Uma notícia pode ajudar a descobrir o documento, mas não substitui sua leitura quando a conclusão depende dos detalhes. Diferencie a data do acontecimento da data em que o texto foi publicado.

## Monte uma tabela de evidências
1. Escreva a pergunta e três subperguntas.
2. Peça ao assistente um plano de busca, sem aceitar fatos novos ainda.
3. Use uma ferramenta de pesquisa disponível ou um buscador convencional.
4. Abra cada fonte e registre autor, título, data, link e afirmação sustentada.
5. Marque divergências e lacunas.
6. Só depois redija a síntese.

```prompt
Organize estas fontes em uma matriz de evidências.
Colunas: afirmação, fonte, trecho relevante, data e limitação.
Não adicione fatos de memória nem invente links.
Se duas fontes discordarem, preserve a divergência.
Ao sintetizar, separe fato documentado de interpretação.
```

## Verifique a sustentação, não apenas a existência
Um link real pode não sustentar a afirmação. Uma estatística pode se referir a outro país, período ou grupo. Confira denominador, amostra e condições antes de generalizar. Se a fonte está inacessível, marque isso em vez de fingir que leu.

Ferramentas de busca também podem trazer conteúdo desatualizado. Para informações que mudam, use a documentação vigente e registre a data de consulta. O resultado deve permitir que outra pessoa refaça o caminho e entenda os limites.
@exercise
Pesquise uma funcionalidade atual de uma ferramenta que você usa. Encontre uma fonte oficial e uma secundária. Registre uma afirmação sustentada por cada fonte e uma informação que você não conseguiu confirmar.
@answer
A entrega correta contém links que você realmente abriu, datas e uma distinção entre confirmação e incerteza. Se a notícia diz que um recurso foi anunciado, mas a documentação limita o acesso por plano, a síntese deve preservar essa condição. “Não consegui confirmar” é um resultado válido de pesquisa.
@quiz {"question":"Encontrar um link real basta para validar uma afirmação?","options":["Não. É preciso conferir se o conteúdo sustenta a afirmação no contexto correto.","Sim, qualquer link oficial confirma qualquer frase.","Sim, se aparecer em muitos resumos gerados."],"correct":0,"explanation":"Existência da fonte e sustentação da alegação são verificações diferentes."}

@lesson {"id":"escrita-e-revisao","title":"Escreva com IA sem perder sua intenção","minutes":30,"summary":"Use briefing, rascunho e revisão para chegar a um texto fiel ao objetivo."}
## Primeiro o conteúdo, depois o polimento
Antes de redigir, liste o que o leitor precisa saber e fazer. Um e-mail de alteração de horário precisa informar o horário anterior, o novo, a data e a ação esperada. Um texto elegante que omite a data não resolveu o problema.

Forneça os fatos como uma lista separada das preferências de tom. Peça ao assistente que identifique lacunas antes de preencher detalhes. Para este exercício, use um encontro fictício em 10 de outubro, transferido de 14h para 15h, no mesmo local. Não há justificativa informada para a mudança.

## Trabalhe em três versões
1. Peça um rascunho objetivo com todos os fatos.
2. Confira nomes, datas, horários e ação esperada.
3. Peça uma revisão de clareza sem mudar fatos.
4. Leia em voz alta para detectar frases artificiais.
5. Solicite uma versão curta para mensagem, preservando as informações essenciais.

```prompt
Redija uma mensagem avisando a mudança de horário.
Fatos: encontro de 10 de outubro; de 14h para 15h; mesmo local.
Tom: cordial e direto. Até 80 palavras.
Não invente motivo para a mudança.
Peça que a pessoa confirme o recebimento.
```

## Separe revisão de reescrita
Uma revisão pode apontar problemas sem substituir sua voz. Peça comentários sobre ambiguidade, excesso e organização. Quando uma sugestão altera o sentido, ela deve ser avaliada por você. Não aceite automaticamente promessas como “garantimos” ou “sem qualquer risco” que não constavam no briefing.

Use amostras próprias para explicar seu estilo e evite incluir dados privados desnecessários. Antes de enviar, confira destinatários, anexos e consequências. Produzir um rascunho é diferente de autorizar seu envio.
@exercise
Faça uma versão de e-mail e outra de mensagem curta para a alteração fictícia. Verifique quais fatos sobreviveram à redução e se alguma justificativa foi inventada.
@answer
Ambas devem preservar 10 de outubro, 14h como horário anterior, 15h como novo horário, mesmo local e pedido de confirmação. A versão curta pode dispensar saudações longas, mas não a data. Um motivo como “por problemas técnicos” seria inventado e deve ser removido.
@quiz {"question":"O que deve permanecer estável durante uma revisão de estilo?","options":["A quantidade exata de adjetivos.","Os fatos, o sentido e as restrições do briefing.","Todas as frases, mesmo quando são ambíguas."],"correct":1,"explanation":"Revisar estilo melhora a forma sem alterar silenciosamente a informação ou o compromisso assumido."}

@lesson {"id":"analise-de-dados","title":"Analise dados e confira as contas","minutes":45,"summary":"Trate duplicatas, valores ausentes e unidades antes de interpretar resultados."}
## Entenda o dado antes do gráfico
Baixe [vendas.csv](downloads/vendas.csv). Cada linha representa um pedido; `quantidade` indica unidades; `preco_unitario` está em reais; `status` indica se o pedido foi pago ou cancelado. A receita de uma linha válida é quantidade multiplicada pelo preço unitário.

O arquivo contém problemas intencionais. O id 1003 aparece duas vezes, 1005 está cancelado e 1008 tem quantidade ausente. A regra didática será manter a primeira ocorrência de cada id, excluir cancelados e separar registros incompletos para revisão. Na vida real, uma duplicata com valores diferentes exigiria investigar qual registro é correto.

## Execute uma análise em etapas
1. Conte linhas e identifique os tipos de cada coluna.
2. Separe exceções com o motivo de exclusão.
3. Calcule receita por linha válida.
4. Some por categoria e depois confira o total geral.
5. Calcule participação de cada categoria dividindo pelo total válido.
6. Escreva conclusões descritivas e hipóteses separadamente.

```python
quantidade = 2
preco_unitario = 120
receita = quantidade * preco_unitario
print(receita)  # 240
```

O gabarito do arquivo é: 8 pedidos válidos, receita R$ 2.960,00, sendo Cursos R$ 2.120,00, Livros R$ 420,00 e Assinaturas R$ 420,00. Esses valores são controles para conferir o método, não números a pedir que a IA reproduza sem cálculo.

## Interprete com limites
Cursos representam aproximadamente 71,62% da receita válida; as outras categorias, aproximadamente 14,19% cada. Isso descreve este arquivo. Não demonstra crescimento, satisfação ou efeito de uma campanha, porque faltam dados para essas conclusões.

Para valores monetários em programas reais, use centavos inteiros ou aritmética decimal apropriada. Números de ponto flutuante podem apresentar arredondamentos. O módulo de programação mostra como transformar esse procedimento em código verificável.
@exercise
Explique por que não é correto preencher a quantidade ausente com 1 sem registrar a decisão. Depois calcule quanto o total mudaria se a linha 1008 fosse incluída com essa suposição.
@answer
A quantidade não foi informada. Preencher com 1 cria um dado e altera o resultado. Como o preço unitário da linha 1008 é R$ 100,00, o total passaria para R$ 3.060,00. Essa é uma análise de sensibilidade, não o total válido definido pela regra do exercício. A linha deve permanecer em revisão até receber informação confiável.
@quiz {"question":"Cursos concentram 71,62% da receita deste arquivo. O que é válido concluir?","options":["A campanha de marketing causou o resultado.","As vendas crescerão no mês seguinte.","Cursos têm essa participação na receita válida calculada segundo as regras usadas."],"correct":2,"explanation":"O percentual descreve o conjunto analisado; causalidade e previsão exigem outras evidências."}
