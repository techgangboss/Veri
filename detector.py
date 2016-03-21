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

def getCommonList(time_list1,time_list2):
    common_list = []
    for q in time_list1:
        for m in time_list2:
            if q[3] == m[3]:
                s1 = []
                s1.append(q[0])
                s1.append(q[1])
                s1.append(q[2])
                s1.append(q[3])
                common_list.append(s1)

    #print(len(common_list))
    return common_list


#Adds to already present superlist
#Adds data from a timelist
def addtoSuperList(superList,newlist):
    diff = 0
    for ln in newlist:
        for idx in range(len(superList)):
            if ln[3] == superList[idx][3]:
                print len(superList[idx][4])
                superList[idx][4].append(newlist[4])
                print len(superList[idx][4])
            # else:
            #     time_inst = []
            #     time_inst_times = []
            #     time_inst.append(ln[0])
            #     time_inst.append(ln[1])
            #     time_inst.append(ln[2])
            #     time_inst.append(ln[3])
            #     time_inst_times.append(ln[4])
            #     time_inst.append(time_inst_times)
            #     superList.append(time_inst)

        #print ".",



    return superList


list1 = buildList('record2.csv')
list2 = buildList('record3_10.csv')
u1,t1 = buildMacList(list1)
u2,t2 = buildMacList(list2)

supList = addtoSuperList(t2,t1)
#print(str(len(t2)) + " element")