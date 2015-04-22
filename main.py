import schedule
from events import Agenda
from assistant import googleassistant

if __name__ == '__main__':
	"""
	Launches job scheduler.
	"""
        agenda = Agenda()
	ggl_assistant = googleassistant.GoogleAssistant()
        ggl_assistant.fill_agenda(agenda)
