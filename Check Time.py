from datetime import datetime
current_time = datetime.now() 
t = current_time.hour #This Prints The Current Hour Digit Alone For Instance Time Is 9:22 It Prints 9 Alone
b = current_time.minute
print(t)
print(b) #this prints the minute alone
print(t,":",b) #this prints the entire time
