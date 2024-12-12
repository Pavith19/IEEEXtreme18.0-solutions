def transformar_A_sequenz(eingaben, länge, anzahl):
    oben_einträge = []
    rechts_einträge = []
    länge2 = 2 * länge
    
    for eintrag in eingaben:
        richtung, nummer = eintrag
        
        if richtung == 'U':
            oben_einträge.append((richtung, länge + nummer))
        elif richtung == 'R':
            rechts_einträge.append((richtung, länge + (länge2 - nummer)))

    oben_einträge.sort(key=lambda x: x[1])
    rechts_einträge.sort(key=lambda x: x[1])

    sortierte_einträge = []
    gesehen = set()
    
    for eintrag in oben_einträge + rechts_einträge:
        if eintrag not in gesehen:
            gesehen.add(eintrag)
            sortierte_einträge.append(eintrag)
    
    return sortierte_einträge

def transformar_B_sequenz(eingaben, länge, anzahl):
    links_einträge = []
    oben_einträge = []
    
    for eintrag in eingaben:
        richtung, nummer = eintrag
        
        if richtung == 'L':
            links_einträge.append((richtung, nummer))
        elif richtung == 'U':
            oben_einträge.append((richtung, nummer + länge))

    links_einträge.sort(key=lambda x: x[1])
    oben_einträge.sort(key=lambda x: x[1])

    sortierte_einträge = []
    gesehen = set()
    
    for eintrag in links_einträge + oben_einträge:
        if eintrag not in gesehen:
            gesehen.add(eintrag)
            sortierte_einträge.append(eintrag)
    
    return sortierte_einträge

def zählen_formen(länge, A, B, anzahl_A, anzahl_B):
    A = transformar_A_sequenz(A, länge, anzahl_A)
    B = transformar_B_sequenz(B, länge, anzahl_B)

    vorherige_intersektionen = 0
    formen = 1 + len(B)
    for strahl in A:
        intersektionen = vorherige_intersektionen
        abstandspunkt_A = strahl[1]
        for sek_strahl in B[vorherige_intersektionen:]:
            abstandspunkt_B = sek_strahl[1]
            if abstandspunkt_A > abstandspunkt_B:
                intersektionen += 1
            else:
                vorherige_intersektionen = intersektionen
                break
        formen += 1 + intersektionen
    return formen

länge, anzahl_A, anzahl_B = [int(_) for _ in input().split()]
A = []
B = []

for _ in range(anzahl_A):
    x, y = input().split()
    A.append([x, int(y)])

for _ in range(anzahl_B):
    x, y = input().split()
    B.append([x, int(y)])

print(zählen_formen(länge, A, B, anzahl_A, anzahl_B))
