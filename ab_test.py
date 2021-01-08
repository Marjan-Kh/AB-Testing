# This program provides a walkthrough of the A/B testing course's final
# project provided by Udacity in collaboration with Google.

#======================================================================
# Author: Marjan Khamesian
# Date: January 2021
#======================================================================

import math as mt
import numpy as np
import pandas as pd
from scipy.stats import norm

# === Baseline data
# placing - the estimators gievn by Udacity - into a dictionary
baseline = {"Cookies":40000,"Clicks":3200,"Enrollments":660,"CTP":0.08,"GConversion":0.20625,
           "Retention":0.53,"NConversion":0.109313}


# === Estimating Analytically 
# getting the p (probability) and n (sample size) needed for different metrics.
# computing the Stansard Deviation (sd).

# Gross Conversion (GC)
GC={}
GC["d_min"]=0.01
GC["p"]=baseline["GConversion"]
GC["n"]=baseline["Clicks"]
GC["sd"]=round(mt.sqrt((GC["p"]*(1-GC["p"]))/GC["n"]),4)
GC["sd"]

# Retention (R)
R={}
R["d_min"]=0.01
R["p"]=baseline["Retention"]
R["n"]=baseline["Enrollments"]
R["sd"]=round(mt.sqrt((R["p"]*(1-R["p"]))/R["n"]),4)
R["sd"]

# Net Conversion (NC)
NC={}
NC["d_min"]=0.0075
NC["p"]=baseline["NConversion"]
NC["n"]=baseline["Clicks"]
NC["sd"]=round(mt.sqrt((NC["p"]*(1-NC["p"]))/NC["n"]),4)
NC["sd"]


