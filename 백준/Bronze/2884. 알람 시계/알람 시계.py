# 현재 시간 입력받기
H, M = map(int, input().split())

# 45분 일찍 알람 설정
if M >= 45:
    M -= 45
else:
    H = H - 1 if H > 0 else 23  # H가 0이면 23으로 설정
    M = 60 - (45 - M)

# 결과 출력
print(H, M)