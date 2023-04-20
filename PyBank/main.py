import os, csv, locale
locale.setlocale(locale.LC_ALL,'')

# Variables
change = []
ctr = 0
TotalBux = 0
TotalChange = 0
AvgChange = 0
Mo1 = 0
Mo2 = 0
ReportHead = "Financial Analysis"
line = "-" * 28

# Open the csv file
csv_file = os.path.join("C:\\","Users","steam","Desktop","Starter_Code - Challenge3","PyBank","Resources","budget_data.csv")
with open(csv_file,'r',encoding='utf') as csvee:
    bux = csv.DictReader(csvee)
    for row in bux:
        # Add Profit/Loss to TotalBux
        TotalBux += int(row['Profit/Losses'])
        # Calculate change between months
        if ctr == 0:
            Mo1 = int(row['Profit/Losses'])
        elif ctr == 1:
            Mo2 = int(row['Profit/Losses'])
            change.append(Mo2-Mo1)
        else:
            Mo1 = Mo2
            Mo2 = int(row['Profit/Losses'])
            change.append(Mo2-Mo1)
        ctr += 1

TotalMonths = ctr
# Calculate average change
for chg in change:
    TotalChange += chg
AvgChange = round(TotalChange / len(change),2)
# Show report
print(ReportHead)
print(line)
print(f"Total Months: {TotalMonths}")
print(f"Total: {locale.currency(TotalBux)}")
print(f"Average Change: {locale.currency(AvgChange)}")
print(f"Greatest Increase in Profits: {max(change)}")
print(f"Greatest Decrease in Profits: {min(change)}")