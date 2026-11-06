"""A tiny client for the Praesago MCP server (Streamable HTTP, JSON-RPC). Needs only `requests`.

Without a key you get headline facts. With an API key (https://praesago.com/docs/mcp) set PRAESAGO_API_KEY to get
the full profile from get_area_context.
"""
import json
import os

import requests

URL = "https://praesago.com/api/mcp"


def call(tool: str, **arguments) -> str:
    """Call one tool and return its text answer."""
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    if os.environ.get("PRAESAGO_API_KEY"):
        headers["X-API-Key"] = os.environ["PRAESAGO_API_KEY"]
    body = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": tool, "arguments": arguments}}
    reply = requests.post(URL, headers=headers, data=json.dumps(body), timeout=60)
    reply.raise_for_status()
    result = reply.json()["result"]
    if result.get("isError"):
        raise RuntimeError(result["content"][0]["text"])
    return result["content"][0]["text"]
