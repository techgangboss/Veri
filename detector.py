from matplotlib import pyplot as plt
import matplotlib.dates as dates
import dateutil.parser as parser
import datetime
from matplotlib.dates import drange


lines  = []

#Build List
with open('record.csv') as f:
   for line in f:
       if line!='\n':
           if 'Name' not in line:
               if 'New_York' not in line:
                lines.append(line.replace("\n","").split(","))


#Name | Device Type | IP | MAC | Last Seen

#Build record for one
def buildRecord(lines, z):
    personOne = []
    personOneIdentify = []
    personOneTimes = []

    personOneIdentify.append(lines[0][0])
    personOneIdentify.append(lines[0][1])
    personOneIdentify.append(lines[0][2])
    personOneIdentify.append(lines[0][3])


    for m in lines:
        if m[2] == personOneIdentify[2]:
            personOneTimes.append(m[4])

    personOne.append(personOneIdentify)
    personOne.append(personOneTimes)

    # print len(personOneTimes)

    # print personOne



    timelist = []

    for r in personOneTimes:
        r1 = r.split(" ")[1]
        timelist.append(parser.parse(r))


    x = [1]*len(timelist)
    return x

usrlist = []
rcd = []
for z in range(len(lines)):
    rcd.append(z)
    usrlist.append(buildRecord(lines,z))


plt.scatter(usrlist[0],rcd[0])
plt.show()
