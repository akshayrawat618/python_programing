
def get_user_ids(file_name):
   with open (file_name, 'r') as fd:
       for line in fd:
           data = line.split()
           id = data[0].split(":")[2]
           print(id)


get_user_ids("/etc/passwd")