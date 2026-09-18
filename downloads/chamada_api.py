"""Laboratório de API: Python 3.11+, sem dependências externas.

Sem rede: python chamada_api.py --dry-run --provider gemini
Com rede: configure AI_PROVIDER, AI_MODEL e AI_API_KEY; execute sem --dry-run.
Chamadas reais podem gerar cobrança. Nunca publique sua chave.
"""
import argparse
import json
import os
import re
import socket
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def make_request(provider, model, key, prompt, workspace=None):
    if not re.fullmatch(r'[A-Za-z0-9._:-]+', model):
        raise ValueError('Use o identificador simples do modelo, sem URL ou caminho.')
    headers = {'Content-Type': 'application/json'}
    if provider == 'openai':
        url = 'https://api.openai.com/v1/responses'
        headers['Authorization'] = 'Bearer ' + key
        payload = {'model': model, 'input': prompt, 'max_output_tokens': 500}
    elif provider == 'anthropic':
        url = 'https://api.anthropic.com/v1/messages'
        headers.update({'x-api-key': key, 'anthropic-version': '2023-06-01'})
        if workspace:
            headers['anthropic-workspace-id'] = workspace
        payload = {'model': model, 'max_tokens': 500, 'messages': [{'role': 'user', 'content': prompt}]}
    elif provider == 'gemini':
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
        headers['x-goog-api-key'] = key
        payload = {'contents': [{'role': 'user', 'parts': [{'text': prompt}]}], 'generationConfig': {'maxOutputTokens': 500}}
    else:
        raise ValueError('Provedor não suportado.')
    return url, headers, payload


def extract_text(provider, data):
    if provider == 'openai':
        parts = [part.get('text', '') for item in data.get('output', []) if item.get('type') == 'message' for part in item.get('content', []) if part.get('type') == 'output_text']
    elif provider == 'anthropic':
        parts = [part.get('text', '') for part in data.get('content', []) if part.get('type') == 'text']
    else:
        parts = [part.get('text', '') for candidate in data.get('candidates', []) for part in candidate.get('content', {}).get('parts', []) if not part.get('thought', False)]
    return '\n'.join(part for part in parts if part)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true', help='Mostra apenas a estrutura, sem rede e sem chave.')
    parser.add_argument('--provider', choices=['openai', 'anthropic', 'gemini'], default=os.getenv('AI_PROVIDER', 'openai'))
    parser.add_argument('--prompt', default='Explique o que é uma API em duas frases para uma pessoa iniciante.')
    args = parser.parse_args()
    model = os.getenv('AI_MODEL', '')
    key = os.getenv('AI_API_KEY', '')
    if not args.dry_run and (not model or not key or model.startswith('SUBSTITUA')):
        parser.error('Configure AI_MODEL com um modelo compatível e AI_API_KEY. Use --dry-run para experimentar sem rede.')
    try:
        url, headers, payload = make_request(args.provider, model or 'MODELO_DA_SUA_CONTA', key, args.prompt, os.getenv('AI_WORKSPACE_ID'))
    except ValueError as error:
        parser.error(str(error))
    if args.dry_run:
        print(json.dumps({'mode': 'dry-run, nenhuma chamada realizada', 'url': url, 'header_names': list(headers), 'body': payload}, ensure_ascii=False, indent=2))
        return 0
    request = Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
    try:
        with urlopen(request, timeout=45) as response:
            data = json.loads(response.read().decode('utf-8'))
    except HTTPError as error:
        # Não imprime corpo de erro, cabeçalhos ou credenciais.
        print(f'Erro HTTP {error.code}. Confira credencial, modelo, parâmetros e limites no painel do provedor.', file=sys.stderr)
        return 1
    except (URLError, TimeoutError, socket.timeout):
        print('Falha de conexão ou timeout. Não houve repetição automática; confira o estado antes de repetir.', file=sys.stderr)
        return 1
    except (json.JSONDecodeError, UnicodeDecodeError):
        print('O servidor retornou um corpo que não foi reconhecido como JSON UTF-8.', file=sys.stderr)
        return 1
    text = extract_text(args.provider, data)
    print(text or 'Nenhum texto encontrado. Pode haver recusa, interrupção ou formato inesperado.')
    usage = data.get('usage', data.get('usageMetadata', {}))
    print('\nUso informado:', json.dumps(usage, ensure_ascii=False))
    stop = data.get('status') or data.get('stop_reason') or [c.get('finishReason') for c in data.get('candidates', [])]
    print('Status/finalização:', stop)
    return 0 if text else 2


if __name__ == '__main__':
    raise SystemExit(main())
