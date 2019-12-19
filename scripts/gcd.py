def gcd(a,b):
    if a < b:
        a,b = b,a
    a,b = b,a%b
    if b == 0:
        return a
    return gcd(a,b)
    
if __name__ == "__main__":

    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    
    r = gcd(a,b)
    print(r)
