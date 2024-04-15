import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", type=str, required=True)
parser.add_argument("-i", "--old", type=str, required=True)
parser.add_argument("-o", "--new", type=str, required=True)

args = parser.parse_args()
with open(args.file, 'r+') as file:
    data = file.read().replace(args.old, args.new)
    file.seek(0)
    file.write(data)
    file.truncate()