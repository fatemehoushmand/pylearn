seconds = int(input('enter seconds:'))

hours = seconds /3600
minutes = seconds / 60

minutes2 = seconds - hours- minutes
seconds2 = seconds - minutes2

print(int(hours) , ':' ,int(minutes2)  ,':' ,int(seconds2))