# Look to the slideshow in google classroom for notes
import csv


prompt = input('Enter a query: ')


def open_file():
    company_db_dict = {}
    list1 = []
    list2 = []
    file_row_numb = 0
    with open('company_db.csv') as db:
        
        # makes row 1 the keys, and fills dictionaries with each rows data 
        # company_db = csv.DictReader(db)

        # loop thru the dictionaries and add them to the main dictionary
        # for row in company_db:
        #     company_db_dict.update(row)
        
        
        company_db = csv.reader(db)
        line1 = db.readline()
        line1_len = len(line1.split(','))
        for val in range(line1_len - 1):
            list2.append(val)
        for value in list2:
            for item in company_db:
                list1.append(item[value])
                company_db_dict.update({line1.split(',')[value]: list1[0:len(list1)-1]})

    return company_db_dict


def check_tokens(tokens, csv_dict):
    work = True
    key_list = ['first', 'last', 'sex', 'age', 'date', 'salary', 'position']
    lo_op_list = ['<', '>', '==', '!=', '<=', '>=']
    tokens_s = tokens.split()
    if len(tokens_s) != 3 and len(tokens_s) != 7:
        work = False
    if len(tokens_s) == 3:
        if tokens_s[0] not in key_list:
            work = False
        elif tokens_s[1] not in lo_op_list:
            work = False
    if len(tokens_s) == 7:
        if tokens_s[4] not in key_list:
            work = False
        elif tokens_s[5] not in lo_op_list:
            work = False
    if work:
        print('Valid')
    else:
        print('Not Valid')


file = open_file()
print(file)

check_tokens(prompt, file)
