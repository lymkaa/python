class StringHandler:
    def getString(self):
        self.s = input()
        
    def printString(self):
        print(self.s.upper())

if __name__ == "__main__":
    sh = StringHandler()
    sh.getString()
    sh.printString()
