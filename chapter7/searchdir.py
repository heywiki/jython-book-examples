#Packages
import search.scanner as scanner
import sys

help = """
Usage: searchdir.py directory terms...
"""

args = sys.argv

if args == None or len(args) < 2:
    print help
    sys.exit()

dir = args[1]
terms = args[2:]
scan = scanner.ScanResults.scan(dir, terms)
scan.display()
