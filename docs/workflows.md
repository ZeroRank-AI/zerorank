# ZeroRank MCP workflows

Start with our [MCP developer guide](https://docs.zerorank.ai/integrations/mcp-server) to connect an assistant. See our [MCP product page](https://zerorank.ai/platform/mcp) and [changelog](https://zerorank.ai/changelog) for workspace management and recent additions.

Your role and workspace determine which operations you can use.

## Analyze existing visibility

Call `list_workspaces`, resolve the target workspace, then read `get_workspace`, `get_brand_rankings` and `list_sources`. Use `list_source_urls` for specific pages. `list_chats` returns summaries. Call `get_chat` with a returned chat ID for the full answer and its sources. Rankings accept a lookback in days (documented default 7, maximum 90).

The current `list_sources` and `list_source_urls` definitions expose no date filter. When reporting citations, give the actual scope of the result. [Reading recent chats](https://docs.zerorank.ai/results/recent-chats) · [Understanding cited sources](https://docs.zerorank.ai/citations/sources)

| If you want to… | Use this tool |
| --- | --- |
| Compare a brand across markets, models, topics or tags | `get_brand_insights` returns a metric time series and a comparison matrix. |
| See where answers included web search, maps, shopping or ads | `get_answer_features` reads provider-reported features. Preserve unknown values in your totals. |
| Find saved source bookmarks or notes | `get_source_library` reads the workspace’s source library. |
| Open the evidence for a saved Copilot opportunity | `list_copilot_opportunities` returns saved summaries. Pass a returned ID to `get_copilot_opportunity` for the evidence and plan. |

## Manage tracking

Inspect existing prompts and model settings first. Prepare the requested prompt text, location, tags and topic. `create_prompts` accepts 1–25 entries and immediately creates active prompts and queues a first run across enabled workspace models. It has no per-call model selection. Review partial failures and duplicate entries before retrying. [How prompt tracking works](https://docs.zerorank.ai/tracking/prompts)

`update_prompt` can pause a prompt reversibly. Reactivating it queues a billable run. A separate `run_prompt` can target a subset of enabled models but does not restrict runs already queued by creation or reactivation. Inspect the returned budget data and use `list_chats` to check results asynchronously. After a timeout, check whether the run was queued before submitting it again.

## Configure models

Read `get_workspace_models` for the available models, enabled configurations and their answer-run weights. `set_workspace_models` requires owner/admin access. By default it patches only the supplied keys. Setting `replace: true` disables omitted models. An unavailable model cannot be enabled, and at least one available model must remain enabled. [AI models and country coverage](https://docs.zerorank.ai/tracking/ai-models)

## Build a prospect pitch

Agree on domain, organization, prompt budget and spending scope. `create_pitch_workspace` generates prompts and runs them once. Its prompt budget defaults to 10 and allows up to 15. It consumes monthly pitch allowance and answer-run budget per generated prompt per enabled model. Set `enableShare: false` unless sharing was requested.

Poll `get_pitch_status` every 30–60 seconds. Fetch analytics when `resultsReady` is true. `complete` means full coverage. `partial` means the settle deadline passed with missing answers, which remain missing for that run. Report partial coverage accurately. A rerun is a new billable action, refreshes the 30-day expiry and can revive an archived pitch.

## Share results

An owner or admin on an eligible plan can use `enable_dashboard_share` to share a dashboard by public link. Review the intended audience before enabling sharing.
