
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop( )

@tl.job(interval=timedelta(milliseconds=100))
def FnTimerInterrupt( ):
    #print("2s job current time : "+ time.ctime())
    print()
    
if __name__ == "__main__":
    tl.start(block=False)
    print("in main")
    while True:
        None