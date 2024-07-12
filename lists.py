numbers=[3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
  if number > max:
    max= number
    print(max)
    
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

for row in matrix:
  for item in matrix:
    print(item)
    
numbers = [5,1,2,7,4]
# numbers.append(20)
numbers.insert(0,10)
numbers.remove(4)
print(numbers)

numbers.pop()
print(numbers)

numbers.index(5)
print(numbers)

numbers.clear()
print(numbers)
