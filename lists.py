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

# 인덱스 0번에 10 삽입
numbers.insert(0,10)

# 리스트 첫번째 4 제거
numbers.remove(4)

# 리스트 마지막 요소 제거, 그 값 반환
numbers.pop()

# 리스트에 3이 있는 지 확인 True / False
3 in numbers

#5개 갯수 세어 반환
numbers.count(5)

# 값 5의 첫번째 인덱스 반환
numbers.index(5)

# 리스트 오름차순 정렬
numbers.sort()

# 리스트 순서 뒤집기
numbers.reverse()

#복사본 만들어 numbers2에 저장
numbers2 = numbers.copy()

# 리스트 모든 요소 제거
numbers.clear()

# 중복값 지우기
numbers= [2,2,4,6,3,4,6,1]
unique = []

for number in numbers:
  if number not in unique:
    unique.append(number)
print(unique)