import os, csv, locale
locale.setlocale(locale.LC_ALL,'')

# Variables
change = []
report = []
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
txt_file = os.path.join("C:\\","Users","steam","Desktop","Starter_Code - Challenge3","PyBank","analysis","report.txt")
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
# Output report to console
print(ReportHead)
print(line)
print(f"Total Months: {TotalMonths}")
print(f"Total: {locale.currency(TotalBux)}")
print(f"Average Change: {locale.currency(AvgChange)}")
print(f"Greatest Increase in Profits: {max(change)}")
print(f"Greatest Decrease in Profits: {min(change)}")

# Store report in a variable, write variable to file
report.append(f"\n{ReportHead}")
report.append(f"\n{line}")
report.append(f"\nTotal Months: {TotalMonths}")
report.append(f"\nTotal: {locale.currency(TotalBux)}")
report.append(f"\nAverage Change: {locale.currency(AvgChange)}")
report.append(f"\nGreatest Increase in Profits: {max(change)}")
report.append(f"\nGreatest Decrease in Profits: {min(change)}")
txt = open(txt_file,'w')
txt.writelines(report)
txt.close()