import schedule
from events import agenda
from assistant import googleassistant

if __name__ == '__main__':
	"""
	Launches job scheduler.
	"""
        agenda = agenda.Agenda()
	ggl_assistant = googleassistant.GoogleAssistant()
        ggl_assistant.fill_agenda(agenda)
