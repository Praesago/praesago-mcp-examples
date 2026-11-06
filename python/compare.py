"""Compare two areas: python compare.py Hackney Leeds"""
import sys

from praesago_mcp import call

a, b = (sys.argv[1:3] + ["Hackney", "Leeds"])[:2]
print(call("compare_areas", area_a=a, area_b=b))
