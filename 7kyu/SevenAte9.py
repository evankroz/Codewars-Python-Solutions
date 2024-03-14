import re
def seven_ate9(str_):
    while "797" in str_:
        str_ = re.sub("797", "77", str_)
    return str_






#test.assert_equals(seven_ate9('165561786121789797'),'16556178612178977')
#test.assert_equals(seven_ate9('797'),'77')
#test.assert_equals(seven_ate9('7979797'),'7777')