def greet_user():
  print('hi!')
  print('welecome')
  
print("start")
greet_user()
print("finish")


def greet_name(name):
  print(f'Hi {name}!')
  print('welecome')
  
print("start")
greet_name("hyo")
print("finish")


def greet_people(people1, people2):
  print(f'Hi {people1} {people2}!')
  print('welecome')
  
print("start")
greet_people(people2="hyo",people1="tion") #키워드 인수를 사용하면 순서를 바꾸어도 무방하다.
print("finish")

#값 return 하기
def square(number):
  return number*number

print(square(10))

def emoji_converter(message):
  words = message.split(" ")
  emojis={
    ":)":"😊",
    ":(":"😕"
  }
  output = ""
  for word in words:
    output += emojis.get(word,word)+(" ")
  return output

message = input(">")
print(emoji_converter(message))