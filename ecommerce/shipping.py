def calc_shipping():
  print("calc_shipping")
  
  
  
# shipping.py
from ecommerce import process_payment 
#__init__.py에 process_payment를 공개 인터페이스에 포함시켜 주었으므로 다음과 같이 접근할 수 있다.

def calc_shipping():
    # 여기서 process_payment 함수를 사용할 수 있음
    process_payment()
    # 기타 배송 관련 로직
