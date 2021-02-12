def main():

    T = int(input())
    for _ in range(T):
        N, K = tuple([int(i) for i in input().split()])
        array = [0 for i in range(N)]
        
        for i, j in enumerate([i for i in input().split()]):
            array [(i+K) % N] = j
        
        print(' '.join(array))

main()