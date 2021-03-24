import time

seconds = int(sys.argv[1])
while seconds:
        mins, secs = divmod(seconds, 60)
        hrs, mins = divmod(mins, 60)
        timer = 'Time left: {:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds-=1
print('\n\nTimer is up! :D')

