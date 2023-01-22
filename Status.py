UP = 'up'
DOWN = 'down'


def getStatus():
    with open('flag.txt', 'r') as file:
        data = file.readlines()

    if len(data) < 1:
        data.append('')

    return data[0]


def setStatus(status):
    if status not in [UP, DOWN]:
        raise Exception("Only 'up' and 'down' are valid statuses")
    with open('flag.txt', 'w') as file:
        file.writelines(status)
