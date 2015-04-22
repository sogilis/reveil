from assistant import Assistant
from events import agenda
from googlecalendar import authenticate
from datetime import datetime

class GoogleAssistant(Assistant):

    def __init__(self):
        self.service = authenticate.get_service()

    def fill_agenda(self, agenda):
        now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print 'Getting the upcoming 10 events'
        eventsResult = self.service.events().list(
            calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])

        if not events:
            print 'No upcoming events found.'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print start, event['summary']
            agenda.content.put((0, event))
