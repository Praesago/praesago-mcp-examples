"""What does a postcode's area look like? python postcode_check.py "E17 7AB"

Prints three lines from the area overview: the sold price of the postcode sector (a median needs 10 sales in 12 months),
the district's sold price, and the Local Housing Allowance (the most housing benefit pays towards rent in its area).
"""
import sys

from praesago_mcp import call

postcode = sys.argv[1] if len(sys.argv) > 1 else "E17 7AB"
text = call("get_area_overview", area=postcode, response_format="detailed")
for line in text.splitlines():
    if line.startswith("Postcode sector") or "Median sold price" in line or "Local Housing Allowance" in line:
        print(line.lstrip("- "))
