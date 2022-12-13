import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fLock = threading.Lock()
        self.bLock = threading.Lock()
        self.fbLock = threading.Lock()
        self.mainLock = threading.Lock()
        self.fLock.acquire()
        self.bLock.acquire()
        self.fbLock.acquire()
        self.done = False

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fLock.acquire()
            if self.done:
                return
            printFizz()
            self.mainLock.release()
                

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.bLock.acquire()
            if self.done:
                return
            printBuzz()
            self.mainLock.release()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fbLock.acquire()
            if self.done:
                return
            printFizzBuzz()
            self.mainLock.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.mainLock.acquire()
            if i % 15 == 0:
                self.fbLock.release()
            elif i % 5 == 0:
                self.bLock.release()
            elif i % 3 == 0:
                self.fLock.release()
            else:
                printNumber(i)
                self.mainLock.release()
        self.mainLock.acquire()
        self.done = True
        self.fbLock.release()
        self.fLock.release()
        self.bLock.release()
        return