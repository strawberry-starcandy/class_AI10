# main program -> test_package/a_module과 test_package/b_module 을 import
from test_package import a_module as a
from test_package import b_module as b

# 모듈 내부의 변수 출력
print(a.variable_a)
print(b.variable_b)