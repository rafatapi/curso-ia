"""Valida conteúdo, referências e exemplos locais sem chamadas a serviços pagos."""
from pathlib import Path
from decimal import Decimal
from collections import defaultdict
import ast
import csv
import importlib.util
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    raw = (ROOT / 'data/course.js').read_text(encoding='utf-8')
    data = json.loads(raw.removeprefix('window.COURSE = ').rstrip().removesuffix(';'))
    check(len(data['modules']) == 16, 'É necessário compilar os 16 módulos.')
    lessons = [l for m in data['modules'] for l in m['lessons']]
    check(len(lessons) == 48, 'Esperadas 48 aulas.')
    ids = [l['id'] for l in lessons]
    check(len(ids) == len(set(ids)), 'Ids de aula duplicados.')
    sources = {s['id'] for s in data['sources']}
    module_ids = {m['id'] for m in data['modules']}
    project_ids = {p['id'] for p in data['projects']}
    for m in data['modules']:
        check(len(m['lessons']) == 3, f"Módulo incompleto: {m['id']}")
        for source in m['sources']:
            check(source in sources, f'Fonte inexistente: {source}')
        for l in m['lessons']:
            check(len(l['content'].split()) >= 220, f"Conteúdo insuficiente: {l['id']}")
            for field in ['exercise', 'answer']:
                check(bool(l[field].strip()), f"Campo ausente {l['id']}: {field}")
            q = l['quiz']
            check(len(q['options']) == 3 and 0 <= q['correct'] < 3 and q['explanation'], f"Quiz inválido: {l['id']}")
            check(l['content'].count('```') % 2 == 0, f"Código não fechado: {l['id']}")
    for d in data['downloads']:
        check((ROOT / d['path']).is_file(), f"Download ausente: {d['path']}")
    for url in re.findall(r'\]\(([^)]+)\)', raw):
        if url.startswith('downloads/'):
            check((ROOT / url).is_file(), f'Link de download quebrado: {url}')
        elif url.startswith('#/projeto/'):
            check(url.split('/')[-1] in project_ids, f'Projeto ausente: {url}')
        elif url.startswith('#/aula/'):
            check(url.split('/')[-1] in ids, f'Aula ausente: {url}')
        elif url.startswith('#/modulo/'):
            check(url.split('/')[-1] in module_ids, f'Módulo ausente: {url}')
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    for path in re.findall(r'(?:src|href)="([^"#]+)"', html):
        if not path.startswith(('http', 'data:')):
            check((ROOT / path).is_file(), f'Asset ausente: {path}')
    for path in ROOT.rglob('*.py'):
        ast.parse(path.read_text(encoding='utf-8'), filename=str(path))

    rows = list(csv.DictReader((ROOT / 'downloads/vendas.csv').open(encoding='utf-8', newline='')))
    seen, totals, valid, errors = set(), defaultdict(Decimal), 0, []
    for row in rows:
        if row['id'] in seen:
            errors.append((row['id'], 'duplicado'))
            continue
        seen.add(row['id'])
        if row['status'] != 'pago' or not row['quantidade']:
            errors.append((row['id'], 'cancelado/incompleto'))
            continue
        totals[row['categoria']] += Decimal(row['quantidade']) * Decimal(row['preco_unitario'])
        valid += 1
    check(valid == 8 and sum(totals.values()) == Decimal('2960'), 'Gabarito financeiro divergente.')
    check(totals == {'Cursos': Decimal('2120'), 'Livros': Decimal('420'), 'Assinaturas': Decimal('420')}, 'Subtotais divergentes.')
    check(len(errors) == 3, 'Exceções divergentes.')

    retrieval = load_module('retrieval', ROOT / 'downloads/recuperacao_local.py')
    check(retrieval.retrieve('Qual é o prazo de acesso?')[0]['id'] == 'POL-ACESSO-v1', 'Recuperação básica falhou.')
    check(not retrieval.retrieve(''), 'Entrada vazia não deve recuperar documentos.')
    check(not retrieval.retrieve('astronomia galáctica'), 'Consulta sem palavras deve retornar vazio.')
    client = load_module('client', ROOT / 'downloads/chamada_api.py')
    fixtures = {
        'openai': {'output': [{'type':'message','content':[{'type':'output_text','text':'OK'}]}]},
        'anthropic': {'content':[{'type':'text','text':'OK'}]},
        'gemini': {'candidates':[{'content':{'parts':[{'text':'OK'}]}}]}
    }
    for provider, payload in fixtures.items():
        check(client.extract_text(provider, payload) == 'OK', f'Extração falhou: {provider}')
        check(client.extract_text(provider, {}) == '', f'Resposta vazia falhou: {provider}')
        result = subprocess.run([sys.executable, str(ROOT / 'downloads/chamada_api.py'), '--dry-run', '--provider', provider], capture_output=True, text=True, check=True)
        check('header_names' in result.stdout, f'Dry-run falhou: {provider}')
    evaluations = list(csv.DictReader((ROOT / 'downloads/avaliacoes.csv').open(encoding='utf-8', newline='')))
    check(len(evaluations) == 20, 'Esperados 20 casos de avaliação.')
    check(len({e['id'] for e in evaluations}) == 20, 'Casos duplicados.')
    print('OK: 16 módulos, 48 aulas completas, quizzes, referências locais e 9 downloads.')
    print('OK: sintaxe Python, dry-run dos 3 provedores, parsers, recuperação lexical e 20 casos de avaliação.')
    print('OK: CSV com 8 pedidos válidos, 3 exceções e receita 2960.00.')
    print('Integrações reais de API, n8n e MCP requerem validação nos serviços/ambientes correspondentes.')


if __name__ == '__main__':
    main()
