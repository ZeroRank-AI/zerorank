# Help desk software across five markets

**Give this prompt to your agent.**

```text
Read https://github.com/ZeroRank-AI/zerorank/tree/main/data/help-desk-software
Help me find patterns in which products the engines mention across markets. Build a chart of the clearest pattern, label it with the study dates and answer counts, and show me one question that illustrates it.
```

We asked practical questions about buying help desk software, from combining WhatsApp and email support to choosing where customer conversations are stored. This release lets you compare product mentions and source domains across the same questions in two AI search experiences.

## Download the data

| File | Contents |
| --- | --- |
| [questions.jsonl](questions.jsonl) | One research question per line, with a release-specific ID. |
| [answers.jsonl](answers.jsonl) | One observation per question, engine and market, with tracked product mentions, a short answer excerpt and reviewed source domains. |
| [metadata.json](metadata.json) | Release version, date definitions, engine and market coverage, field descriptions and reuse terms. |

The JSONL files are UTF-8 text with one JSON object on each line. Join the files on `question_id`. You can analyze a local copy independently of the ZeroRank API.

## Study scope

| Study detail | Coverage |
| --- | --- |
| Answer record dates | October 29–30, 2026 (UTC). Collection finished on November 2, 2026. |
| Dataset release | Version 1.1, November 25, 2026 |
| Engines | Standard ChatGPT and Google AI Overviews |
| Requested markets | United States, United Kingdom, Canada, Australia and India |
| Question language | English, using the same wording in all five markets. Some answers were returned in Hindi. |
| Comparison | 34 distinct questions × 2 engines × 5 markets = 340 answers. Each engine has 170 answers, with 34 per market. |

Both engines answered the same 34 questions in all five markets. Each record’s date comes from the provider’s timestamp, and its market is the country setting we requested.

## How to read the results

Count a tracked product once per answer, even when the text names it several times. We measured mentions in the full answer and included one short excerpt per record. An excerpt can illustrate only part of an answer. A mention can occur in a recommendation, a comparison or a passing reference. The twelve tracked products cover a defined comparison set. Other products can appear in the original answers.

For a quick check, count Zendesk mentions separately for each engine. You should find **101 of 170 ChatGPT answers** and **101 of 170 Google AI Overviews answers**. For a country comparison, use the same 34 questions in each country and keep the engine fixed.

The optional `source_domains` list contains reviewed public domains for the whole answer. An empty list means this release shares no domain for that answer. Use it to study where the published domains appear. It cannot tell you how often an engine supplied citations overall.

## Attribution

Credit line for a chart, report or notebook:

> Source: ZeroRank, [Help desk software across five markets](https://github.com/ZeroRank-AI/zerorank/tree/main/data/help-desk-software), v1.1. Answers dated October 29–30, 2026 (UTC). [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

If you adapted the study, add a brief description of your changes. When quoting an answer, name the engine shown on that record. We report what the engines returned and have no affiliation with or control over the businesses mentioned. [Scope of the study license](../../LICENSE.md)

If a record concerns you, include its question or answer ID when you [request a correction](../../CONTRIBUTING.md#correct-a-record) or [ask us to remove it](../../CONTRIBUTING.md#request-removal-from-a-dataset).
