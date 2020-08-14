# Inexact(String) Matching / ECS122B 8/13

"""
- Measuring the difference/distance between two strings
- Want to find optimal, global (aligning entirety of both strings) alignment
- Incur cost: Align mismatching characters, fail to align characters (No cross alignments allowed)

- Optimal alignment: how to minimize the cosst (cost of mismatches or gaps etc)
- Focus on how to transform one string into another string through INSERT, REMOVE, REPLACE character

- Edit distance: minimum number of edit operations -- insertions, deletion, substituion needed to transform the first string into second string


D(i, j) is edit distance between two strings S1[1...i] - size of N, and S2[1...j] - size of M => Final Answer D(N, M)

Recurrence
- when i>0 j>0, D(i, j) = min(D(i-1,j) + 1 removing the gap, D(i, j-1) + 1 inserting the char cause there is gap, D(i-1, j-1) + t(i,j) substitution)
- t(i, j) = 1 if S1[i] != S2[j]; otherwise, t(i, j) = 0

Base condition: D(i,0) = i matching all i characters with nothing cause deleting all the i, 1Xi  , D(0, j) = j inserting all the  j characters, jX1

ex)
S1
n 4 | 4 3 3 4 4
a 3 | 3 3 2 3 3
e 2 | 2 2 2 3 2
m 1 | 1 1 2 2 3
  0 | 0 1 2 3 4
    ㅡ ㅡ ㅡ ㅡ ㅡ
      0 1 2 3 4
        n a m e S2
              
D(1,1) = min(D(0,1) + 1, D(1,0) + 1, D(0,0) + 1 = min(2,2,1) = 1 - align m with n ...
Optimal Alignment: D(4,4) = min(D(3,4) + 1 = 4, D(4,3) + 1 = 4, D(3,3) + t(4,4) = 5) = 4 => 2 multiple possible solutions
"""

# Topdown is also possible but arguably inefficient than the bottomup
def bottom_up(S1, S2):
    D = [[0 for i in range(len(S2))] for j in range(len(S1))] # 0 instead of empty?
    D[0][0] = 1 #
    print(D)

    for i in range(1, len(S2)):
        D[i][0] = i + 1 #
    
    for j in range(1, len(S1)):
        D[0][j] = j + 1 #
    print(D)

    for i in range(1, len(S1)):
        for j in range(1, len(S2)):
            if S1[i] != S2[j]:
                t = 1
            else:
                t = 0
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + t)
    print(D)
    return D[len(S1)-1][len(S2)-1]

S1 = "mean"
S2 = "name"
print("Difference between \"" + S1 + "\" and \"" + S2 + "\": "+ str(bottom_up(S1, S2)))

"""
Worst-case time complexity: theta(nm) / space complexity: theta(nm)

Generalization: Operation-Weight Edit Distance Problem
- additional parameters d, r, e
- d: cost of insertion/deletion, r: cost of substitution/mimatch, e: cost of match
- usually d, r = 1, e = 0

-> t(i, j) = r if  S1[i] != S2[j], otherwise, t(i, j) = e
-> D[i,0] = i * d, D[0,j] = j * d
"""