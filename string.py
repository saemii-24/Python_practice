course = 'Python for Beginners'

print(course[0])
print(course[-2])
print(course[0:3])
print(course[0:])
print(course[1:])
print(course[:5])
print(course[:])

name = 'yooni'
# 1번 인덱스부터 -1자리를 제외하고 oon이 출력됨
print(name[1:-1])

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

# str 관련
course = 'Python! hello'
print(len(course))
print(course.title()) #각 단어 첫 글자 대문자로 변환
print(course.upper())
print(course.lower())
print(course)

#대소문자 구별함 없으면 -1
print(course.find('o'))
print(course.replace('ython', 'ie'))
#찾지 못할 경우 원래 문자 그대로 출력함
print(course.replace('ythons', 'ile'))

# course 변수안에 해당 글자가 존재하는지 확인한다
print('Python' in course)
print('python' in course) #대소문자 구분 False