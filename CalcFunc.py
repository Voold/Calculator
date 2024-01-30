def write_number(field, number):
    if field.text() != "0":
        field.setText(field.text() + number)
    else:
        field.clear()
        field.setText(number)


def operate(func, field, arr):
    if len(field.text()) != 0:
        arr.append([func, int(field.text())])
        field.clear()


def minus(field, res, num):
    res -= int(num)
    field.clear()
    return res


def plus(field, res, num):
    res += int(num)
    field.clear()
    return res


def percent(field, res, num):
    res /= int(num)
    field.clear()
    return res


def equ(field, arr):
    if len(arr) != 0:
        arr.append([None, int(field.text())])
        field.clear()
        res = arr[0][1]
        for i in range(len(arr) - 1):
            res = arr[i][0](field, res, arr[i + 1][1])
        field.setText(str(res))
        arr.clear()
    else:
        field.setText("0")
