print("팩맨 게임을 시작합니다.")
print("유령이 나타났다")
print("1.도망간다 2.아이템쓴다 3.싸운다")
number = int (input("숫자를 입력하세요: "))
# 유저가 입력한 글자를 출력
print("유저 입력값:", number)
# 만약에 유저가 입력한 글자가 1이면 도망
if number == 1:
    print("도망")
# 만약에 유저가 입력한 글자가 2면 아이템
if number == 2:
    print("아이템 사용")
# 만약에 유저가 입력한 글자가 3이면 싸운다
if number == 3:
    print("싸운다")