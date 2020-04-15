from search.walker import DirectoryWalker
from javax.swing import JFrame, JTable, WindowConstants

class ScanResults(object):
    def __init__(self):
        self.results = []

    def add(self, file, line):
        self.results.append((file, line))

    def display(self):
        colnames = ['file', 'line']
        table = JTable(self.results, colnames)
        frame = JFrame("%i Results" % len(self.results))
        frame.getContentPane().add(table)
        frame.size = 400, 300
        frame.defaultCloseOperation = WindowConstants.EXIT_ON_CLOSE
        frame.visible = True

    @staticmethod
    def scan(dir, terms):
        results = ScanResults()
        for filename in DirectoryWalker(dir):
            for line in open(filename):
                for term in terms:
                    if term in line:
                        results.add(filename,line)
        return results
