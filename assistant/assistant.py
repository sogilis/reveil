class Assistant:

    def __init__(self):
        raise NotImplementedError("You Are Using An Interface")

    def fill_agenda(self, agenda):
        """
        Empty the agenda and fill it with new events freshly fetched
        from the remote calendar.
        Emptying and refill must be done atomically.
        """
        raise NotImplementedError("You Are Using An Interface")
