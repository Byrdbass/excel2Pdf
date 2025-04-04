import pandas as pd
import json

def parse_excel(file_path):
    data_frame = pd.read_excel(file_path)
    # array of objects
    student_data = []
    # underscore for a palceholder that is not used in data
    for _, row in data_frame.iterrows():
        full_name = row['Student'].strip()
        name_parts = full_name.split(',')
        last_name = name_parts[0]
        first_name = name_parts[1].strip()

        student = {
            'student_name': full_name.title(),
            'student_id' : str(row['Student id']),
            'grade_level' : str(row['Grade level'])
        }

        student_data.append(student)
    with open('student_data.json', 'w') as f:
        json.dump(student_data, f, indent=4)
        print("JSON created with {0} records".format(len(student_data)))
    return "JSON created with {0} records".format(len(student_data))

parse_excel('/Users/ByrdBass/Documents/MAESTRO BYRD/MARIACHI/Rosters Mariachi/Grade_change_project/AllPeriods.xls')