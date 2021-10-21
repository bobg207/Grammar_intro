# Look to the slideshow in google classroom for notes
import csv


# prompt = input('Enter a query: ')


def open_file():
    company_db_dict = {}
    list1 = []
    list2 = []
    file_row_numb = 0
    with open('company_db.csv') as db:
        company_db = csv.reader(db)
        line1 = db.readline()
        line1_len = len(line1.split(','))
        for val in range(line1_len - 1):
            list2.append(val)
        for value in list2:
            for item in company_db:
                list1.append(item[list2[value]])
                company_db_dict.update({line1.split(',')[list2[value]]: list1[0:len(list1)-1]})

    return company_db_dict


def check_tokens(tokens, csv_dict):
    work = True
    tokens_s = tokens.split()
    if len(tokens_s) != 3 or len(tokens_s) != 7:
        work = False
    # elif


file = open_file()
print(file)

# check_tokens(prompt, file)
