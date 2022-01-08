import csv
# import os

file_read = 'ElectionAnalysis\Resources\election_results.csv'
file_write = 'ElectionAnalysis\Analysis\election_analysis.txt'

candidate_options = []
candidate_votes = {}
total_votes = 0

winning_candidate = ""
winning_count = 0
winning_percentage = 0


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

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


print(f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")


# with open(file_write, "w") as txt_file:

#     Write data
