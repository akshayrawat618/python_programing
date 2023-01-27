
import re
from collections import Counter

my_regex =  r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
with open("/home/shadow_captain/workspace/python_coding/log_parsing/http.log", "r") as f:
    log = f.read()
    my_ip = re.findall(my_regex,log)
    ip_count = Counter(my_ip)
    print(ip_count)
    for k,v in ip_count.items():
        print("IP Address " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))
#print(log)

