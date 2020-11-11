# imports
from argparse import ArgumentParser
from importPuzzles import importPuzzlesFromFile
from heuristics import h0
from astar import astar

# global variables
filePath = "samplePuzzles.txt"

# argument parser with file argument
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
args = parser.parse_args()
if args.filename is not None:
    filePath = args.filename

# import puzzles
puzzles = importPuzzlesFromFile(filePath)

print(puzzles)

astar(puzzles[4], 2, 4)
