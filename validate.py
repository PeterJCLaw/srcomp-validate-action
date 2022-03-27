#!/usr/bin/env python3

from argparse import ArgumentParser

from sr.comp.comp import SRComp
from sr.comp.validation import validate

parser = ArgumentParser(description="SR Competition State validator")
parser.add_argument("compstate", help="Competition state git repository path")

args = parser.parse_args()

comp = SRComp(args.compstate)
error_count = validate(comp)

exit(error_count)
