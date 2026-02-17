#measering the time complexity:
#1.)Mersor by the import time 
import time
start=time.time()
for i in range(1,101):
    print(i)
"""i=1
while 1>=100:
    print(i)
    i+=1
end=time.time()  """  
print(f"start time:{start} end time:{end}\n Total time taken={end-start}")

#see the result and run multiple time and see the result and if we run this in defferent
# device then it will take also more time or less time 
"""so we use other measerining mwthod that reduce the device
 dependency of run time of the program"""