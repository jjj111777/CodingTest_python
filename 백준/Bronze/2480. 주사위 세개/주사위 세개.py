# 세 개의 주사위 값 입력받기
a, b, c = map(int, input().split())

# 같은 눈이 3개인 경우
if a == b == c:
    prize = 10000 + a * 1000
# 같은 눈이 2개만 있는 경우
elif a == b or a == c:
    prize = 1000 + a * 100
elif b == c:
    prize = 1000 + b * 100
# 모두 다른 눈이 나오는 경우
else:
    prize = max(a, b, c) * 100

# 결과 출력
print(prize)