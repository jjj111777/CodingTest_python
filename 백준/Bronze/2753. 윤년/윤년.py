year = int(input())

# 윤년 판별
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(1)
else:
    print(0)