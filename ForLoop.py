import time
#CountWatch 
#For x in range (start , end ,step)

#To skip an iteration

for x in range(1,21):
    if x== 13:
        continue #skips 13
        #break , breaks the whole next iteration
    else:
        print(x)

        #Countdown app
My_time=int(input("Enter time in seconds"))

for x in range(0,My_time):
    seconds = x % 60
    minuets = int(x/60) % 60
    hours = int(x/3600)% 24
    print(f"{hours}:{minuets}:{seconds}")
    time.sleep(1)

