# first=int(input())
# second=int(input())
# FT=first%10
# ST=second%10
# FH=first%100
# SH=second%100
# if FT > ST :
#     print(first)
# elif FT < ST :
#     print()
#     if FT == ST :
#         FH-FT > SH-ST:
#         print()
#         FH-FT<SH-ST:
#         print()
#         if FH-FT==SH-ST:

# 똥꼬쇼끝
            
# 2.
#리스트 뒤집기 reverse 함수
first, second = input().split()
first = int(first[::-1])
second = int(second[::-1])
if first>second:
    print(first)
else :
    print(second)
