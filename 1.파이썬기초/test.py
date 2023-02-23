class Test:
    def __init__(self, name):
        self.name = name
        print(f'{self.name}이 생성 됨')
    def __del__(self):
        print(f'{self.name}이 파괴 됨')

a = Test('A')
b = Test('B')
c = Test('C')
