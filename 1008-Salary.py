employee_number = int(input())
worked_hours = int(input())
amount_per_hour = float(input())

employees_salary = worked_hours * amount_per_hour

print(f'NUMBER = {employee_number}')
print(f'SALARY = U$ {employees_salary:.2f}')
