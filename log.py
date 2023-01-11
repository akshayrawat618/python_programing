# Given the apache logs below, determine the following:
    # Count the total number of requests
    # Count the number of requests per type (get / put / post / delete)
    # Average size of various types of requests  (get / put / post / delete)
    # Count the total number of requests per ip address per type (get / put / post / delete)

'''
#! /bin/bash 

#count the total number of requests
file='/usercode/FILESYSTEM/log.txt'
request_count=`cat $file | wc -l` 
echo "Total_request_count = $request_count"
    
#count the number of request per type
request_per_type=`cat $file | awk -F " " {'print $6'} | sort | uniq -c` 
echo "Request/call: $request_per_type"


#Average Size of various type of request
request=`cat $file | awk -F " " {'print $6,$10'}`
request_types=`cat $file | awk -F " " {'print $6'} | sort | uniq`
for i in $request_types ;do
    size=`cat $file | grep -i $i | awk -F " " {'print $10'}`
    sum=0
    for i in $size;do
       sum=$(($sum+$i));
    done
    echo $sum
done
'''
def get_count():
    count = 0
    with open(r"/home/shresth_rawat/workspace/akshay_workspace/log.txt", 'r') as fp:
        for line in fp:
            count += 1 
    print(count)

def number_of_req_type():
    with open(r"/home/shresth_rawat/workspace/akshay_workspace/log.txt", 'r') as fp:
        for line in fp:
            req_type = line.split('PUT')
    print (req_type)    

get_count()
number_of_req_type()

#get_count()
number_of_req_type()