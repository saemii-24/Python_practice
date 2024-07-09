
# 아래 코드는 타입 에러를 발생시킨다.
# birth_year = input('태어난 년도: ')
# age = 2024 - birth_year + 1
# print(age)

# input으로 받은 값은 string이므로 주의한다.
# int()
# float()
# bool()
birth_year = input('태어난 년도: ')
print(type(birth_year)) #타입을 출력한다.

age = 2024 - int(birth_year) + 1
print(type(age))

print(age)

pound = input('파운드 무게: ')
kg = int(pound) * 0.453592
print(kg)