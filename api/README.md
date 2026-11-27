# ZeroRank REST API for AI search analytics

For current endpoints and key permissions, start here. [Official ZeroRank API documentation](https://docs.zerorank.ai/api/overview) · [Authentication and scopes](https://docs.zerorank.ai/api/authentication) · [Download the OpenAPI specification](https://docs.zerorank.ai/api/openapi.json)

[MCP](../mcp/README.md) · [API](../api/README.md) · [Datasets](../data/README.md)

Use our REST API to read saved AI answers in your workspace and bring brand mentions and citations into your own reports. Each key belongs to one workspace. API access requires an active trial or paid plan. Free AEO endpoints may be coming soon.

## Start with your coding agent

Copy this prompt to set up a key and read your first answer. The example also works with a key you already have.

```text
Use https://github.com/ZeroRank-AI/zerorank/tree/main/api and https://docs.zerorank.ai/api/authentication to help me set a read-only ZERORANK_API_KEY locally, keep its value out of chat, verify my workspace, and show the question, engine and cited URLs from one saved answer.
```

## Get a workspace key

If you’re using Meta Muse, ask it to create a custom connector from this guide, then use its secure credential setup for a read-only key. [Muse custom connectors](https://www.meta.com/help/superintelligence/1687253048996149/)

An owner or admin of a paid workspace or active trial can open **Developer → API** in the ZeroRank sidebar and create a key. Turn **Allow write access** off for this example. Save the key in your secret manager and supply it to your process as `ZERORANK_API_KEY`. The authentication guide still shows the previous location in Workspace settings. [Authentication and key scopes](https://docs.zerorank.ai/api/authentication) · [Developer sidebar update, July 28](https://zerorank.ai/changelog)

[Open your ZeroRank workspace](https://app.zerorank.ai/?utm_source=github&utm_medium=readme&utm_campaign=zerorank-ai-api)

The base URL is `https://api.zerorank.ai/api/v1`. Send `Authorization: Bearer <your-key>` with each request. Start with `GET /workspace` to confirm the workspace name in `data.workspace.name` and the current key’s scopes in `data.apiKey.scopes` when key details are present. [Workspace reference](https://docs.zerorank.ai/api-reference/workspace/get-workspace-context)

## Read one answer

From the root of your downloaded or cloned repository, run the [Python example](examples/recent_answer.py). It uses the Python 3 standard library.

```sh
python3 api/examples/recent_answer.py
```

The script prints a JSON object with `workspace`, `id`, `question`, `aiModel`, `location`, `createdAt`, `status`, `answer`, and `sources`. The source records preserve the returned URLs and positions. To revisit a known record, add `--chat-id` followed by its UUID. You can use the ID returned by your [connected assistant](../mcp/README.md#read-one-answer) if both credentials can access the same workspace.

| Request | What it gives you |
| --- | --- |
| [`GET /workspace`](https://docs.zerorank.ai/api-reference/workspace/get-workspace-context) | The workspace associated with the key, including its name in `data.workspace.name`. |
| [`GET /chats?limit=1`](https://docs.zerorank.ai/api-reference/analytics/list-recent-chats) | A recent chat ID in `data[0].id`. If there are no records, the script prints `no_recent_chats` and stops. |
| [`GET /chats/{id}`](https://docs.zerorank.ai/api-reference/analytics/get-a-chat) | The full `data.answer`, original `data.question`, and `data.sources` for that execution. |

Use the returned status when an answer is incomplete. An empty source array means the service returned zero entries for that execution. A missing source field means coverage is unknown.

If Python reports a certificate verification failure, configure its trusted CA bundle and retry. Python installations using OpenSSL accept the path to your system or organization’s trusted bundle in `SSL_CERT_FILE`.

## Try it in Postman

1. Import the [three-request collection](examples/zerorank.postman_collection.json) into Postman Desktop.
2. Add a local Vault secret named `zerorank-api-key` and allow it for `api.zerorank.ai`. [Postman Vault](https://learning.postman.com/docs/use/postman-vault/postman-vault-secrets/)
3. Run the collection in order. The runner uses the ID returned in the second response to open the third. When sending requests individually, copy the returned ID into the final URL.

The collection stops on an empty chat history. Both examples only read existing answers.

## Two more requests to try

**Export your most-cited domains.** The source endpoint returns ranked domains with fields including `domain` and `usage`. [List top source domains](https://docs.zerorank.ai/api-reference/analytics/list-top-source-domains)

```text
Write a Python script that reads ZERORANK_API_KEY from my environment and exports my workspace’s five most-cited domains and their usage percentages to CSV.
```

**Follow one tracked question.** Replace the bracketed text with an existing prompt ID. [List recent chats by prompt](https://docs.zerorank.ai/api-reference/analytics/list-recent-chats)

```text
Use the ZeroRank API to list up to five saved answers for prompt ID [prompt ID] and show the engine, date, and source URLs for each.
```

## Build your own integration

The API includes prompts, brands, tags, topics, and analytics. Check the schema for each endpoint before choosing a field or filter. A `429` response includes a `Retry-After` interval. Creating, reactivating, or rerunning prompts can consume answer-run usage. [API overview](https://docs.zerorank.ai/api/overview) · [OpenAPI specification](https://docs.zerorank.ai/api/openapi.json) · [Workflow guidance](../mcp/workflows.md#manage-tracking)
