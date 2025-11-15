class LSMBuffer:
    def __init__(self):
        self.memtable = {}

    def write(self, key, value):
        self.memtable[key] = value

    def flush(self):
        flushed = self.memtable
        self.memtable = {}
        return flushed