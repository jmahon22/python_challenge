#import csv
import os
import csv
budgetdata_csv = os.path.join("Resources", "budget_data.csv")

TotalMonths=0
TotalProfitLoss=0
TotalChange=0
LastProfitLoss=0
RecentChange=0
GreatestProfit=0
GreatestProfitMonth=""
GreatestLoss=0
GreatestLossMonth=""

#open and read csv
with open(budgetdata_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#read the header row first
    csv_header = next(csv_reader)

    for row in csv_reader:  
#total number of months included in dataset
        TotalMonths+=1
#net total amount of profit/losses over entire period
        TotalProfitLoss+=int(row[1])
#average of changes in profit/losses over entire period
        if TotalMonths==1:
            LastProfitLoss=int(row[1])
        else:
            RecentChange=int(row[1])-LastProfitLoss
            TotalChange+=RecentChange
            LastProfitLoss=int(row[1])
#greatest increase in profits (date and amount) over the entire period
        if RecentChange>GreatestProfit:
            GreatestProfit=RecentChange
            GreatestProfitMonth=str(row[0])
#greatest decrease in losses (date and amount) over the entire period
        elif RecentChange<GreatestLoss:
            GreatestLoss=RecentChange
            GreatestLossMonth=str(row[0])

AvgChange="%.2f" % (TotalChange/(TotalMonths-1))
#print analysis to terminal and export a test file with results
output_path = os.path.join("Analysis", "PyBankResults.txt")
with open(output_path, 'w') as txtfile:
    print("Financial Analysis", file=txtfile)
    print("Financial Analysis")
    print("-----------------------", file=txtfile)
    print("-----------------------")
    print(f"Total Months: {TotalMonths}", file=txtfile)
    print(f"Total Months: {TotalMonths}")
    print(f"Total: ${TotalProfitLoss}", file=txtfile)
    print(f"Total: ${TotalProfitLoss}")
    print(f"Average Change: ${AvgChange}", file=txtfile)
    print(f"Average Change: ${AvgChange}")
    print(f"Greatest Increase in Profits: {GreatestProfitMonth} (${GreatestProfit})", file=txtfile)
    print(f"Greatest Increase in Profits: {GreatestProfitMonth} (${GreatestProfit})")
    print(f"Greatest Decrease in Profits: {GreatestLossMonth} (${GreatestLoss})", file=txtfile)
    print(f"Greatest Decrease in Profits: {GreatestLossMonth} (${GreatestLoss})")
