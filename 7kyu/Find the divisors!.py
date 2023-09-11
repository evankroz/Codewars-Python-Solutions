def divisors(n):
    res = []
    for i in range(2, n):
        if n % i == 0:
            res.append(i)
    return res if res else "{} is prime".format(n)
  #https://www.codewars.com/kata/544aed4c4a30184e960010f4/python
