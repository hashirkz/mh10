import openai
import os
from dotenv import load_dotenv

load_dotenv('./.env')
OPENAI_API_TOKEN = os.getenv("OPENAI_API_TOKEN")

#sets the api key
openai.api_key = OPENAI_API_TOKEN

def get_response(pdf_text):
    """
    Takes in string parsed from pdf with all escape characters removed and returns the model's reponse
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What are the important dates for midterms, quizes, homework, exams, or assignments from the following text? " + pdf_text + " give the response in the following format - Event Name:MM/DD/YYYY. Exlude times of day. Take note of start dates and end dates. Make each event on a new line.",
        temperature=0.05,
        max_tokens=200,
        logit_bias={"22622": 1 , "4354": 1, "39": 1, "54": 1, "28718": 1, "6433": 1, "8021": 1, "16747": 1, "40781": 1, "900": 1, "3705": 1, "3109": 1, "321": 1, "4507": 1 , "528": 1} 
    )
    
    return response.choices[0].text

def format_dates(first_text):
    """
    Takes in a string with all escape characters removed and isolates the dates, formatting them into MM/DD/YYYY
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="remove everything in the following text except for dates which are formatted into MM/DD/YYYY: " + first_text,
        temperature=0.3,
    )

def get_response_summary(pdf_text: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="please summarize the following text" + pdf_text,
        max_tokens=200,
    )

    return response.choices[0].text

def get_response_ask(prompt: str, pdf_text: str) -> str:
    if len(pdf_text) > 7000: pdf_text = pdf_text[:7000]

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= prompt + 'in the following text' + pdf_text,
        max_tokens=200,
    )

    return response.choices[0].text

if __name__ == '__main__':
    text = '''
McGill University, Department of Mathematics and Statistics
Course Outline, Winter 2022
MATH 141 – Calculus 2 (4 CR)
Instructors
Section Name E-mail
001 Alberto Cavallo alberto.cavallo@mcgill.ca
002 Sean Bibby sean.bibby@mcgill.ca
003 J ́erˆome Fortier (coordinator) jerome.fortier@mcgill.ca
The list of teaching assistants and the details for office hours will be posted on myCourses.
Course Overview
The definite integral. Techniques of integration. Applications. Introduction to sequences and
series.
Restrictions
- Prerequisites: MATH 139 or MATH 140 or MATH 150.
- Restrictions: Not open to students who have taken MATH 121 or CEGEP objective 00UP or
equivalent. Not open to students who have taken or are taking MATH 122, except by permission
of the Department of Mathematics and Statistics.
Calendar
- Classes Period: From Wednesday, January 5 to Tuesday, April 12.
- Final Exams: From Wednesday, April 13 to Friday, April 29 .
- Tutorials: From Monday, January 10 to Friday, April 8.
- Study Break (no classes): From Monday, February 28 to Friday, March 4
Course Delivery
Lectures will be delivered online (on Zoom) due to large classes. However, if the epidemiological
situation safely permits, tutorials and exams will be in-person. The course will be delivered in
a “flipped classroom” approach. That means:
 On Monday, we will post a pre-recorded lecture common to all three sections, where the
theory for the whole week will be covered. The instructor who teaches that lecture will
vary from week to week. Sections 2 and 3 will not have a live lecture on that day.
 Examples will be worked out by the instructors in their respective sections for the remain-
ing two hours of lecture. Note that lectures of section 1 will be reduced to one hour each
in order not to advantage that section.
 There is also a mandatory two-hours tutorial, where you will work on some problems with
your peers, under supervision of a TA.
Textbook
We will cover most sections of Chapters 5, 6, 7, 8 and 11 of the following textbook:
Stewart, J., Clegg, D. and Watson, S., Calculus: Early Transcendentals, 9th Edi-
tion. Cengage Learning, 2019.
That being said, if you possess any other text covering all the material, you may not wish to
buy the required text. In particular, any prior edition is more than satisfactory.
Evaluation
The evaluation scheme consists of the following components.
- WeBWork Assignments (15%) : Web-based assignments graded by the computer. They
have a strict deadline, but you can take as much time as you like to work on the problems.
- Exams: Midterm (25%) and Final (40%). In-person, closed-book exams, unless the
pandemic forces us to move them online. Their precise dates will be posted on myCourses.
- Quizzes (20%) : These are timed assignments: they will be available for 48 hours and you
have one hour to complete them once you start. There will be approximately one quiz every
two weeks (six quizzes in total). To take possible technical issues into account, your quiz with
the lowest mark will not be counted towards your final grade.
Alternate grading scheme: 70% for the final exam, and all other components divided by
two. Note that this option will be available only if the final exam is in-person. We will take the
scheme that is the most advantageous to you: no need to register.
Need Help?
This term we will be using Piazza for class discussion. The system is highly catered to getting you
help fast and efficiently from classmates, TAs, and instructors. Rather than emailing questions
to the teaching staff, we encourage you to post your questions on Piazza. To signup, please click
here or use the link on myCourses.
This course is eligible to free tutoring services provided by the departmental helpdesk (Burnside-
911) and by FRezCA. Visit their web pages for more information.
Policies
You are allowed (in fact encouraged) to discuss the WebWork assignments with other students,
and you may consult any books, websites, etc. However, you must work out your own solution.
Direct copying from other students is not permitted.
Quizzes and exams should be completely worked out by yourself: seeking help from someone or
searching the web for those if strictly prohibited and may lead to disciplinary procedures (see
www.mcgill.ca/integrity for more information).
Absences on exams must be justified with appropriate documentation, and communicated be-
fore the exam (if possible) in order to arrange suitable accommodations. This is at the discretion
of the course coordinator for the midterm exam, and of your faculty for the final exam.
In accord with McGill University’s Charter of Students’ Rights, students in this course have the
right to submit in English or in French any written work that is to be graded.
In the event of extraordinary circumstances beyond the University’s control, the content and/or
evaluation scheme in this course is subject to change.
'''
    print(get_response(text))