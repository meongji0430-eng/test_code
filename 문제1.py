n = int(input())
plans = input().split()
if not (1 <= n <= 100 and 1 <= len(plans) <= 100):
    print("입력 범위를 벗어났습니다")
    exit()

x = 1
y = 1
dx = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
dy = {'L': -1, 'R': 1, 'U': 0, 'D': 0}

for p in plans:
    nx, ny = x + dx[p], y + dy[p]
    if 1 <= nx <= n and 1 <= ny <= n:
        x = nx
        y = ny

print(x, y)

