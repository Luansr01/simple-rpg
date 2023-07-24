MAX_LOG = 5

class Log:
    log = []

    def AddLine(self, txt):
        line_count = len(self.log)

        if(line_count > MAX_LOG):
            self.log.pop(0)
            
        self.log.append("> " + txt)

    def Clear(self):
        self.log = []
    
    def Print(self):
        print("\n".join(self.log))
