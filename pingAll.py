
from pythonping import ping
from colorama import Fore, Back, Style

def check_online(ip: str):
    # 如果扫描失败可以考虑增大timeout的值
    message = ping(ip, timeout=0.005)
    success_ping = "Reply"
    if success_ping in str(message):
        return True
    else:
        return False
 
if __name__ == '__main__':
    available_ip_last_addrs = []
    while True:
        available_ip_addrs = []
        ip_prefix = '192.168.31.'
        for ip_idx in range(20, 255, 1):
            ip_addr = ip_prefix + str(ip_idx)
            result = check_online(ip_addr)
            if True == result:
                available_ip_addrs.append(ip_addr)

        ip_diff = set(available_ip_addrs) - set(available_ip_last_addrs)
        ip_diff2 = set(available_ip_last_addrs) - set(available_ip_addrs)
        available_ip_last_addrs = available_ip_addrs
        print("当前网段新增ip")
        for ip in ip_diff:
            print(ip)
        print("当前网段掉线")
        for ip in ip_diff2:
            print(ip)
 