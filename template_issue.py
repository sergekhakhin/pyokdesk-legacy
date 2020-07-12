from companies import *
from employees import *
from issues import *

while True:
    template_title = str(input("[ INPUT ] Название заявки: "))
    if not template_title:
        print("[ ERROR ] Название заявки не может быть пустым!")
        continue
    else:
        break

while True:
    company_id = get_company_id(input("[ INPUT ] Организация: "))
    if not company_id:
        continue
    else:
        break

while True:
    employee_id = get_employee_id(input("[ INPUT ] Сотрудник: "))
    if not employee_id:
        continue
    else:
        break

while True:
    comment = input("[ INPUT ] Комментарий: ")
    if not comment:
        print("[ ERROR ] Комментарий не может быть пустым!")
        continue
    else:
        break

services = []
while True:
    if not services:
        try:
            service_id = int(input("[ INPUT ] ID спецификации: "))
            service_quantity = int(input("[ INPUT ] Количество (спецификация): "))
            service_tuple = (service_id, service_quantity)
            services.append(service_tuple)
        except ValueError:
            print("[ ERROR ] Некорректный ввод!")
            continue
    else:
        try:
            service_id = input("[ INPUT ] ID спецификации (q для выхода): ")
            if service_id == 'q':
                break
            service_id = int(service_id)
            service_quantity = int(input("[ INPUT ] Количество (спецификация): "))
            service_tuple = (service_id, service_quantity)
            services.append(service_tuple)
        except ValueError:
            print("[ ERROR ] Некорректный ввод!")
            continue

while True:
    try:
        quantity = int(input("[ INPUT ] Количество создаваемых заявок: "))
        break
    except ValueError:
        print("[ ERROR ] Некорректный ввод!")
        continue

created_issues = []
for i in range(1, quantity + 1):
    title = f'{template_title} ({i}/{quantity})'
    payload = {
        'company_id': str(company_id),
        'assignee_id': str(employee_id),
        'author': {
            'id': str(employee_id),
            'type': 'employee'
        }
    }
    issue_id = create_issue(title, **payload)
    created_issues.append(issue_id)

for issue_id in created_issues:
    leave_comment(issue_id, comment, employee_id)
    for service in services:
        add_service(issue_id, service[0], service[1], employee_id)
    change_issue_status(issue_id, 'completed')
