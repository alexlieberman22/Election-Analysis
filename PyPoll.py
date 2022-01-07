import csv
import os

file_read = os.path.join('Resources','election_results.csv')
file_write = os.path.join('Analysis', 'election_analysis.txt')

candidate_options = []
total_votes = 0

with open(file_read) as election_data:
    reader = csv.reader(election_data)

    headers = next(reader)

    for row in reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

print(total_votes)
print(candidate_options)


# with open(file_write, "w") as txt_file:
    
    #Write data
