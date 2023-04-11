# 상수 선언
# 파이썬은 다른 언어처럼 상수 선언을 하는 키워드가 없음(ex : final, const)
# 따라서 변수처럼 상수 변수를 선언하고 사용할 수 있겠지만, 변경하고자 한다면 변경 가능
# 완전한 상수로 유지하고자 한다면 불가능한 것은 아니지만 별도의 추가적인 코드가 필요함
PI = 3.14
GRAVITY = 9.8

# 변수 선언
# 파이썬은 변수 선언시 먼저 선언할 필요가 없음
# 그떄그때 변수 선언 및 할당하면 됨
a = 100
b = 3.14
c = 'k'
d = 'hello'

# 다중 할당
a = b = c = d = 100

a, b, c, d = 100, 3.14, 'k', 'korea'

# 쌍따옴표, 홀따옴표
print(' "더이상 '+ "'카레'"+ '는 먹기 싫어요!" ')
print(' "더이상 \'카레\'는 먹기 싫어요!" ')
