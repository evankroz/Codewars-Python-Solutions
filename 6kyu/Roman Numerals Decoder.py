roman_letters = (
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
        ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
        ('IV', 4), ('I', 1)
)

def solution(roman):
    result = 0
    index = 0
    for i, c in roman_letters:
        while roman[index : index+len(i)] == i:
            result += c
            index += len(i)
    return result
  #https://www.codewars.com/kata/51b6249c4612257ac0000005/python
