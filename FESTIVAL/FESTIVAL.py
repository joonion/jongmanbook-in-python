def solve(N, L, cost):
    acc = cost[:]
    for i in range(1, N):
        acc[i] += acc[i - 1]
    minavg = 0xFFFFFFFF
    for d in range(L, N + 1):
        for e in range(d - 1, N):
            total = acc[e] - acc[e - d] if e > d else acc[e]
            if total / d < minavg:
                minavg = total / d
    return minavg

T = int(input())
for _ in range(T):
    N, L = map(int, input().split())
    cost = list(map(int, input().split()))
    print('%.8f' % solve(N, L, cost))
