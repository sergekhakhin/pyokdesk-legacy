import random

employee_dict = {
    'kis': 1,
    'mon': 3,
    'kha': 6,
    'per': 8
}


def get_employee_id_by_ref(ref: str):
    try:
        return employee_dict[ref]
    except KeyError:
        print("[ ERROR ] Не удалось найти сотрудника")


def get_employee_ref_by_id(employee_id: int):
    try:
        return [k for k, v in employee_dict.items() if v == employee_id]
    except KeyError:
        print("[ ERROR ] Не удалось найти сотрудника по ID")


def get_random_employee_id():
    id_list = list(employee_dict.values())
    id_list.remove(1)
    return random.choice(id_list)
