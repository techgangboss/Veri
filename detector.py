from matplotlib import pyplot as plt
import matplotlib.dates as dates
import dateutil.parser as parser
import datetime
from matplotlib.dates import drange


#Builds a list from the file input
#List of Instances, not MAC
def buildList(file):
    lines  = []
    refined = []
    i = 0
    #Build List
    with open(file) as f:
        lines = f.read().splitlines()


    #Refine List
    for m in lines:
        if ',,' not in m:
            if 'Seen' not in m:
                refined.append(m.split(","))


    return refined



#Build list of unique addresses
#Name | Device Type | IP | MAC | Last Seen

def buildMacList(refined):
    mac_list = []
    time_list = []
    for rline in refined:
        if rline[3] not in mac_list:
            mac_list.append(rline[3])

            time_inst = []
            time_inst_times = []
            time_inst.append(rline[0])
            time_inst.append(rline[1])
            time_inst.append(rline[2])
            time_inst.append(rline[3])
            time_inst_times.append(rline[4])
            time_inst.append(time_inst_times)
            time_list.append(time_inst)

        else:
            for tm_el in time_list:
                tm_el[4].append(rline[4])




    # for z in range(3):
    #     if(len(time_list[z][4])>2):
    #         print(time_list[z])

    print(len(time_list))

    return mac_list,time_list


#Compare multiple files

def getSuperList(mac_list1,mac_list2):
    superList = []
    for q in mac_list1:
        if q in mac_list2:
            superList.append(q)

    print(len(superList))
    pass


list1 = buildList('record2.csv')
list2 = buildList('record3_10.csv')
u1,t1 = buildMacList(list1)
u2,t2 = buildMacList(list2)