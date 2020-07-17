import random

employee_dict = {
    'kis': 1,
    'mon': 3,
    'kha': 6,
    'sok': 7,
    'per': 8
}


def get_employee_id(ref):
    try:
        return employee_dict[ref]
    except KeyError:
        print("[ ERROR ] Не удалось найти сотрудника")


def get_random_employee_id():
    id_list = list(employee_dict.values())
    id_list.remove(1)
    return random.choice(id_list)


def get_employee_ref(employee_id):
    try:
        return [k for k, v in employee_dict.items() if v == employee_id]
    except KeyError:
        print("[ ERROR ] Не удалось найти сотрудника по ID")
