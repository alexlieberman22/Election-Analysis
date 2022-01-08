import csv
# import os

file_read = 'ElectionAnalysis\Resources\election_results.csv'
file_write = 'ElectionAnalysis\Analysis\election_analysis.txt'

candidate_options = []
candidate_votes = {}
total_votes = 0

with open(file_read) as election_data:
    reader = csv.reader(election_data)

    headers = next(reader)

    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1
        

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
   
        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: {vote_percentage:.1f}% ")



# with open(file_write, "w") as txt_file:

#     Write data
