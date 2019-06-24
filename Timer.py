from time import time, sleep

class Timer ():
    def __init__(self, init : bool = False ):
        self.startingTime = time() if init else None
        self.endingTime   = None
        self.totalTime    = None
        
    def timeIsSet(self):
        return False if self.startingTime == None else True

    def startTimer(self):
        if self.timeIsSet(): return False
        else:
            self.startingTime = time()
            return self.startingTime
    
    def getCurrentTime(self):
        return False if not self.timeIsSet() else time() - self.startingTime
            

    def stopTimer(self):
        if not self.timeIsSet(): return False
        else:
            self.endingTime = time()
            self.totalTime = self.endingTime - self.startingTime
            return self.totalTime
    
    def resetTimer(self, init : bool = False):
        self.__init__(init)



if __name__ == '__main__':
    myTimer = Timer(True)
    print('Starting timer now...')
    myTimer.startTimer()
    print('Sleeping now...')
    sleep(4)
    print(f'Current time: {myTimer.getCurrentTime()}')
    sleep(2)
    print(f'Seconds transcurred {myTimer.stopTimer()}s')