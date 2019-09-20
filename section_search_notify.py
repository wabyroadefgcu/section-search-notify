#!/usr/bin/python3

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import emailer.email_results as email_results

debug = 0
sendEmail = 0

now = datetime.now() #get current time at beginning of script in order to send debug email twice per day at 7:45AM and 7:45PM
if (now.strftime('%I:%M') == '11:45'):
    debug = 1

payload2 = {'Termcode': '201808', 'Sess': '', 'Campcode': '', 'CollegeCode': '', 'Deptcode': '', 'Status': '',
            'Level': '', 'CRN': '80557', 'Subjcode': '', 'CourseNumber': '', 'CourseTitle': '', 'CreditHours': '',
            'courseattribute': '', 'BeginTime': '', 'Instructor': '', 'sortby': 'course', 'Button1': 'Search'}
courseResult2 = requests.post('https://gulfline.fgcu.edu/pls/fgpo/szkschd.p_showresult', data=payload2)
courseMatrix = []

soup2 = BeautifulSoup(courseResult2.text, 'html.parser')

table4b = soup2.find(id="Table4")
index = 0
tableHeadings = []

for tableRow in table4b.find_all("tr"):
    print("ROW: ")
    thisCourse = {}
    cellIndex = 0
    for tableCell in tableRow.find_all("td"):
        if(index == 0):
            tableHeadings.append(tableCell.text)
        else:
            thisCourse[tableHeadings[cellIndex]] = tableCell.text
        cellIndex = cellIndex + 1
    if (index >> 0):
        courseMatrix.append(thisCourse)
    index = index + 1


body = ""
for iterCourse in courseMatrix:
    thisCRN = iterCourse['CRN']
    thisCourseName = iterCourse['Course']
    thisMaxSeats = iterCourse['Max Seats']
    thisAvailSeats = iterCourse['Seats Avail.']
    thisTimeLoc = iterCourse['Meet Times Days -- Times -- Location         '].replace("\n"," ")

    print("CRN: " + thisCRN)
    print("Max Seats: " + thisMaxSeats)
    print("Avail. Seats: " + str(thisAvailSeats))
    print("Meet Times Days -- Times -- Location: " + thisTimeLoc)
    if (int(thisAvailSeats) >> 0) or (debug == 1):
        sendEmail = 1
        print("Seats Available!")
        availableClass = "Seats: " + thisAvailSeats + "  CRN: " + thisCRN + "  Course: " + thisCourseName\
                         + "  Schedule: " + thisTimeLoc + "\n\n";
        body += availableClass

if sendEmail == 1:
    subject = "Your report for %s" % (now.strftime('%m/%d/%Y %H:%M')) # change subject line here!
    result = email_results.email_section_list(subject, body)
