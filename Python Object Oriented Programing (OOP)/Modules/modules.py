    #importing specific modules
import datetime as dt

now = dt.datetime.now()
print(now)

#custom functions
import geometry #imports data from geometry file

print(geometry.area_rectangle(5,3)) #Output: 15
print(geometry.perimeter_rectangle(5,3)) #Output: 16
