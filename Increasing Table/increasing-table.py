"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
def überprüfe_anordnung(reihe1, reihe2, A, B, N):

    for i in range(N-1):
        if reihe1[i] >= reihe1[i+1] or reihe2[i] >= reihe2[i+1]:
            return False
        if reihe1[i] >= reihe2[i]:
            return False
    
    if reihe1[-1] >= reihe2[-1]:
        return False
        
    for x in A:
        if x not in reihe1:
            return False
    for x in B:
        if x not in reihe2:
            return False
            
    return True

def generiere_anordnungen(N, A, B):

    MOD = 998244353
    
    A = set(A)
    B = set(B)
    
    if len(A) > N or len(B) > N:
        return 0
        
    if A & B:
        return 0
    
    alle_zahlen = set(range(1, 2*N + 1))
    flexible_zahlen = list(alle_zahlen - A - B)
    flexible_zahlen.sort()
    
    benötigte_reihe1 = N - len(A)
    benötigte_reihe2 = N - len(B)
    
    if len(flexible_zahlen) != benötigte_reihe1 + benötigte_reihe2:
        return 0
    
    A_liste = sorted(A)
    B_liste = sorted(B)
    
    if len(A_liste) > 1 and any(A_liste[i] >= A_liste[i+1] for i in range(len(A_liste)-1)):
        return 0
    if len(B_liste) > 1 and any(B_liste[i] >= B_liste[i+1] for i in range(len(B_liste)-1)):
        return 0
    
    from itertools import combinations
    anzahl = 0
    
    for flex_reihe1_zahlen in combinations(flexible_zahlen, benötigte_reihe1):

        reihe1 = A_liste + list(flex_reihe1_zahlen)
        reihe1.sort()
        
        flex_reihe2_zahlen = [x for x in flexible_zahlen if x not in flex_reihe1_zahlen]
        reihe2 = B_liste + flex_reihe2_zahlen
        reihe2.sort()
        
        if überprüfe_anordnung(reihe1, reihe2, A, B, N):
            anzahl = (anzahl + 1) % MOD
    
    return anzahl

def hauptfunktion():

    N = int(input())

    A_eingabe = list(map(int, input().split()))
    
    B_eingabe = list(map(int, input().split()))
    B = B_eingabe[1:] 
    
    ergebnis = generiere_anordnungen(N, A, B)
    print(ergebnis)

if __name__ == "__main__":
    hauptfunktion()
