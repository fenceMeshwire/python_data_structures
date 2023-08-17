#!/usr/bin/env python3

# Python 3.9.5

# replace_statements.py

# Dependencies
import os
import re

def change_working_directory():
    path = "/home/user/files"
    os.chdir(path)
    return

def correct_terms_in_statement():
    # Regular Expression for a term:
    term = re.compile(r"'\w{12}'") # 'ABCDEF123456' or 'A1B2C3D4E5F6', etc.

    # Import statements:
    with open('statements.txt', encoding='utf-8') as statements:
        imported_statements = statements.readlines()
    statements = [s.replace("\n", "") for s in imported_statements]

    # Import list of terms:
    with open('terms.txt', encoding='utf-8') as corrected_terms:
        new_terms = corrected_terms.readlines()
    new_terms = [t.replace("\n", "") for t in new_terms]

    # Replace corrected terms in statement:
    for i in range(len(new_terms)):
        location = term.search(statements[i])
        term_start = location.start()
        term_end = location.end()
        new_term = new_terms[i]
        first = statements[i][:term_start]
        last = statements[i][term_end:]
        statements[i] = first + "'" + new_term + "'" + last

    # Write new statements to TXT file:
    corrected = open('corrected_statements.txt', 'w')
    for element in statements:
        corrected.write(element + "\n")
    corrected.close()
    return

if __name__ == '__main__':
    change_working_directory()
    correct_terms_in_statement()
