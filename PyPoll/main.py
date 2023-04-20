import os, csv
from collections import defaultdict

# Variables
votes = {}
report = []
candidates = defaultdict()
ReportHead = "Election Results"
line = "-" * 28

# Open the csv file
csv_file = os.path.join("C:\\","Users","steam","Desktop","Starter_Code - Challenge3","PyPoll","Resources","election_data.csv")
txt_file = os.path.join("C:\\","Users","steam","Desktop","Starter_Code - Challenge3","PyPoll","analysis","report.txt")
with open(csv_file,'r',encoding='utf') as csvee:
    votes = csv.DictReader(csvee)
    for row in votes:
        if not row['Candidate'] in candidates:
            candidates[row['Candidate']] = 1
        else:
            candidates[row['Candidate']] += 1

TotalVotes = candidates['Charles Casper Stockham'] + candidates['Diana DeGette'] + candidates['Raymon Anthony Doane']

print(ReportHead)
print(line)
print(f"Total Votes: {TotalVotes}")
print(line)
for candidate in candidates:
    print(f"{candidate}: {round((candidates[candidate]/TotalVotes*100),3)}% ({candidates[candidate]})")
print(line)
print(f"Winner: {max(zip(candidates.values(),candidates.keys()))[1]}")
print(line)

report.append(f"\n{ReportHead}")
report.append(f"\n{line}")
report.append(f"\nTotal Votes: {TotalVotes}")
report.append(f"\n{line}")
for candidate in candidates:
    report.append(f"\n{candidate}: {round((candidates[candidate]/TotalVotes*100),3)}% ({candidates[candidate]})")
report.append(f"\n{line}")
report.append(f"\nWinner: {max(zip(candidates.values(),candidates.keys()))[1]}")
report.append(f"\n{line}")

txt = open(txt_file,'w')
txt.writelines(report)
txt.close()