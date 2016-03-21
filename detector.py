from matplotlib import pyplot as plt
import matplotlib.dates as dates
import dateutil.parser as parser
import datetime
from matplotlib.dates import drange



#____________________

# lines1  = []
#
# #Build List
# with open('record.csv') as f:
#    for line1 in f:
#        if line1!='\n':
#            if 'Name' not in line1:
#                if 'New_York' not in line1:
#                 lines1.append(line1.replace("\n","").split(","))
#
#
# #Name | Device Type | IP | MAC | Last Seen
#
#
# mac_list1 = []
# for m1 in lines1:
#     mac1 = m1[3]
#     if mac1 not in mac_list1:
#         mac_list1.append(mac1)
#
# print len(mac_list1)
#_________________

#____________________

lines2  = []
refined = []
i = 0
#Build List
with open('record3_10.csv') as f:
   lines2 = f.read().splitlines()


#Refine List
for m in lines2:
    if ',,' not in m:
        if 'Seen' not in m:
            refined.append(m.split(","))




#Check unique addresses
#MAC at location 3
#Name | Device Type | IP | MAC | Last Seen


mac_list1 = []
for m1 in refined:
    mac1 = m1[3]
    if mac1 not in mac_list1:
        mac_list1.append(mac1)

print len(mac_list1)