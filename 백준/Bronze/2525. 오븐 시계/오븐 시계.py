A, B = map(int, input().split())
C = int(input())

total_minutes = A * 60 + B + C

new_hour = (total_minutes // 60) % 24
new_minute = total_minutes % 60

print(new_hour, new_minute)