from player import player
from datetime import datetime

class Alarm:

    def __init__(self):
        self.player = player.Player()


    def wake_up(self, agenda):
        event = agenda.content.get()
        if event.top <= datetime.now():
            self.player.play_uri(event.url)
