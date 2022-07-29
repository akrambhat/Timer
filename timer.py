import os,time
      
def countdown(t):
    if x==1:
        t=t*60
    elif x==2:
        t=t*3600
    else:
        t=t
    os.system("clear")
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

os.system("clear")
x=int(input("0 for seconds\t1 for Minutes\t2 for Hours:\n"))
t = input("Enter the time: ")
countdown(int(t))
os.system(f"aplay sound.wav")
