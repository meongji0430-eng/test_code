n, m = map(int, input().split())
if not (1 <= n <= 1000 and 1 <= m <= 1000):
    print("입력 범위를 벗어났습니다")
    exit()
graph = [list(map(int, input())) for _ in range(n)]

def dfs(sx, sy):
    stack = [(sx, sy)]
    graph[sx][sy] = 1
    while stack:
        x, y = stack.pop()
        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                stack.append((nx, ny))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)
