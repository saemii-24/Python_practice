# 파이썬에서 __init__.py 파일이 존재하는 디렉토리는 패키지로 인식된다.
#  __init__.py 파일은 패키지의 공개 인터페이스를 정의한다.

# ecommerce/__init__.py
from .shipping import calc_shipping
from .payment import process_payment

__all__ = ['calc_shipping', 'process_payment']
