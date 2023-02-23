students = {}

def print_info_title():
    str_line = '=' * 5
    print('{:8s}\t{:8s}\t{:8s}\t{:8s}\t{:8s}'.format('이름', '국어', '영어', '수학', '평균'))
    print(f'{str_line:8s}\t' * 5)
    
def print_info_student(name, scores):
    print(f'{name:8s}\t{scores[0]:8s}\t{scores[1]:8s}\t{scores[2]:8s}\t{scores[3]:8s}')

def search_student():
    str_input = input('학생 이름 입력 (종료시 q) : ').strip()
    if str_input == 'q':
        return str_input
    elif str_input in students:
        print_info_title()
        print_info_student(str_input, students[str_input])
        return str_input
    else:
        print('    Error - 존재하지 않는 이름입니다.')
        return
    
def menu_print():
    print('메뉴')
    print('  1. : 학생 정보 입력')
    print('  2. : 학생 성적 조회')
    print('  3. : 학생 정보 삭제')
    print('  4. : 학생 전체 정보 조회')
    print('  9 : 프로그램 종료')
    return input('  메뉴를 선택하세요 : ')

def insert_menu():
    global students
    print('->1. : 학생 정보 입력')
    while True:
        str_input = input('학생의 이름, 국어, 영어, 수학 점수 입력 (종료시 q) : ').split()
        if len(str_input) == 0:
            continue
        elif str_input[0] == 'q':
            break
        elif len(str_input) != 4:
            print('    Error - 입력한 자료 갯수가 잘못되었습니다.')
        elif str_input[1].isnumeric() and str_input[2].isnumeric() and str_input[3].isnumeric():
            score_avr = sum(map(int, str_input[1:4])) / 3
            students[str_input[0]] = [*str_input[1:4], f'{score_avr:.2f}']
            print('    정상적으로 입력되었습니다.')
        else:
            print('    Error - 성적은 숫자로 입력하여야 합니다.')
        print()

def inquiry_student():
    global students
    print('->2. : 학생 성적 조회')
    while True:
        if search_student() == 'q':
            break
        print()

def delete_student():
    global students
    print('->3. : 학생 정보 삭제')
    while True:
        s_name = search_student()
        if s_name:
            if s_name == 'q':
                break
            str_yes = input('    삭제하시려면 \'Y\'를 입력하세요 : ').strip()
            if str_yes == 'y' or str_yes == 'Y':
                students.pop(s_name)
                print(f'    {s_name}의 정보가 삭제되었습니다.')
            else:
                print('    취소하였습니다.')
        print()

def inquiry_students():
    global students
    print('->4. : 학생 전체 정보 조회')
    print_info_title()
    for name, value in students.items():
        print_info_student(name, value)
    print()

while True:
    menu = menu_print()      # 초기 화면 출력
    if menu == '1':          # 학생 정보 삽입
        insert_menu()
    elif menu == '2':        # 개인 학생 정보 조회
        inquiry_student()
    elif menu == '3':        # 개인 학생 정보 삭제
        delete_student()
    elif menu == '4':        # 학생 전체 정보 조회
        inquiry_students()
    elif menu == '9':        # 프로그램 종료
        print('->9 : 프로그램 종료')
        break
    print()