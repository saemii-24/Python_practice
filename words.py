# 자리수 맞추기
x = 123
formatted_string = f'{x:010}'
print(formatted_string)  # 출력: 0000000123


# 금액 콤마
x = 9000000
formatted_string = f'{x:,}'
print(formatted_string)  # 출력: 9,000,000


# 소수점 이하 자리수
x = 0.123
formatted_string = f'{x:.5f}'
print(formatted_string)  # 출력: 0.12300


#글자 연결해서 작성하기
person1 = 'conan'
person2 = 'kid'

print(f'{person1 + person2} 좋아')