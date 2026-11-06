# Praesago MCP examples

Small, working examples for the [Praesago](https://praesago.com) MCP server: UK property area data (sold prices, rents, crime, flood risk, live listings) for every postcode district in England and Wales.

Server URL: `https://praesago.com/api/mcp` (Streamable HTTP). Setup for Claude, ChatGPT, Cursor and VS Code: https://praesago.com/docs/mcp

It is also in the official MCP Registry as `com.praesago/praesago`.

## Run an example

```
pip install requests
cd python
python compare.py Hackney Leeds
python cheap_welsh_districts.py 150000
```

The server works without a key for headline facts. For the full profile, get an API key (setup at https://praesago.com/docs/mcp) and set it:

```
export PRAESAGO_API_KEY=your_key      # PowerShell: $env:PRAESAGO_API_KEY = "your_key"
```

`python/praesago_mcp.py` is the whole client: one function, `call(tool, **arguments)`.

## Tools

`get_area_overview`, `get_area_context` (full profile, needs a key), `get_area_profile`, `get_market_pulse`, `compare_areas`, `screen_areas`, `search_areas`, `search`, `fetch`. Every figure in an answer carries its source year or date.

## Not covered

Scotland and Northern Ireland, forecasts, and individual listings (only weekly totals and medians).
