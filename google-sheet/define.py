import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Authenticate using credentials
creds = ServiceAccountCredentials.from_json_keyfile_name('weighty-gasket-414010-2cb2a336174b.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets document
spreadsheet_id = '1uy6TCfYZPAHgTZQMTDvYfjwMj0NVvhSXL00bsNEznhA'
spreadsheet = client.open_by_key(spreadsheet_id)

# Select the worksheet
worksheet = spreadsheet.sheet1

# Define the headers
headers = ["Student Name", "Compiler design", "computer networks", "Machine learning", "Design and analysis of algorithm", "cloud computing", "Total", "Average", "Percentage"]

# Update headers in the first row
worksheet.append_row(headers)

# Define student names and their marks for five subjects
students = {
    "Monika Mali": [90, 85, 75, 60, 70],
    "Apeksha Surywanshi": [85, 75, 80, 90, 95],
    "Devki Deshpande" : [90, 60, 80, 50, 68]
}

# Calculate total, average, and percentage for each student and append to the worksheet
for student, marks in students.items():
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    max_marks_per_subject = 100
    total_max_marks = len(marks) * max_marks_per_subject
    percentage = (total_marks / total_max_marks) * 100
    
    # Append student name, marks for five subjects, total, average, and percentage
    row = [student] + marks + [total_marks, average_marks, percentage]
    worksheet.append_row(row)

print("Student names, marks, total, average, and percentage added successfully.")