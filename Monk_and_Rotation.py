T = int(input())
while T > 0:

    V = str(input())
    N = int(V[0])
    K = int(V[-1])

    # elements of array
    A = str(input())
    # print(A)
    # new array
    B = A.split()
    # here the for loop loops throught the str to find out non white-space items to add them in the B array
    # for i in A:
    #     if i != ' ':
    #         B.append(i)

    #########################
    Last_index = N - 1  # 4
    negative_arr = []
    negative_N = -N
    for i in range(1, N+1):
        negative_arr.append(-i)
    ########################

    new_array = []
    for i in B:
        new_array.append(i)

    for i in negative_arr:
        new_array[i + K] = B[i]
    
    S = ' '
    H = S.join(new_array)

    print(H)
    T = T-1



# Correct one is here
# testCase = int(input())
# for _ in range(testCase):
#     n, k = map(int, input().split())
#     l = list(map(int, input().split()))
#     x = k % n
#     print(*(l[n-x:]+l[:n-x]))
