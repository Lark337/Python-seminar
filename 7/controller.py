from models import add, show
def prog():
    a = int(input('Выберите операцию:\n1 = Добавление данных\n2 = Вывод данных\n'))
    if a == 1:
        add()
    if a == 2:
        show()