# ZeroRank MCP for AI visibility tracking

For current connection instructions, start here. [Official ZeroRank MCP setup guide](https://docs.zerorank.ai/integrations/mcp-server) · [ZeroRank documentation index for agents](https://docs.zerorank.ai/llms.txt)

[MCP](../mcp/README.md) · [API](../api/README.md) · [Datasets](../data/README.md)

Connect an AI assistant to your ZeroRank workspace with our hosted Model Context Protocol (MCP) server. Investigate brand mentions, compare competitors and open the cited sources behind a saved AI answer.

The server can list workspaces you can access and supports changes your permissions allow. Select the intended workspace before approving a change. [Product changelog](https://zerorank.ai/changelog) · [MCP tool reference](tools.md)

## Start with your assistant

Copy this prompt into the assistant you want to connect. Complete the sign-in in your browser and choose your workspace. For in-app setup instructions and the server URL, open **Developer → MCP** in the ZeroRank sidebar. [Our MCP website](https://zerorank.ai/platform/mcp)

```text
Use https://github.com/ZeroRank-AI/zerorank/tree/main/mcp and https://docs.zerorank.ai/integrations/mcp-server to connect this assistant to https://api.zerorank.ai/mcp, help me sign in if needed, and show one saved answer with its citations from the workspace I choose.
```

## Connector setup by assistant

| Assistant | Setup route |
| --- | --- |
| Grok Bot | In the desktop app, open **Connect apps → Add a custom connector**. Choose **Remote HTTPS**, enter `https://api.zerorank.ai/mcp`, save it and complete sign-in when prompted. [Grok Bot connector guide](https://docs.x.ai/grok-bot/computer-and-apps) |
| Claude | Add `https://api.zerorank.ai/mcp` as a custom connector and complete browser sign-in. [Claude setup](clients.md#claude) |
| Codex | Add the server URL to your MCP settings, then sign in to ZeroRank. [Codex setup](clients.md#codex) |
| Pi | Register the remote server with `pi mcp add` and sign in with `pi mcp login zerorank`. [Pi setup and commands](clients.md#pi) |
| Meta Muse | Ask Muse to create a custom connector using our [REST API guide](../api/README.md). Meta documents this personal setup and separately accepts API or MCP integrations through its connector platform. [Muse custom connectors](https://www.meta.com/help/superintelligence/1687253048996149/) · [Muse connector platform](https://platform.muse.ai/docs) |

For additional clients and version requirements, see the [full MCP client guide](clients.md).

## What to ask first

**Read a buyer’s exact question.** [How recent chats work](https://docs.zerorank.ai/results/recent-chats)

```text
In my ZeroRank workspace, open one recent saved answer and show the buyer’s exact question, the engine, and the links it cited.
```

**Find out which websites get cited.** [How we group sources](https://docs.zerorank.ai/citations/sources)

```text
Which five domains are cited most often in my ZeroRank workspace, and what usage percentage does ZeroRank report for each?
```

**Find an answer where a competitor appeared.** Replace the two names with the brands you want to compare. [Tracking brands and competitors](https://docs.zerorank.ai/tracking/brands-and-competitors)

```text
Review my 20 most recent saved answers for mentions of [competitor] without [my brand], quote one matching answer if available, and tell me how many you checked.
```

Current workspace access requires an active trial or a paid plan. Free AEO endpoints may be coming soon. You can explore our [help desk dataset](../data/help-desk-software/README.md) without a ZeroRank account. [Open your ZeroRank workspace](https://app.zerorank.ai/?utm_source=github&utm_medium=readme&utm_campaign=zerorank-ai-mcp)

## Connect your assistant

**[Install in Cursor](https://cursor.com/en/install-mcp?name=zerorank&config=eyJ1cmwiOiJodHRwczovL2FwaS56ZXJvcmFuay5haS9tY3AifQ%3D%3D)** or follow the instructions for [Codex, Claude, ChatGPT and other clients](clients.md). Review the server configuration and sign in to ZeroRank in your browser.

| Setting | Value |
| --- | --- |
| Server URL | `https://api.zerorank.ai/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth with your ZeroRank account |

## Read one answer

The saved-answer request above uses three read operations. The chat ID lets you reopen the same record later.

| Step | Tool | Result |
| --- | --- | --- |
| Find the workspace | `list_workspaces` | Match the name to a returned workspace ID. Ask which one to use if several match. |
| Find a saved answer | `list_chats` with that `workspaceId` and `limit: 1` | A recent chat summary and its `id`. An empty list means there is no recent record to open. |
| Open the evidence | `get_chat` with the same `workspaceId` and returned `id` | The question, answer, engine, date, status, and available sources. |

Keep the returned status with unfinished answers. An empty source list means that execution returned zero source entries. A missing list means source coverage is unknown.

For work that creates tracked prompts or starts new runs, first inspect the workspace's enabled engines and answer-run allowance. [Tracking workflows](workflows.md)

## Connection problems

- **A sign-in request or HTTP 401** means the client needs to complete OAuth. Reopen its authentication flow.
- **An access error after sign-in** can come from the subscription, your role, or the workspace selected. Check all three.
- **A tool is missing**. Refresh the client's tool list or start a fresh session. Check the signed-in client's tool names and input fields against the [tool reference](tools.md).

To open the same chat from your code using a workspace key, use the [REST API guide](../api/README.md#read-one-answer).
