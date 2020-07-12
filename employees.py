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
