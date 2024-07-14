# age = int(input('Age: '))
# print(age)

try:
  age = int(input('Age: '))
  income = 20000
  risk = income / age
  print(age)
except ZeroDivisionError: # Python 표준 라이브러리에서 제공하는 내장 예외 클래스
  print('Age cannt be 0.')
except ValueError:
  print('Invalid age')
  
