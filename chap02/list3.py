# 리스트의 모든 원소를 enumerate() 함수로 스캔하기

x = ['Jhon', 'Gerorge', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')