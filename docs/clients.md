# Install ZeroRank in your AI client

Connect your assistant to `https://api.zerorank.ai/mcp` using Streamable HTTP and sign in to ZeroRank in your browser. For account and workspace setup, start with our [ZeroRank MCP documentation](https://docs.zerorank.ai/integrations/mcp-server). After connecting, [read one saved answer](../mcp/README.md#read-one-answer).

Choose your client below for its setup instructions. Custom connector availability depends on your client version, plan and organization settings.

## Client coverage

For Grok Bot, Claude, Codex, Pi and Meta Muse, see our [assistant-specific connector routes](../mcp/README.md#connector-setup-by-assistant).

| Client | Fastest documented route | Primary documentation |
| --- | --- | --- |
| [Cursor](#cursor) | Install link | [Docs](https://cursor.com/docs/mcp/install-links) |
| [VS Code / Insiders](#vscode) | Command Palette → MCP: Add Server | [Docs](https://code.visualstudio.com/docs/agent-customization/mcp-servers) |
| [Codex CLI / IDE / desktop](#codex) | CLI or MCP settings | [Docs](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) |
| [ChatGPT](#chatgpt) | Custom MCP/plugin UI | [Docs](https://developers.openai.com/api/docs/guides/custom-mcp-server) |
| [Claude Code](#claude-code) | CLI, then /mcp | [Docs](https://code.claude.com/docs/en/mcp) |
| [Claude web / desktop](#claude) | Custom connector UI | [Docs](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) |
| [Gemini CLI](#gemini) | CLI, then /mcp auth | [Docs](https://geminicli.com/docs/tools/mcp-server/) |
| [Pi 0.99+](#pi) | Native CLI, then login | [Docs](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/mcp.md) |
| [OpenCode](#opencode) | CLI, then browser authorization | [Docs](https://opencode.ai/docs/mcp-servers/) |
| [GitHub Copilot CLI](#copilot) | CLI, then /mcp auth | [Docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers) |
| [Zed](#zed) | Remote-server UI or configuration | [Docs](https://zed.dev/docs/ai/mcp) |
| [Antigravity](#antigravity) | MCP configuration and OAuth UI | [Docs](https://antigravity.google/docs/mcp) |
| [Kiro](#kiro) | MCP configuration and browser OAuth | [Docs](https://kiro.dev/docs/mcp/configuration/) |
| [Devin Local / CLI](#devin) | MCP configuration and browser OAuth | [Docs](https://docs.devin.ai/desktop/devin-local/customizations) |
| [Cline](#cline) | Remote-server UI or CLI with OAuth | [Docs](https://docs.cline.bot/mcp/mcp-overview) |
| [Continue](#continue) | Remote YAML configuration | [Docs](https://docs.continue.dev/customize/deep-dives/mcp) |
| [Goose](#goose) | Custom extension UI or configure wizard | [Docs](https://github.com/aaif-goose/goose/blob/main/documentation/docs/getting-started/using-extensions.md) |
| [Kilo Code](#kilo) | Remote configuration and OAuth | [Docs](https://kilo.ai/docs/automate/mcp/using-in-kilo-code) |
| [Grok Build](#grok) | CLI and automatic OAuth | [Docs](https://docs.x.ai/build/features/mcp-servers) |
| [Grok web](#grok-web) | Custom connector UI | [Docs](https://docs.x.ai/grok/connectors) |
| [Grok Bot](#grok-bot) | Desktop custom connector | [Docs](https://docs.x.ai/grok-bot/computer-and-apps) |

## cursor

Use the [Cursor install link](https://cursor.com/en/install-mcp?name=zerorank&config=eyJ1cmwiOiJodHRwczovL2FwaS56ZXJvcmFuay5haS9tY3AifQ%3D%3D), review the server, then complete OAuth. See [configuration](../examples/cursor.mcp.json).

## vscode

In a VS Code or Insiders chat with Copilot selected, open the Command Palette and run `MCP: Add Server`. Choose **HTTP**, paste the ZeroRank endpoint, and name the server `zerorank`. Choose **Global → Copilot Global** for your own setup or choose the workspace destination if you want to share the configuration. Review the prompts and sign in to ZeroRank.

To configure the current Copilot harness by hand, merge our [example](../examples/vscode.mcp.json) into your workspace-root `.mcp.json` or Copilot user `mcp-config.json`. It makes the three tools for the first read available. Existing Local harness configurations have a different format. [VS Code configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration)

## codex

Add the hosted server from your terminal.

```sh
codex mcp add zerorank --url https://api.zerorank.ai/mcp
```

Complete browser sign-in when prompted. To start it manually, run `codex mcp login zerorank`. Check the connection with `codex mcp list`. Codex shares the server configuration between its CLI, IDE extension and desktop app. If you edit your configuration directly, merge the [TOML example](../examples/codex.config.toml) into `~/.codex/config.toml`.

## chatgpt

In ChatGPT on the web, open **Plugins**, use **+** to add a custom MCP server, and enter the ZeroRank endpoint. Choose OAuth, review the requested access and sign in. Your workspace administrator may need to enable custom servers. [ChatGPT custom MCP guide](https://developers.openai.com/api/docs/guides/custom-mcp-server)

## claude-code

```sh
claude mcp add --transport http --scope user zerorank https://api.zerorank.ai/mcp
```

In Claude Code, open `/mcp` and authenticate ZeroRank. [Project configuration example](../examples/claude.mcp.json) can be merged into `.mcp.json` instead of using user scope.

## claude

On Claude Pro or Max, open **Customize → Connectors → + Add → Add custom connector** and enter the ZeroRank name and endpoint. Review the authentication setup and complete browser sign-in. For Team or Enterprise, an owner first adds the server in **Organization settings → Connectors**. Members can then select **Connect** for ZeroRank.

## gemini

```sh
gemini mcp add --transport http --scope user zerorank https://api.zerorank.ai/mcp
```

Inside Gemini CLI run `/mcp auth zerorank`. The [settings example](../examples/gemini.mcp.json) uses Gemini CLI’s `httpUrl` field.

## pi

Use a Pi release with native MCP support (0.99 or later).

```sh
pi mcp add zerorank --url https://api.zerorank.ai/mcp
pi mcp login zerorank
pi mcp list
```

Open `/mcp` to inspect the connection in a Pi session. If you configure it by hand, merge the [example](../examples/pi.mcp.json) into `~/.pi/agent/mcp.json` or a trusted project's `.pi/mcp.json`.

## opencode

In OpenCode v2, run the following in the project where you want to use ZeroRank.

```sh
opencode mcp add zerorank --url https://api.zerorank.ai/mcp
opencode mcp auth zerorank
```

You can also open `/mcps`, select ZeroRank and sign in. The [v2 configuration example](../examples/opencode.mcp.json) places the server under `mcp.servers`.

## copilot

```sh
copilot mcp add --transport http zerorank https://api.zerorank.ai/mcp
```

In the interactive CLI, use `/mcp auth zerorank`. To expose just the tools for your first read, merge the [configuration example](../examples/copilot.mcp.json) into `~/.copilot/mcp-config.json`. [Copilot CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)

## zed

Open **Settings → AI → MCP Servers → Add Server → Add Remote Server** and enter the endpoint. Leave static authorization headers unset so Zed can use OAuth. Alternatively merge [this example](../examples/zed.mcp.json) into settings.

## antigravity

Open the MCP manager with `/mcp`, or edit the user file `~/.gemini/config/mcp_config.json` or project file `.agents/mcp_config.json`. Merge the [example](../examples/antigravity.mcp.json), which uses `serverUrl`, and complete the browser authorization flow.

## kiro

Merge [this example](../examples/kiro.mcp.json) into the MCP configuration opened from Kiro. Connect and finish browser OAuth. No preconfigured client secret is included. Consult the linked Kiro documentation for your IDE/CLI configuration location.

## cascade

For existing Windsurf Cascade installations, the [legacy configuration example](../examples/cascade.mcp.json) uses `serverUrl`. The former Cascade documentation now directs readers to [Devin Local](#devin).

## devin

In Devin Desktop, open **Agents → Customize → MCPs** and select **This computer**. For personal use, merge our [Devin configuration](../examples/devin.mcp.json) into `~/.config/devin/mcp_config.json`. For a shared project, use `.devin/mcp_config.json`. Refresh the list and follow the browser authorization prompt, or run `devin mcp login zerorank` in Devin CLI. [Devin configuration reference](https://docs.devin.ai/cli/extensibility/mcp/configuration)

## cline

In the Cline CLI, run the command below to open the setup wizard with the URL filled in. In the IDE, open **MCP Servers → Configure → Configure MCP Servers** and merge the [Cline example](../examples/cline.mcp.json). It leaves automatic approvals empty.

```sh
cline mcp add zerorank https://api.zerorank.ai/mcp --transport http
```

In `cline mcp`, select **Authorize OAuth** for ZeroRank to start browser sign-in.

## continue

Continue documents `streamable-http` servers in YAML under `.continue/mcpServers/`. See its setup guide for the transport and the authentication options available in your client.

## goose

Run `goose configure`, select Add Extension and choose a remote Streamable HTTP extension. Supply ZeroRank and `https://api.zerorank.ai/mcp`. Desktop also offers Settings → Extensions → Add custom extension. Goose documents OAuth for remote extensions.

## kilo

In the Kilo extension, open the MCP server settings and add a remote HTTP server. For a file-based setup, merge [our example](../examples/kilo.mcp.json) into `~/.config/kilo/kilo.jsonc` for personal use or `.kilo/kilo.jsonc` in your project. Kilo also accepts `.json` files. Connect to the server and complete browser OAuth.

## grok

```sh
grok mcp add --transport http zerorank https://api.zerorank.ai/mcp
```

Grok Build starts OAuth when required. Use `/mcps` for server management and `grok mcp doctor zerorank` for connection diagnostics.

## grok-web

Open [Grok connectors](https://grok.com/connectors), choose New Connector → Custom, enter the ZeroRank endpoint and authenticate. On Grok Business or Enterprise, an admin must provision the connector before organization members can use it.

## grok-bot

In Grok Bot desktop, open **Connect apps → Add a custom connector**. Enter `ZeroRank`, choose **Remote HTTPS**, paste the MCP endpoint in **Server URL**, and select **Add plugin**. Follow the sign-in prompt if offered. A team’s MCP policy can block a custom server. [Grok Bot connector guide](https://docs.x.ai/grok-bot/computer-and-apps)
