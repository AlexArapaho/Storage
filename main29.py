from random import choice
import json

def get_person():
    global id_num
    global name
    global tel
    id_num = ''
    name = ''
    tel = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(id_num) != 10:
        id_num += choice(nums)
    # print(id_num)

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {
        id_num: {
        "name": name,
        "tel": tel
        }
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = {}

    data[id_num] = {"name": name,
        "tel": tel}
    with open('person.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(get_person())