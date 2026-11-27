# Connect an agent to ZeroRank

[Official ZeroRank MCP setup guide](https://docs.zerorank.ai/integrations/mcp-server) · [ZeroRank documentation index for agents](https://docs.zerorank.ai/llms.txt)

1. Use the user's existing MCP client. ZeroRank’s sidebar has connection instructions under **Developer → MCP**. Configure `https://api.zerorank.ai/mcp` with Streamable HTTP and OAuth. Preserve existing client settings. [Client guide](mcp/clients.md) · [Connection examples](docs/connection.md)
2. Let the user complete browser authentication. Do not ask for tokens or put credentials in repository files. A REST API key is not the MCP OAuth credential.
3. Refresh the server’s tool list after sign-in. Review the workspace permissions and requested action before making changes. [Current tool reference](mcp/tools.md) · [Machine-readable inventory](mcp/metadata/tools.json) · [Changelog](https://zerorank.ai/changelog)
4. Call `list_workspaces` with `{}`. Resolve the user's intended workspace and use its returned `workspaceId`; never invent IDs or assume the first workspace is correct.
5. Use `get_workspace` to confirm the workspace name. Use `list_chats` with `limit: 1` to read one recent chat.
6. Read [AGENTS.md](AGENTS.md) and [workflows](docs/workflows.md) before actions that change data or spend answer-run budget.

This is a hosted integration. There is no local ZeroRank server to build or npm package to execute from this repository.

Check the installed client version before using a setup command. Pi’s native MCP support requires version 0.99.0 or later.
