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

# === Experiment Sizing
# get z-score critical value and Standard Deviations
def get_sds(p,d):
    sd1=mt.sqrt(2*p*(1-p))
    sd2=mt.sqrt(p*(1-p)+(p+d)*(1-(p+d)))
    x=[sd1,sd2]
    return x

# z-score for given alpha
def get_z_score(alpha):
    return norm.ppf(alpha)

def get_sds(p,d):
    sd1=mt.sqrt(2*p*(1-p))
    sd2=mt.sqrt(p*(1-p)+(p+d)*(1-(p+d)))
    sds=[sd1,sd2]
    return sds

# the minimum sample size required per group 
def get_sampSize(sds,alpha,beta,d):
    n=pow((get_z_score(1-alpha/2)*sds[0]+get_z_score(1-beta)*sds[1]),2)/pow(d,2)
    return n

# === Calculate Sample Size per Metric
# adding the d parameter to each of the metrics characteristics for each metric
GC["d"]=0.01
R["d"]=0.01
NC["d"]=0.0075

# Gross Conversion
GC["SampSize"]=round(get_sampSize(get_sds(GC["p"],GC["d"]),0.05,0.2,GC["d"]))
GC["SampSize"]

# the total amount of samples per the Gross Conversion metric
GC["SampSize"]=round(GC["SampSize"]/0.08*2)
GC["SampSize"]

# Retention
R["SampSize"]=round(get_sampSize(get_sds(R["p"],R["d"]),0.05,0.2,R["d"]))
R["SampSize"]

R["SampSize"]=R["SampSize"]/0.08/0.20625*2
R["SampSize"]

# Net Conversion
NC["SampSize"]=round(get_sampSize(get_sds(NC["p"],NC["d"]),0.05,0.2,NC["d"]))
NC["SampSize"]

NC["SampSize"]=NC["SampSize"]/0.08*2
NC["SampSize"]

