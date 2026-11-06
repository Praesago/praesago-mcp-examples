"""List Welsh postcode districts with a median sold price under a limit, then print the headline facts for the cheapest one."""
import re
import sys

from praesago_mcp import call

limit = int(sys.argv[1]) if len(sys.argv) > 1 else 150_000
print(call("screen_areas", region="Wales", max_price=limit))
first = re.search(r"\b([A-Z]{1,2}\d[A-Z\d]?)\b", call("screen_areas", region="Wales", max_price=limit))
if first:
    print()
    print(call("get_area_overview", area=first.group(1)))
