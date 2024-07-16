from pathlib import Path

#ecommerce가 존재하는가?
path = Path("ecommerce")
print(path.exists())

#emails 폴더를 만들어라
path = Path("emails")
print(path.mkdir())

#emails 폴더를 지워라
path = Path("emails")
print(path.rmdir())

# 모든 py파일을 검사한다.
path = Path()
print(path.glob('*.py'))
