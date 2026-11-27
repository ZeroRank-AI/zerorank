# Connect an assistant to ZeroRank MCP

Open **Developer → MCP** in your ZeroRank workspace for setup instructions. Our [MCP developer guide](https://docs.zerorank.ai/integrations/mcp-server) explains browser sign-in, and our [MCP product page](https://zerorank.ai/platform/mcp) describes the hosted service.

| Setting | Value |
| --- | --- |
| Server URL | `https://api.zerorank.ai/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth through your browser |

## Cursor

[Install ZeroRank](https://cursor.com/en/install-mcp?name=zerorank&config=eyJ1cmwiOiJodHRwczovL2FwaS56ZXJvcmFuay5haS9tY3AifQ%3D%3D), review the server configuration, and complete the sign-in flow. If your browser cannot launch Cursor, add this entry to your existing Cursor MCP configuration. Merge it with other servers instead of replacing the entire file.

```json
{
  "mcpServers": {
    "zerorank": {
      "url": "https://api.zerorank.ai/mcp"
    }
  }
}
```

A copy is available in [examples/cursor.mcp.json](../examples/cursor.mcp.json).

## VS Code

In the Command Palette, choose **MCP: Add Server**, select **HTTP**, and enter `https://api.zerorank.ai/mcp`. Complete OAuth when the client prompts you.

For a Copilot-managed session, our [Copilot configuration example](../examples/vscode.mcp.json) uses `mcpServers` and enables the three tools for reading one saved answer. Follow the instructions for your harness and configuration file in [Microsoft’s MCP configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration).

## Confirm the connection

Ask the assistant to call `list_workspaces` with no arguments. Select the intended workspace by name and use its returned ID. Do not choose the first workspace automatically, especially for writes. Read `get_workspace` and `get_workspace_models` before planning changes or paid runs.

## Troubleshooting

- For HTTP 401, start the client’s ZeroRank OAuth sign-in and reconnect.
- If access is denied, check your subscription/trial, workspace access and role.
- If tools are missing after a server update, reconnect or refresh the client's tool list.
- If an operation returns a prompt or answer-run limit error, inspect the workspace and budget before retrying a billable action.
- If results are not ready, check progress with the appropriate read tool.

## Reference implementations

- [Cursor install link format](https://cursor.com/docs/mcp/install-links)
- [VS Code MCP setup and CLI](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

## More clients

See the [client guide](clients.md) for Codex, ChatGPT, Claude, Gemini CLI, Pi and other harnesses, with version requirements and authentication limitations.
