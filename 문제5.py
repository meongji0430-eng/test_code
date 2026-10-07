n, m = map(int, input().split())
cakes = list(map(int, input().split()))
if not (1 <= n <= 1000000 and 1 <= m <= 2000000000) or not all(0 <= c <= 1000000000 for c in cakes):
    print("입력 범위를 벗어났습니다")
    exit()

start, end = 0, max(cakes)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = sum(c - mid for c in cakes if c > mid)
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

