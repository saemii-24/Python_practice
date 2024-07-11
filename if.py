is_hot = False
is_cold = False

if is_hot:
    print("It's hot day")
    print("Drink plenty of water")
elif is_cold: # = else if
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

price = 1000000
credit = 'Good'

# == 두개만 사용한다 (3개 없음)
# 파이썬은 문자열과 숫자를 알아서 잘 구별한다.
if credit=='Good' :
    price *= 0.9
    print(price)
else:
    price *= 0.8
    print(price)

# AND OR NOT

temper = 35
if temper > 30:
    print("더워요")
else:
    print("안 더워요")


name = "J"
print(len((name)))

if len(name)<3:
    print("3글자보다 많이 입력하세요")
elif len(name) > 50:
    print("50글자보다 적게 입력하세요")
else:
    print("좋네요!")

