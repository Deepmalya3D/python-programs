import numpy as np


def identity_mat(n):
    arr = [[0]*n for _ in range(n)]
    for _ in range(n):
        arr[_][_] = 1
    return arr


def print_mat(x):
    for _ in x:
        print(_)


n = int(input("Enter The Length of Matrix: "))
model_mat = identity_mat(n)
inv_mat = identity_mat(n)
user_mat = identity_mat(n)

for _ in range(n):
    for e in range(n):
        user_mat[_][e] = float(input(f"Enter {_+1}x{e+1} term: "))

print("\nThe Following Is Your Matrix:\n")
print_mat(user_mat)
print("\n")

a = np.array(user_mat)
det = np.linalg.det(a)

if int(det) == 0:
    print("SORRY. Invalid Matrix. Determinant is Zero.")
else:
    flag = 0
    while user_mat != model_mat:
        if user_mat[flag][flag] == 0:
            for _ in range(flag, n):
                if user_mat[_][flag] != 0:
                    break
            for e in range(0, n):
                user_mat[flag][e] += user_mat[_][e]
                inv_mat[flag][e] += inv_mat[_][e]

        t = user_mat[flag][flag]
        for _ in range(0, n):
            user_mat[flag][_] = user_mat[flag][_]/t
            inv_mat[flag][_] = inv_mat[flag][_] / t

        for _ in range(0, n):
            x = user_mat[_][flag]
            for e in range(0, n):
                if _ == flag:
                    continue
                else:
                    user_mat[_][e] += - user_mat[flag][e]*x
                    inv_mat[_][e] += - inv_mat[flag][e] * x
        flag += 1

print("The Following Is Your Inverse Matrix\n")
print_mat(inv_mat)
