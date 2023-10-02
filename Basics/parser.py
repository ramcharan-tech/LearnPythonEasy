import sys
import argparse

parser=argparse.ArgumentParser(description='My First Program')
parser.add_argument('--n',type =int,help='Pass the number',dest='num')
args = parser.parse_args()

number = args.num
print("* " * number)
print(args)