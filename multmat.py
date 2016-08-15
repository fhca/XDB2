A = [[2,3,4],[6,3,7]]
B = [[1,5,2], [6,3,7], [0,4,2]]

C = [[0,0,0],[0,0,0]]

for i in range(len(A)):
  for j in range(len(A[0])):
    for k in range(len(B)):
      C[i][j] += A[i][k]*B[k][j]

print(C)
