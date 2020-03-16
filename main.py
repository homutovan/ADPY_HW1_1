from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    
    employes_list = {'Ivanov','Petrov', 'Sidorov'}
    
    for employee in employes_list:
        print(f'Сотрудник: {employee} заработная плата в месяц: {calculate_salary(get_employees(employee)):.2f}р.')