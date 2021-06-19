T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    d, q = 0, list(range(1, n + 1))
    while n > 2:
        q.pop(d)
        n -= 1
        d = (d + k - 1) % n
    print(q[0], q[1])