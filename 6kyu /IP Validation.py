from ipaddress import ip_address
def is_valid_IP(s):
    try:
        return True if ip_address(s) else False
    except:
        return False
