from matplotlib import pyplot as plt
import matplotlib.dates as dates
import dateutil.parser as parser
import datetime
from matplotlib.dates import drange


#Builds a list from the file input
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



#Check unique addresses
#MAC at location 3
#Name | Device Type | IP | MAC | Last Seen

def countUniqueMac(refined):
    mac_list1 = []
    for m1 in refined:
        mac1 = m1[3]
        if mac1 not in mac_list1:
            mac_list1.append(mac1)

    print len(mac_list1)





countUniqueMac(buildList('record2.csv'))
countUniqueMac(buildList('record3_10.csv'))