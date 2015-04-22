import pygst
import gst
import time

class PlayerHasNoUriSet(BaseException):
    pass

def _on_tag(bus, msg):
        taglist = msg.parse_tag()
        print 'on_tag:'
        for key in taglist.keys():
            print '\t%s = %s' % (key, taglist[key])

class Player:

    def __init__(self):
        #creates a playbin (plays media form an uri)
        self.pipeline = gst.element_factory_make("playbin", "player")

        self.uri = None

        #listen for tags on the message bus; tag event might be called more than once
        self.bus = self.pipeline.get_bus()
        self.bus.enable_sync_message_emission()
        self.bus.add_signal_watch()
        self.bus.connect('message::tag', _on_tag)

    def play(self):
        if self.uri is not None:
            self.pipeline.set_state(gst.STATE_PLAYING)
        else:
            raise PlayerHasNoUriSet("Player has no URI set")

    def pause(self):
        self.pipeline.set_state(gst.STATE_PAUSED)

    def stop(self):
        self.pipeline.set_state(gst.STATE_NULL)

    def play_uri(self, new_uri):
        self.pipeline.set_state(gst.STATE_NULL)
        self.uri = new_uri
        self.pipeline.set_property('uri', new_uri )
        self.play()
