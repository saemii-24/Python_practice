customer = {
  "Name": "hyo",
  "Email": "hyo@example.com",
  "phone": 1234,
  "singer": True
}

print(customer["Name"])

#key값이 존재하지 않는 값에 기본값을 줄수 있다
print(customer.get("birthdate", "April")) #April
print(customer.get("birthdate")) #None
# None은 주로 값이 없거나 초기화 되지 않은 변수이자 하나의 고유한 객체다. 

