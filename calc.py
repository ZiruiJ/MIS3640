import math
print (math.pi)
3.141592653589793
print ('The volume of a sphere with radius 5 is {}'. format (100*3.141592653589793))
# The volume of a sphere with radius 5 is 314.1592653589793
print ('The the total wholesale cost for 60 copies is {}'. format (24.95*60*0.6+(3+0.75*59)))
# The the total wholesale cost for 60 copies is 945.4499999999999

print ('the percentage of the increase is {:.1f}%'. format (7/82))
# the percentage of the increase is 0.1%

start=(6*60+52)*60
easy=(8*60+15)*2
fast=(7*60+12)*3
finish_hour=(start+easy+fast)/(60*60.0)
finish_floored=(start+easy+fast)//(60*60)
finish_minute=(finish_hour-finish_floored)*60
print('Finish time was %d:%d' %(finish_hour,finish_minute))