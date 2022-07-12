import os
import csv
budget_csv = os.path.join("..", "Resources", "budget_data.csv")
#print result to a file
outputfile = os.path.join("PyBank Analysis.txt")
totalRevenue = 0
totalMonth=0
# Open and read csv
with open(budget_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
#grab header
    csvheader = next(csv_file)
    #move down a row after header
    firstRow=next(csvreader)
    #set 0
    totalMonths = 0
    totalRevenue += float(firstRow[1])
    previousRevenue=float(firstRow[1])
    monthlyChanges = []
    months=[]
    #find previous revenue
    previousRevenue = firstRow[1]
    print(f'Header: {csvheader}')
    for row in csvreader:
        totalMonths+=1
        totalRevenue+=float(row[1])
        netChange = float(row[1])-float(previousRevenue)
        monthlyChanges.append(netChange)
        #first month a change occurred
        months.append(row[0])
        previousRevenue=float(row[1])


averageChangePM = round(sum(monthlyChanges)/len(monthlyChanges),2)
greatIncrease=[months[0],monthlyChanges[0]]
greatDecrease=[months[0],monthlyChanges[0]]
for month in range(len(monthlyChanges)):
    #find greatest increase and decrease
    if(monthlyChanges[month]>greatIncrease[1]):
        greatIncrease[1]=monthlyChanges[month]
        greatIncrease[0]=months[month]
    if(monthlyChanges[month]<greatDecrease[1]):
        greatDecrease[1]=monthlyChanges[month]
        greatDecrease[0]=months[month]
    

#output
output = f'Total Months: = {totalMonths} \nTotal: = ${totalRevenue} \nAverage Change: ${averageChangePM}\nGreatest Increase in Profits:{greatIncrease}\nGreatest Decrease in Profits:{greatDecrease}'
print(f"Financial Analysis: \n------------------\n{output}")
with open(outputfile,"w") as textFile:
    textFile.write(f"Financial Analysis: \n------------------\n{output}")

 




