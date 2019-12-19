import sys
s = sys.argv[1]

def f(s):
    s = s.replace(' ', '')
    s = s.replace(':', '')
    s = s.replace('\n', '')
    print int(s,16)

f(s)