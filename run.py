
import time
while True :
    time.sleep(0.3)
    try :
        exec(open('svg.py').read())
    except Exception as err:
        print(err)