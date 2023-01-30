

def get_user_ids(file_name):
    with open (file_name, 'r') as fd:
        for line in fd:
            data = line.split()
            id = data[0].split(":")[2]
            users = data[0].split(":")[0]
            shell = data[0].split(":")[-1]
            print(id +"|"+ users +"|"+ shell)


get_user_ids("/etc/passwd")
