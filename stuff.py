# Look to the slideshow in google classroom for notes
import csv


# prompt = input('Enter a query: ')


def open_file():
    company_db_dict = {}
    list1 = []
    file_row_numb = 0
    with open('company_db.csv') as db:
        company_db = csv.reader(db)
        line1 = db.readline()
        for val in range(0, len(line1.split(','))):
            list1.clear()
            for item in company_db:
                list1.append(item[val])
                company_db_dict.update({list1[0]: list1[1:len(list1)-1]})

    return company_db_dict


def check_tokens(tokens, file):
    work = True
    tokens_s = tokens.split()
    if len(tokens_s) != 3 or len(tokens_s) != 7:
        work = False
    # elif


file = open_file()
print(file)

# check_tokens(prompt, file)
