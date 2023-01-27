import kubernetes 
from kubernetes import client, config
import yaml
import re


def get_pod_details(cxt, nmsp):
    print("api connect")
    config.load_kube_config(context=cxt + "-c1")
    v1 = client.CoreV1Api()
    namespace = nmsp
    cluster_name = "devel"
    #pod_regex = "^(druid).\boverlord\b.\b{}\b.\bprod\b.[0-2]".format(cluster_name)
    print("Getting the details for namespace:{}".format(nmsp))
    pod_data = v1.list_namespaced_pod(nmsp)
    print("Getting the list")
    #print(pod_data)
    pod_list = []
    for pod in pod_data.items:
        pod_name = pod.metadata.name
        if re.match("druid-overlord-{}-devel-[0-2]".format(cluster_name), pod_name):
            pod_list.append(pod_name)
        #pod_name = re.match("druid-overlord-{}-devel-[0-2]".format(cluster_name), pod_name)
        #print("Matched pod_name:{}".format(pod_name))
        #pod_list.append(pod_name)
    print("Printing the final list")
    print(pod_list)

    for pod_name in pod_list:
        print(pod_name)

    #
    #api_status = v1.list_namespaced_pod(namespace=nmsp)
    #print(pod_name)
    #print(api_status)

def delete_pod(cxt, nmsp, pod):
    config.load_kube_config(context=cxt)
    v1 = client.CoreV1Api()
    ret = v1.list_namespaced_pod(nmsp)
    print('Deleting the Pod {}'.format(pod))
    pod = v1.delete_namespaced_pod(name=pod, namespace=nmsp, dry_run="All", pretty=True )
    del_pod = pod.metadata.name
    print(del_pod)
     
#get_pod_details("qus1-c1", "dba")
get_pod_details("qus1-c1", "druid-albus")
#delete_pod("qus1-c1", "dba", "helloworld-devel-0")

#cd /Users/arawat/workspace/source/dist 
## ./pants binary druid/core/src/main/python/alert
#time ./alert.pex --yaml clusters.yaml