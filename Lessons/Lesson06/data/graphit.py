# 
# Generic code to graph the virtual dartboard
# Created by: jrizos
# Created on: 4/7/2019
#

import matplotlib.pyplot as plt

def GraphIt(xin_, yin_, xout_, yout_):
    circle = plt.Circle((0.5, 0.5), radius =0.5, fill=False)
    ax = plt.gca()
    ax.add_patch(circle)
    plt.scatter(xin_, yin_, color='g', marker='.')
    plt.scatter(xout_, yout_, color='r', marker='.')
    
    plt.axis('scaled')
    plt.show()
    
    return None
