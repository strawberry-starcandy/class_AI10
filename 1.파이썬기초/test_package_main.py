# main program -> test_package/a_module과 test_package/b_module 을 import
from test_package import * # __init__.py 의 __all__ 에 나열된 모듈 모두 삽입

# 모듈 내부의 변수 출력
print(a.variable_a)
print(b.variable_b)