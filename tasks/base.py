class Task:
    def __init__(self, filename):
        self.file = open(filename, "r")

    def __del__(self):
        self.file.close()

    def run1(self):
        pass

    def run2(self):
        pass

    def peek(self) -> str:
        pos = self.file.tell()
        line = self.file.readline()
        self.file.seek(pos)
        return line
