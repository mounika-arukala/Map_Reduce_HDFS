#!/usr/bin/env python
 
import sys

last_key = None
running_total = 0
new_key = 0.0
new1_key = 0.0
max1_key = 0
max_key = None
max_total = 0
max2_key = None
#running_total=0.0
for input_line in sys.stdin:
   input_line = input_line.strip()
   this_key, value = input_line.split("\t", 1)
   value = int(value)
 
   if last_key == this_key:
       running_total += value
       if value>new_key:
		new_key=value

   else:
       if last_key:
	   new1_key = new_key*100/running_total
	   if max1_key<new1_key:
		max1_key=new1_key
		max2_key=last_key
           #print( "%s\t%d\t%d\t%d" % (last_key, running_total,new_key,new_key*100/running_total ))
       running_total = value
       last_key = this_key
       new_key = value
 
if last_key == this_key:
	new1_key = float(new_key)*100/float(running_total)
	if max1_key<new1_key:
		max1_key=new1_key
		max2_key=last_key
   	#print( "%s\t%d\t%d\t%d" % (last_key, running_total, new_key, new1_key) )

print("The County is %s"%(max2_key))
