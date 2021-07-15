def solve(N, K):
    queue = [i for i in range(1, N + 1)]
    print(queue)
    k = 1
    while len(queue) > 2:
        queue.pop(k - 1)
        k += K - 1
        if k >= len(queue):
            k = k - len(queue)
        print(queue)
    return queue[0], queue[1]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    one, two = solve(N, K)
    if (one > two):
        one, two = two, one
    print(one, two)
