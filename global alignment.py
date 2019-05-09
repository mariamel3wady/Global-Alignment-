##m is responsible for column length (length of first string )
##n is responsible for row length (length of second string )
##We'll iterate row by row

def ga(X, Y):
    m=len(X)
    n=len(Y)
    L = [[0 for x in range(m+1)] for y in range(n+1)] 
    for i in range (n+1):
        L[i][0]=-i
    for j in range (m+1):
        L[0][j] =-j
    for i in range(1,n+1,1):
        for j in range(1,m+1,1):
            if X[j-1] == Y[i-1]:
                score = 1
            else :
                score =-1
            L[i][j] = max(L[i-1][j]-1, L[i][j-1]-1,L[i-1][j-1]+score)
    print(L[n][m])

    GAFirst =""
    GASecond=""
    GAMatch=""
    i = n
    j = m
    while i > 0 and j > 0:
        up = L[i-1][j]-1
        left=L[i][j-1]-1
        if  X[j-1]==Y[i-1]:
            score=1
        else :
            score=-1
        diagonal = L[i-1][j-1]+score
        if L[i][j]==diagonal:
            GAFirst+=X[j-1]
            GASecond+=Y[i-1]
            if score==1:
                GAMatch+="|"
            else:
                GAMatch+=" "
            i-=1
            j-=1
        elif L[i][j] == up:
            GAFirst+="-"
            GAMatch+=" "
            GASecond+=Y[i-1]
            i-=1
        else:
            GAFirst+=X[j-1]
            GASecond+="-"
            GAMatch+=" "
            j-=1

    while (i>0):
        GAFirst+="-"
        GASecond+=Y[i-1]
        GAMatch+=" "
        i-=1
    while(j>0):
        GAFirst+=X[j-1]
        GASecond+="-"
        GAMatch+=" "
        j-=1
        
    GAFirst=GAFirst[::-1]
    GAMatch=GAMatch[::-1]
    GASecond=GASecond[::-1]
    
    print (GAFirst)
    print(GAMatch)
    print(GASecond)
 
# Driver program
X = "ACGC"
Y = "GACTAC"
ga(X, Y)
