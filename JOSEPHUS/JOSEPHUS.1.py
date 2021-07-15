def solve(N, K):
    queue = [i for i in range(1, N + 1)]
    # print(queue)
    while len(queue) > 2:
        for k in range(1, K + 1):
            target = queue.pop(0)
            if k != K:
                queue.append(target)
            # print(queue)
    return queue[0], queue[1]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    one, two = solve(N, K)
    if (one > two):
        one, two = two, one
    print(one, two)
