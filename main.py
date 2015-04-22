import schedule
from alarm import alarm
from events import Agenda
from assistant import googleassistant

if __name__ == '__main__':
	"""
	Launches job scheduler.
	"""
        agenda = Agenda()
        alarm  = alarm.Alarm()
	ggl_assistant = googleassistant.GoogleAssistant()
        ggl_assistant.fill_agenda(agenda)
        schedule.every().minute.do(alarm.wake_up, agenda)
