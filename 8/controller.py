from models import init, add, show
def prog():
    text = init()
    kto = int(input('Ученик или учитель? \n1 - учитель\n2 - ученик\n'))
    if kto == 1:
        add(text)
    elif kto == 2:
        show(text)
