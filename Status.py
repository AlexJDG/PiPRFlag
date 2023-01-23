from pathlib import Path

UP = 'up'
DOWN = 'down'

p = Path(__file__).with_name('flag.txt')


def getStatus():
    with p.open('r') as file:
        data = file.readlines()

    if len(data) < 1:
        data.append('')

    return data[0]


def setStatus(status):
    if status not in [UP, DOWN]:
        raise Exception("Only 'up' and 'down' are valid statuses")
    with p.open('w') as file:
        file.writelines(status)


print(getStatus())
