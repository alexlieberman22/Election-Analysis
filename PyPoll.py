from _typeshed import ReadableBuffer
import csv
import os

file_read = os.path.join('Resources','election_results.csv')
file_write = os.path.join('Analysis', 'election_analysis.txt')


with open(file_read) as election_data:
    reader = csv.reader(election_data)

    headers = next(reader)
    then_this = next(headers)
    print(headers)
    print(then_this)



    # for row in reader:
    #     print(row)





# with open(file_write, "w") as txt_file:
    
    #Write data
