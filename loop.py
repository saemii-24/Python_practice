i = 1
while i <= 5:
    print(i)
    i = i+1
print("Done")

number = 9
count = 0
limit = 3
guess = 6

while count < limit:
    count += 1
    if guess == number:
        print('You won!')
        break
else:
    print('You lose!')

for item in 'Python':
    print(item)

for item in range(10):
    #0부터 9까지
    print(item)

for item in range(5, 10):
    #5부터 9까지
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
#앞에 f를 써주어야 { } 안에 변수 넣어 출력 가능
print(f"Total: {total}")

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')


numbers = [5,2,5,2,2]
for x in numbers:
    print('*' * x)