# Chapter03-4
# 파이썬 튜플
# 리스트와 비교를 중요포인트로 잡아야 하는 자료형
# 튜플 자료형은 순서와 중복은 가능하나 수정과 삭제가 안된다. 불변 용도 : 절대 변하지 않는 값들을 저장하기 좋다.

# 선언

a = () # 리스트는 대괄호로 선언을 하였다면, 튜블은 소괄호로 선언을 한다.
b = (1,) # 만약 원소가 하나인 경우에 튜플은 선언하고 싶다면, 괄호 안에 콤마를 꼭 찍어줘야한다. (1)만 입력하면 class는 int형으로 나온다.
print(type(a), type(b)) # 이처럼 둘 다 튜플 자료형으로 나옴을 알 수 있다.

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine') # 리시트와 같이 튜플도 자료형의 상관없이 선언이 가능하다.
e = (100, 1000, ('Ace', 'Base', 'Captine')) # 리스트 때와 마찬가지로 튜플 안에 튜플을 선언 할 수 있다.

# 인덱싱
print('d - ', d[1]) # 튜플도 선언 후 인덱싱을 할 때, '[]'(대괄호)를 사용한다.
print('d - ', d[0] + d[1] + d[1]) # 이도 리스트랑 똑같이 계산이 가능하다.
print('d - ', d[-1]) # 당연하게도 리스트 처럼 우측 열로부터 인덱싱을 해온다.
print('e - ', e[-1]) # '-1'의 원소는 튜플이기 때문에 튜플이 출력됨을 알 수 있다.
print('e - ', e[-1][1]) # '-1'의 원소인 튜플 내에서 '1'의 원소를 인덱싱하므로 'Base'가 출력 (이또한 리스트랑 똑같음)
print('e - ', list(e[-1][1])) # 또한 튜플도 리스트의 자료형으로 형변환이 가능하다. 리스트로 형변환이된다,

# 수정기능 학인
# d[0] = 1500 처럼 리스트 때와 같이 수정하려고 선언하면 튜플형은 수정이 불가능하다고 에러가 발생한다.

# 슬라이싱 : 리스트랑 동일하다.
print('d - ', d[0:3]) # 이것도 리스트와 동일하게 0,1,2번째 원소가 슬라이싱되어 출력됨을 알 수 있다.
print('d - ', d[2:]) # 이처럼 생략도 완벽하게 출력됨을 알 수 있다.

# 튜플 연산 : 리스트와 동일하다.
print('c + d', c + d) # 연산도 당연히 동일하게 작동된다.
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2)) # 튜플 함수는 리스트와는 다르게 수정과 삭제가 불가능 하기에 함수가 많이 쓰이지는 않는다. 리스트때 배웠던 인덱스와 카운트만 기억하자.

# 팩킹 & 언팩킹 (Packing and Unpacking)

# Packing
t = ('foo', 'bar', 'baz', 'qux')
print(t) # 우리가 늘 해왔던 과정을 팩킹이라고 한다. 팩킹은 말그대로 '묶다'의 의미를 가지고 있다. 위처럼 우리가 선언하여 하나의 자료형으로 묶이는 저 과정을 팩킹이라고 한다.

# Unpacking
(x1, x2, x3, x4) = t # 각각의 변수로 팩킹되어 있는 변수를 변수 t로 선언한다. (()가 없더라도 언팩킹이 이뤄진다. 단, 국룰상 갈호를 씌운다.)

print(type(x1), type(x2), type(x3), type(x4)) # 각각의 class는 str(문자형)으로 출력된 것을 알 수 있다.
print(x1, x2, x3, x4) # 각각의 Type이 문자형인 이유는 t를 선언할 때, 문자로 팩킹되어 튜플형이 되었던 원소들이 다시 언팩킹되어 문자형으로 각각의 변수에 재선언된 것.

# 팩킹 & 언팩킹
t2 = (1, 2, 3)
t3 = 4, # 괄호를 생략해도 튜플로 선언이 된다. 단, 하나의 원소는 언제나 ,을 빼먹으면 안된다.
x1, x2, x3 = t2 # Unpacking
x4, x5, x6 = 4, 5, 6 # Unpacking

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6) # 이처럼 전부 팩킹과 언팩킹이 잘 이뤄진 것을 알 수 있다. 간단하게 정리하면 팩킹 <-> 언팩킹은 반대되는 개념이다.
