from icalendar import Calendar, Event, vText
import pytz
from datetime import datetime


#"\n\nMidterm Exam Date: Tuesday Feb 21\nOn-line Quiz Date: Jan 30\nEssay Deadline: Wed Mar 22 by 5pm\nFinal Exam Date: Date, time and place announced by the university\nConference with TA between Feb 16 and Feb 24\nSupplemental Exam: May (if applicable)"

#def parse_output_text(titles_dates_string):


def events_generator(titles_dates_list):
    # titles_dates_list is a list of tuples

    cal = Calendar()

    for i in range(len(titles_dates_list)):

        if len(titles_dates_list[i]) == 3:
            title, start_date, end_date = titles_dates_list[i]
        else:
            title, start_date = titles_dates_list[i]
            end_date = None

        event = Event()
        event.add('summary', title)
        event.add('dtstart', start_date)

        if end_date is not None:
            event.add('dtend', end_date)
        cal.add_component(event)

    directory = "./calendars/all_events.ics"
    f = open(directory, 'wb')
    f.write(cal.to_ical())
    f.close()


# testing
"""
timezone = pytz.timezone('US/Eastern')
date1 = datetime(2023, 1, 29, 8, 30, 0, tzinfo=timezone)
date2 = datetime(2023, 1, 30, 8, 30, 0, tzinfo=timezone)
titles_dates = [("test 03", date1), ("test 04", date2)]

events_generator(titles_dates)
"""


