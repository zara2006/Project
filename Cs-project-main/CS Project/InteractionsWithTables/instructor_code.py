import user_code as user
import common_functions
import csv

subject_file = r"CS Project\Tables\subjects.csv"
questions_file = r"CS Project\Tables\questions.csv"

def add_class(name, passing_grade, code, section): # Done
    data = common_functions.__read_file_csv(subject_file)
    id = user.__maximum_id_csv(data)
    
    if not __check_if_class_exists(name, section, data):
        new_class = [id, name, passing_grade, code, section]
        common_functions.__add_csv(new_class, subject_file)
        return True
    return False

def __check_if_class_exists(name, section, data):
    for subject in data:
        if subject[1] == name and subject[3] == section:
            return True
        
    return False

# add a question to questions.csv
# def add_question(question, answers, correct, subject_id, difficulty):
#     with open(questions_file, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)
#         ids = [int(row[0]) for row in reader if row]
#     new_id = max(ids, default=0) + 1

#     with open(questions_file, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([new_id, question, *answers, correct, subject_id, difficulty])
#     print(f"Question added successfully under subject ID '{subject_id}' with ID {new_id}.")

# # edit a subject in subjects.csv
# def edit_subject(subject_id, field_to_edit, new_value):
#     updated = False
#     with open(subjects_file, 'r') as file:
#         rows = list(csv.reader(file))
#         headers = rows[0]
#         if field_to_edit not in headers:
#             print(f"Invalid field '{field_to_edit}'. Valid fields are: {headers}")
#             return
#         field_index = headers.index(field_to_edit)

#     for row in rows:
#         if row[0] == str(subject_id):
#             row[field_index] = new_value
#             updated = True
#             break

#     if updated:
#         with open(subjects_file, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(rows)
#         print(f"Updated '{field_to_edit}' for subject ID '{subject_id}' to '{new_value}'.")
#     else:
#         print(f"Subject with ID '{subject_id}' not found.")

# # remove a question from questions.csv
# def remove_question(question_id):
#     removed = False
#     with open(questions_file, 'r') as file:
#         rows = list(csv.reader(file))

#     with open(questions_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         for row in rows:
#             if row[0] == str(question_id):
#                 removed = True
#                 continue
#             writer.writerow(row)

#     if removed:
#         print(f"Question with ID '{question_id}' removed successfully.")
#     else:
#         print(f"Question with ID '{question_id}' not found.")

# # remove a subject from subjects.csv
# def remove_subject(subject_id):
#     removed = False
#     with open(subjects_file, 'r') as file:
#         rows = list(csv.reader(file))

#     with open(subjects_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         for row in rows:
#             if row[0] == str(subject_id):
#                 removed = True
#                 continue
#             writer.writerow(row)

#     if removed:
#         print(f"Subject with ID '{subject_id}' removed successfully.")
#     else:
#         print(f"Subject with ID '{subject_id}' not found.")




