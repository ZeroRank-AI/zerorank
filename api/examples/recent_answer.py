"""Read one existing answer and its returned sources from a ZeroRank workspace."""

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from uuid import UUID


BASE_URL = "https://api.zerorank.ai/api/v1"


def get(path, key):
    request = Request(BASE_URL + path, headers={
        "Accept": "application/json",
        "User-Agent": "ZeroRankAI-WorkspaceReader/1.0 (+https://zerorank.ai)",
    })
    request.add_unredirected_header("Authorization", f"Bearer {key}")
    try:
        with urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except HTTPError as error:
        try:
            body = json.load(error)
        except (ValueError, UnicodeError):
            body = {}
        message = body.get("message", error.reason) if isinstance(body, dict) else error.reason
        code = body.get("code") if isinstance(body, dict) else None
        detail = f"HTTP {error.code}: {message}"
        if code:
            detail += f" ({code})"
        retry = error.headers.get("Retry-After")
        if error.code == 429 and retry:
            detail += f". Retry-After: {retry}"
        raise SystemExit(detail) from None
    except (URLError, TimeoutError) as error:
        raise SystemExit(f"Could not reach the ZeroRank API: {error}") from None
    except ValueError:
        raise SystemExit("The API returned an unreadable JSON response.") from None

    if not isinstance(payload, dict) or payload.get("success") is not True or "data" not in payload:
        message = payload.get("message") if isinstance(payload, dict) else None
        raise SystemExit(message or "The API returned an unexpected response.")
    return payload["data"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chat-id", type=UUID, help="Read a specific chat UUID from this workspace.")
    args = parser.parse_args()
    key = os.environ.get("ZERORANK_API_KEY")
    if not key:
        raise SystemExit("Set ZERORANK_API_KEY to a read-scoped key from the intended workspace.")

    workspace = get("/workspace", key)["workspace"]["name"]
    chat_id = args.chat_id
    if chat_id is None:
        summaries = get("/chats?limit=1", key)
        if not summaries:
            print(json.dumps({"workspace": workspace, "result": "no_recent_chats"}, ensure_ascii=False))
            return
        chat_id = UUID(summaries[0]["id"])

    chat = get(f"/chats/{chat_id}", key)
    output = {"workspace": workspace}
    for name in ("id", "question", "aiModel", "location", "createdAt", "status", "answer", "sources"):
        output[name] = chat.get(name)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
