def f( a, b, c ):
    return ( a and (not b) ) or c

def g( a, b, c ):
    return (not a) or (not b) or (not c)

def h( a, b, c ):
    return a or not b

def main():
    print( "  a  b  c  |  f  g  h" )
    for a in [ 0, 1 ]:
        for b in [ 0, 1 ]:
            for c in [ 0, 1 ]:
                print( "%3d%3d%3d  |%3d%3d%3d" % 
                      ( a, b, c,
                        f( a, b, c ),
                        g( a, b, c ),
                        h( a, b, c ) ) )
main()
