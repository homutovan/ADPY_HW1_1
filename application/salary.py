def calculate_salary(work_category, minimal_salary = 8000):
    return minimal_salary * (1.16 ** (work_category - 1))
    