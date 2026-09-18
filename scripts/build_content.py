"""Compila o conteúdo autoral em JavaScript estático, sem dependências externas."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def build():
    catalog = json.loads((ROOT / 'conteudo/catalogo.json').read_text(encoding='utf-8'))
    if '--partial' in sys.argv:
        catalog['modules'] = [m for m in catalog['modules'] if (ROOT / 'conteudo' / (m['id'] + '.md')).exists()]
    for module in catalog['modules']:
        raw = (ROOT / 'conteudo' / (module['id'] + '.md')).read_text(encoding='utf-8')
        module['lessons'] = []
        for block in raw.split('@lesson ')[1:]:
            meta, body = block.split('\n', 1)
            lesson = json.loads(meta)
            content, rest = body.split('\n@exercise\n', 1)
            exercise, rest = rest.split('\n@answer\n', 1)
            answer, quiz = rest.split('\n@quiz ', 1)
            lesson.update(content=content.strip(), exercise=exercise.strip(), answer=answer.strip(), quiz=json.loads(quiz.strip()))
            module['lessons'].append(lesson)
    (ROOT / 'data/course.js').write_text('window.COURSE = ' + json.dumps(catalog, ensure_ascii=False, indent=2) + ';\n', encoding='utf-8')
    words = sum(len(re.findall(r'\S+', l['content'] + l['exercise'] + l['answer'])) for m in catalog['modules'] for l in m['lessons'])
    print(f"Conteúdo compilado: {len(catalog['modules'])} módulos, {sum(len(m['lessons']) for m in catalog['modules'])} aulas, {words} palavras nas aulas.")

if __name__ == '__main__':
    build()
