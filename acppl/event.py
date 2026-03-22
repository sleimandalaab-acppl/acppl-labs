class Event:
    def __init__(self, name, timestamp, **kwargs):
        self.name = name
        self.timestamp = timestamp
        self.data = kwargs
