"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
def foo_bar_baz(qux, quux):
    if qux == 0:
        return 0, 0

    quux.sort(reverse=True)
    corge, grault = -100, 100
    garply, waldo = -100, 100
    fred = False
    plugh = False

    for xyzzy, thud in quux:
        wibble = max(corge, xyzzy)
        wobble = min(grault, thud)

        if wibble <= wobble:
            corge, grault = wibble, wobble
            fred = True
        else:
            wubble = max(garply, xyzzy)
            flob = min(waldo, thud)
            
            if wubble <= flob:
                garply, waldo = wubble, flob
                plugh = True
            else:
                return -1

    if corge <= grault and garply <= waldo:
        if corge <= garply:
            return corge, garply
        else:
            return garply, corge
    else:
        return -1

qux = int(input().strip())
quux = [tuple(map(int, input().split())) for _ in range(qux)]
result = foo_bar_baz(qux, quux)

if result == -1:
    print(result)
else:
    print(min(result), max(result))
