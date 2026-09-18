"""Servidor de estudo, somente leitura e dados fictícios.

Dependência: mcp[cli]>=1.28,<2 (SDK oficial, linha 1.x).
Inspecionar: mcp dev servidor_mcp.py
Transporte: stdio. Não é servidor HTTP; precisa de um cliente MCP.
"""
from typing import Literal
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Politicas Aurora - laboratorio')
POLICIES = {
    'acesso': {'id': 'POL-ACESSO', 'versao': '1', 'texto': 'O material fica disponível por 90 dias a partir da matrícula.'},
    'suporte': {'id': 'POL-SUPORTE', 'versao': '1', 'texto': 'O suporte responde por e-mail em até dois dias úteis. Telefone não informado.'},
    'certificado': {'id': 'POL-CERTIFICADO', 'versao': '1', 'texto': 'O certificado depende da conclusão de todas as atividades obrigatórias.'},
}


@mcp.tool()
def consultar_politica(topico: Literal['acesso', 'suporte', 'certificado']) -> dict:
    """Consulta uma política fictícia. Somente leitura; não executa ações externas."""
    if topico not in POLICIES:
        raise ValueError('Tópico não permitido.')
    return {'ok': True, 'politica': dict(POLICIES[topico])}


if __name__ == '__main__':
    mcp.run(transport='stdio')
