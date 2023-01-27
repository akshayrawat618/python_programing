from collections import Counter

with open("/home/shadow_captain/workspace/python_coding/log_parsing/http.log", "r") as f:
    log = f.read()
    log_line = log.split()
    my_ip = log_line[0]
    print(my_ip)
    ip_count = Counter(my_ip)
    for k,v in ip_count.items():
        print("IP Address " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))
    print(log_line[0])