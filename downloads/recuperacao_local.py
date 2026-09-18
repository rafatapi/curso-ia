"""Busca lexical educativa. NÃO usa embeddings nem um modelo de IA.

Execute: python recuperacao_local.py "Qual é o prazo de acesso?"
Saída: trechos recuperados e contexto para uma possível etapa de geração.
"""
import re
import sys
import unicodedata

DOCUMENTS = [
    {'id': 'POL-ACESSO-v1', 'title': 'Prazo de acesso', 'text': 'O acesso ao material fica disponível por 90 dias a partir da matrícula.'},
    {'id': 'POL-SUPORTE-v1', 'title': 'Canal de suporte', 'text': 'O suporte responde por e-mail em até dois dias úteis. A política não informa atendimento por telefone.'},
    {'id': 'POL-CERTIFICADO-v1', 'title': 'Certificado de conclusão', 'text': 'O certificado é disponibilizado após concluir todas as atividades obrigatórias do curso.'},
]
STOPWORDS = set('a o as os um uma de da do das dos e em no na nos nas por para com que qual quais como meu minha eu ao ate se ha existe'.split())


def tokens(text):
    clean = ''.join(c for c in unicodedata.normalize('NFD', text.lower()) if unicodedata.category(c) != 'Mn')
    return set(re.findall(r'[a-z0-9]+', clean)) - STOPWORDS


def retrieve(question, limit=2):
    query = tokens(question)
    if not query:
        return []
    results = []
    for doc in DOCUMENTS:
        terms = tokens(doc['title'] + ' ' + doc['text'])
        matches = sorted(query & terms)
        if matches:
            results.append({**doc, 'score': len(matches) / len(query), 'matches': matches})
    return sorted(results, key=lambda d: (-d['score'], d['id']))[:limit]


def main():
    question = ' '.join(sys.argv[1:]).strip() or 'Qual é o prazo de acesso?'
    results = retrieve(question)
    print('Pergunta:', question)
    if not results:
        print('Nenhum trecho recuperado por palavras. Isso NÃO prova que a base não tem a resposta.')
        return
    print('\nCONTEXTO RECUPERADO (pontuação lexical, não confiança):')
    for result in results:
        print(f"\n[{result['id']}] {result['title']} | score={result['score']:.2f}")
        print(result['text'])
        print('Palavras em comum:', ', '.join(result['matches']))
    print('\nPróxima etapa: responder somente com evidências destes trechos e citar seus ids.')
    print('Este laboratório não executa a etapa de geração e não chama serviços externos.')


if __name__ == '__main__':
    main()
