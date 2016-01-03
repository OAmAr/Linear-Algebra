class Vector:
    def __init__(self, first, second):
        self.f = first
        self.s = second
        self.unit = sqrt((first*first) +
    def add(self, vec):
        newf = self.f + vec.f
        news = self.s + vec.s
        return Vector (newf, news)
    def showCo(self):
        return self.f, self.s
    def showUn(self):
        
