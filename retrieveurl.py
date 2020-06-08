
class retrieveURLs(object):

    def __init__(self, filename):
        self.filename = filename

    def getURL(self):
        with open(self.filename) as pageSpeedListURL:
            content = pageSpeedListURL.readlines()
            content = [line.rstrip('\n') for line in content]
            pageSpeedListURL.close()
        return content