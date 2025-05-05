import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 기본 정렬: 첫 번째 원소 기준 정렬, 같으면 두 번째 기준
points.sort()

for x, y in points:
    print(x, y)