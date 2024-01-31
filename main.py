import csv

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    print(index)
    print(row)
    print(row.score)
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

# approach 1 to use CSV reader
# with open('nato_phonetic_alphabet.csv') as data_file:
#     data = csv.reader(data_file)
#     new_data = {row[0]:row[1] for row in data}
# alpha_pd = pandas.DataFrame(new_data, index=[0])
# print(alpha_pd)
# print(alpha_pd.A[0])

# approach 2 to use pandas read_csv
alpha_pd = pandas.read_csv('nato_phonetic_alphabet.csv')
print(alpha_pd)
alpha_dict = {row.letter:row.code for (index, row) in alpha_pd.iterrows()}
print(alpha_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        list = [alpha_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please !!!")
        generate_phonetic()
    else:
        print(list)

generate_phonetic()
