def bonus_time(salary, bonus):
#2 solutions, 1st is faster
    if bonus == True:
      new_salary = f"${salary * 10}"
    else:
      new_salary = f"${salary}"
    return new_salary
#or
    return f"${salary}" if bonus == False else f"${salary * 10}"
