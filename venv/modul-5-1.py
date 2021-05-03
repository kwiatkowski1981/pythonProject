def group_them(**kwargs):
    result = ''
    for key, value in kwargs.items():
        # print(f'{key.capitalize()} is {value}')
        result += key.capitalize() + ' is ' + value + '\n'
    return result


def test_group_them(capsys):
    group_them(wall='red', tomato='red', light='yellow')
    out, err = capsys.readouterr()
    assert out == 'Wall is red\nTomato is red\nLight is yellow\n'


print(group_them(wall='red', tomato='red', light='yellow'))
