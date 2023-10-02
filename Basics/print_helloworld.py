import sys
import optparse

parser=optparse.OptionParser()
parser.add_option('-n','--num',help='Pass the number')
(opts,args) = parser.parse_args()

number = int(opts.num)
print("* " * number)
print(opts)
print(args)