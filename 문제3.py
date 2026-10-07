from collections import deque

n, m = map(int, input().split())
if not (4 <= n <= 200 and 4 <= m <= 200):
    print("입력 범위를 벗어났습니다")
    exit()
graph = [list(map(int, input())) for _ in range(n)]

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

print(graph[n-1][m-1])

