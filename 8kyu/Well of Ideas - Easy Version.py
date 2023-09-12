def well(x):
    if x.count("good") == 0:
        return "Fail!"
    if x.count("good") == 1 or x.count("good") == 2:
        return "Publish!"
    if x.count("good") > 2:
        return "I smell a series!"
#https://www.codewars.com/kata/57f222ce69e09c3630000212/python
