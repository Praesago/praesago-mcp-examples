# Praesago MCP examples

Small, working examples for the [Praesago](https://praesago.com) MCP server: property-area data for every postcode district in England and Wales
(2,293 districts). Sold prices (including by postcode sector), private rents, asking rents and yields, Local Housing Allowance rates, crime, flood risk,
schools, deprivation, broadband, council tax, planning applications and the weekly live listings market. Every figure comes from a named official
source and carries its date. Scotland and Northern Ireland are not covered.

## Connect

Server URL: `https://praesago.com/api/mcp` (Streamable HTTP). No key is needed to start.

Claude Code:

```
claude mcp add --transport http praesago https://praesago.com/api/mcp
```

Claude (web and desktop), ChatGPT, Cursor and VS Code: https://praesago.com/docs/mcp

It is also in the official MCP Registry as `com.praesago/praesago`.

## Ask your assistant

- "Compare Walthamstow and Tottenham: prices, incomes and flood risk."
- "What do homes in the E17 7 postcode sector sell for, and what is the housing allowance there?"
- "Which districts in Wales have a median sold price under £150,000?"
- "Is the market in Leeds LS6 moving or stuck? Are sellers cutting prices?"

## Run an example

```
pip install requests
cd python
python compare.py Hackney Leeds
python cheap_welsh_districts.py 150000
python postcode_check.py "E17 7AB"
```

`postcode_check.py` prints, for one postcode: the sold price of its postcode sector, the district's sold price, and the Local Housing Allowance
for its rental area. For example:

```
Postcode sector E17 7 (part of E17): median sold price £505,000 from 89 sales in the last 12 months; -2.4% on the 12 months before.
Median sold price, all property types, last 12 months: £550,000 (699 sales; latest sale 2026-08-19), +4.2% on the 12 months before.
Local Housing Allowance (April 2026 to March 2027, Outer East London): £1,400 a month for a 2-bed home, £1,200 for a 1-bed.
```

The server answers headline facts without a key. For the full profile (about 30 sections), get an API key (setup at
https://praesago.com/docs/mcp) and set it:

```
export PRAESAGO_API_KEY=your_key      # PowerShell: $env:PRAESAGO_API_KEY = "your_key"
```

`python/praesago_mcp.py` is the whole client: one function, `call(tool, **arguments)`.

## Tools

`get_area_overview`, `get_area_context` (full profile, needs a key), `get_area_profile`, `get_market_pulse`, `compare_areas`, `screen_areas`,
`search_areas`, `search`, `fetch`, `get_usage`. Every figure in an answer carries its source year or date.

## REST API

The same data is a REST API with an OpenAPI description: https://praesago.com/docs/api (try `curl https://praesago.com/api/v1/demo`, no key needed).

## Monthly email

Monthly email for builders (what moved in the England and Wales property market, which official data was updated, one API call to try): <https://praesago.com/newsletter>

## Not covered

Scotland and Northern Ireland, forecasts, valuations of single homes, and individual listings (only weekly totals and medians).
