def domain_name(url):
    dom = url.replace("http://", "").replace("www.","").replace("https://", "")
    dom = dom.split(".")
    return dom[0]

#https://www.codewars.com/kata/514a024011ea4fb54200004b/solutions/python
