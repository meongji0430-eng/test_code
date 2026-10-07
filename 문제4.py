n, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
if not (1 <= n <= 100000 and 0 <= k <= n) or not all(1 <= v < 10000000 for v in a + b):
    print("입력 범위를 벗어났습니다")
    exit()

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

