import Queue

AGENDA_CAPACITY = 10

class Agenda:

    def __init__(self):
        self.content = Queue.PriorityQueue(AGENDA_CAPACITY)
