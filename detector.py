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
#fig = plt.figure()
#ax = fig.add_subplot(111)
# start = datetime.datetime.strptime("21-06-2014", "%d-%m-%Y")
# end = datetime.datetime.strptime("07-07-2014", "%d-%m-%Y")
# date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
# #ax.set_xticks()
plt.scatter(timelist,x)
plt.show()
