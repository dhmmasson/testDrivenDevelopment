# Flight-Phases

## Flight Phases

For those interested, you can read research paper [1] or thesis [2] for free.

### Concept

In this project, we will implement a very simplistic heuristic: we will simply look at the `yaw` value. If it is relatively constant, it is a **cruise** phase. Whatever happens before the first cruise phase is the **take off** phase, whatever remains after the last cruise phase is the **landing** phase.

![alt text](phases.png "Phases illustration")

> _Fig. 1 Illustration of flight phases simple heuristic in our project.  
 Top: Flight path.  
 Middle: Yaw values. A green line indicates the beginning of a plateau. A red line indicates the end of a plateau. (Note that the green and red lines in the middle are merged on this example)  
 Bottom: Yaw delta values_

### Algorithm

1. Take the yaw values
2. Take the delta values (simple difference between `i` and `i-1`)
3. Consider delta values that are
	1. **smaller than 1**
	2. for yaw values that are **different from -1** (default values when the sensors are not turned on yet)
	3. after at least **10 delta values were greater than 1** (To make sure we do not get first plateau happening before any yaw consequent modification)
4. A plateau is defined as a portion in time for which values delta values are < 1 **and for at least 60 seconds**

> Note  
With this pseudo-algorithm and its heuristics, most flight analyses make sense.  
Only one flight (RU) will have an undetected take off phase.

```python
def findPlateaux(values, timestamp) :
	
	## PREPARE THE DATA #########################

	# get the delta
	delta = delta(values)				# no need for delta time division
	# get the indexes we are interested in
	# we want the index for which
	#		* yaw values != -1
	#		* delta values < 1
	#		* after at least 10 deltas > 1 happened (to make sure the sensors were correctly switched on!)
	indexes = delta.where(<1 and values != -1 and turbulences_happened = True)					# !Important: threshold of 1 
	# get the distance between these indexes
	distance_index = diff(indexes)
	start, end  = None
	array = []

	## MAIN LOOP #########################
	loop on i:
		if start_plateau_detected:
			save(start)
		if end_plateau_detected:
			save(end)
			save_in_array([start, end])

	## FILTERING #########################
    # filter the saved plateaus to know if they 
    # are long enough in time to be considered
    for start, end in array:
    	if time_between(start, end) > 60 			# !Important: threshold of 60
        save_in_results([start, end])
    return results


def OtherFuntion(...)
    plateaus = findPlateaux(yaws, timestamp)

    take_off = before(plateaus.first())
    landing = after(plateaus.last())
    cruise = plateaus.first.start() to plateaus.last.end()



```

[1] Goblet, Valentine & Fala, Nicoletta & Marais, Karen. (2015). Identifying Phases of Flight in General Aviation Operations. 10.2514/6.2015-2851. [link](https://www.researchgate.net/publication/299610035_Identifying_Phases_of_Flight_in_General_Aviation_Operations)

[2] Goblet, Valentine Pascale. "Phase of flight identification in general aviation operations." (2016). [link](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1807&context=open_access_theses)
