"""Offline checks only; never connect to accounts or invoke MCP tools."""
import base64
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = 'https://api.zerorank.ai/mcp'

def validate_study_files():
    for manifest in (ROOT / 'data').glob('*/metadata.json'):
        study = json.loads(manifest.read_text())
        for file in study['files']:
            name = file['path']
            content = (manifest.parent / name).read_bytes()
            assert hashlib.sha256(content).hexdigest() == file['sha256'], name
            rows = [json.loads(line) for line in content.decode('utf-8').splitlines()]
            assert len(rows) == file['records'], name
            assert len({row[file['primary_key']] for row in rows}) == len(rows), name
            assert all(row.keys() == study['fields'][name].keys() for row in rows), name

def main():
    validate_study_files()
    for path in ROOT.rglob('*.json'):
        json.loads(path.read_text())
    inventory = json.loads((ROOT / 'metadata/tools.json').read_text())
    tools = inventory['tools']
    names = {t['name'] for t in tools}
    assert len(names) == len(tools) == 45
    assert sum(t['annotations']['readOnlyHint'] is True for t in tools) == 24
    reference = (ROOT / 'docs/tools.md').read_text()
    for tool in tools:
        assert f"## `{tool['name']}`" in reference
        assert tool['inputSchema']['type'] == 'object'
    for file in ('tools.json', 'clients.json', 'install-links.json'):
        assert (ROOT / 'mcp/metadata' / file).read_bytes() == (ROOT / 'metadata' / file).read_bytes()
    assert (ROOT / 'mcp/tools.md').read_bytes() == (ROOT / 'docs/tools.md').read_bytes()
    links = json.loads((ROOT / 'metadata/install-links.json').read_text())
    for key in ('cursor', 'cursor_deeplink'):
        link = links[key]
        query = parse_qs(urlparse(link).query)
        assert query['name'] == ['zerorank']
        assert json.loads(base64.b64decode(query['config'][0], validate=True)) == {'url': ENDPOINT}
    assert links['cursor'] in (ROOT / 'mcp/README.md').read_text()
    for key in ('vscode', 'vscode_insiders'):
        assert json.loads(unquote(urlparse(links[key]).query)) == {'name': 'zerorank', 'type': 'http', 'url': ENDPOINT}
    clients = json.loads((ROOT / 'metadata/clients.json').read_text())['clients']
    assert len({c['id'] for c in clients}) == len(clients) == 21
    for c in clients:
        assert f"## {c['id']}" in (ROOT / 'docs/clients.md').read_text()
        assert c['source'].startswith('https://')
    for path in (ROOT / 'examples').glob('*.json'):
        assert ENDPOINT in path.read_text()
        assert 'Authorization' not in path.read_text()

    cursor = json.loads((ROOT / 'examples/cursor.mcp.json').read_text())
    vscode = json.loads((ROOT / 'examples/vscode.mcp.json').read_text())
    assert cursor['mcpServers']['zerorank'] == {'url': ENDPOINT}
    assert vscode['mcpServers']['zerorank'] == {
        'type': 'http', 'url': ENDPOINT, 'tools': ['list_workspaces', 'list_chats', 'get_chat']
    }
    opencode = json.loads((ROOT / 'examples/opencode.mcp.json').read_text())
    assert opencode['mcp']['servers']['zerorank'] == {'type': 'remote', 'url': ENDPOINT}
    server = json.loads((ROOT / 'server.json').read_text())
    assert server['remotes'] == [{'type': 'streamable-http', 'url': ENDPOINT}]
    for path in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if urlparse(target).scheme or target.startswith('#'):
                continue
            assert (path.parent / unquote(target.split('#')[0])).exists(), (path, target)
    print('PASS: study files, JSON, 45-tool inventory, encoded install links, client configurations and local Markdown links')

if __name__ == '__main__':
    main()
