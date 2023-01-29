from icalendar import Calendar, Event, vText
#import pytz
from datetime import datetime


def events_generator(titles_dates_list):
    """
    Input: A list of tuples of either length 2 or 3. 
           Tuple format: (str, datetime, datetime) or (str, datetime)
    Output: None. 
    This function creates/overwrites the all_events.ics file in the calendars folder.
    """

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
date1 = datetime(2023, 1, 29, tzinfo=timezone)
date2 = datetime(2023, 1, 30, tzinfo=timezone)
date3 = datetime(2023, 1, 31, 8, 30, 0, tzinfo=timezone)
date4 = datetime(2023, 2, 1, 8, 30, 0, tzinfo=timezone)
titles_dates = [("test 06", date1), ("test 07", date2), ("test 08", date3, date4)]

events_generator(titles_dates)
"""

