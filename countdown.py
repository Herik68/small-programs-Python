import time
my_time = int(input("Enter the time in seconds:"))
for x in range(my_time,0,-1):#for x in reversed(range(0,my_time):
    second=x%60
    minute=int(x/60)%60
    hour=int(x/3600)
    print(f'{hour:02}:{minute:02}:{second:02}')
    time.sleep(1)
print("Time up!")