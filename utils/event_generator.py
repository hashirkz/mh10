from icalendar import Calendar, Event
import os


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
    os.makedirs(os.path.dirname(directory), exist_ok=True)
    with open(directory, 'wb') as f:
        f.write(cal.to_ical())
    f.close()