from icalendar import Calendar, Event, vText
import pytz
from datetime import datetime


"\n\nMidterm Exam Date: Tuesday Feb 21\nOn-line Quiz Date: Jan 30\nEssay Deadline: Wed Mar 22 by 5pm\nFinal Exam Date: Date, time and place announced by the university\nConference with TA between Feb 16 and Feb 24\nSupplemental Exam: May (if applicable)"

def events_generator(titles_dates_string):

    timezone = pytz.timezone('US/Eastern')
    cal = Calendar()

    

    event = Event()
    event.add('summary', event_title)

    event.add('dtstart', start_date)
    #if end_date is not None:
       # event.add('dtend', end_date)

    #event.add('dtstamp', date)

   # if location is not None:
      #  event['location'] = vText(location)

    # Adding events to calendar
    cal.add_component(event)

    # ics file will be generated at this directory
    #directory = "./calendars/your_events.ics"
    #f = open(directory, 'ab')
    #f.write(cal.to_ical())
    #f.close()

# testing

cal1 = Calendar()

timezone = pytz.timezone('US/Eastern')

for i in range(2):
    event = Event()

event1 = Event()
event1.add('summary', "test1")
sdate1 = datetime(2023, 1, 30, 8, 30, 0, tzinfo=timezone)
event1.add('dtstart', sdate1)
cal1.add_component(event1)

event2 = Event()
event2.add('summary', "test2")
sdate2 = datetime(2023, 1, 31, 8, 30, 0, tzinfo=timezone)
event2.add('dtstart', sdate2)
cal1.add_component(event2)

#edate1 = datetime(2023, 1, 31, 9, 0, 0, tzinfo=timezone)
#event_generator(cal1, "test1", sdate1)


#sdate2 = datetime(2023, 1, 31, 8, 30, 0, tzinfo=timezone)
#edate2 = datetime(2023, 1, 31, 9, 0, 0, tzinfo=timezone)
#event_generator(cal1, "test2", sdate2)

#sdate3 = datetime(2023, 2, 1, 8, 30, 0, tzinfo=timezone)
#edate3 = datetime(2023, 2, 1, 9, 0, 0, tzinfo=timezone)
#event_generator(cal1, "test3", sdate3)



# for the discord bot 
#with open('./calendars/your_events.ics', 'rb') as fp:
#    await channel.send(file=discord.File(fp, 'your_events.ics'))

directory = "./calendars/your_events_test.ics"
f = open(directory, 'wb')
f.write(cal1.to_ical())
f.close()