# main.py 파일
import test_module as test

print('main의 __name__ 출력 -> ', __name__)
radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))