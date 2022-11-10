#!/usr/bin/env python3
import rospy
from random import uniform, choice
from math import copysign


"""
This is a simple pythin script that generates random values
for circN parameters read by simple_sim to place objects

It places 1, 2 or 3 circles in a +/- 1.5m area around the
center of the map
"""

def randsign():
    """ Return -1 or 1 randomly """
    return copysign(1, uniform(-1.0, 1.0))


# Init as a node so it can access the ros parameter server
rospy.init_node('place_random_object')

# Number of objects to place
#to_place = choice([1,1,1,2,2,3])
#to_place = choice([1,1,2,2,2])

for i in range(10):
    # Place a random circle
    rospy.set_param('circ{}'.format(i), [
        #uniform(0.3, 1.2) * randsign(), # x
        #uniform(0.3, 1.2) * randsign(), # y
        #uniform(0.1, 0.2), #radius
        uniform(0.52, 2.3), # x
        uniform(-1.7, -0.445), # y
        uniform(0.04, 0.049), #radius
    ])