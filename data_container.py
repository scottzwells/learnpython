def test(x,y,z,kk,j):
    n=kk(x,y)
    print(n)
    return x,y,z,j

def hel(x,y):
    return x+y
a=1
b=2
c=3
test(a,b,c,lambda x,y:x+y,c)