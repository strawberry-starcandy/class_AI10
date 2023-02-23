# 계산기 프로그램 작성
# 1. 계산식 입력, +, -, *, / 만 허용
# 2. 처음 자료에 'q'가 입력되면 계산기 프로그램 종료
# 3. 입력된 자료가 숫자 부호 숫자 형식으로만 입력
# 4. 입력된 자료의 수는 3개인지 check
# 5. 처음 자료와 마지막 자료가 숫자인지 확인
# 6. 부호가 +, -, *, / 중에 있는지 확인
# 7. 위의 조건이 모두 맞으면 계산식 출력
# 8.             아니면 다시 입력

while True:
    str_input = input('수식을 입력하세요: ').split()
    if len(str_input) < 1:
        print('입력이 필요합니다.\n')
        continue
    if str_input[0][0] == 'q':
        print('프로그램을 종료합니다.\n')
        break
    if len(str_input) != 3:
        print('입력 항목이 잘못되었습니다.\n')
        continue
    
    if (not str_input[0].isdigit()) and (not str_input[2].isdigit()):
        print('처음과 마지막 자료는 숫자여야 합니다.\n')
    elif (len(str_input[1]) != 1) or (str_input[1] not in '+-*/'):
        print('두번째 자료는 부호여야 합니다(+-*/).\n')
    else:
        num1 = int(str_input[0])
        num2 = int(str_input[2])
        op = str_input[1]
        if op == '+':
            ans = num1 + num2
        elif op == '-':
            ans = num1 - num2
        elif op == '*':
            ans = num1 * num2
        elif op == '/':
            ans = num1 / num2
        print(f'{num1} {op} {num2} = {ans}\n')