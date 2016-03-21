
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

print personOne