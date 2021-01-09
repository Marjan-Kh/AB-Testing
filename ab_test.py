# This program provides a walkthrough of the A/B testing
# course's final project provided by Udacity.

#========================================================
# Author: Marjan Khamesian
# Date: January 2021
#========================================================

import math as mt
import numpy as np
import pandas as pd
from scipy.stats import norm

# === Baseline data
# =================
# placing - the estimators gievn by Udacity - into a dictionary
baseline = {"Cookies":40000,"Clicks":3200,"Enrollments":660,"CTP":0.08,"GConversion":0.20625,
           "Retention":0.53,"NConversion":0.109313}

# == Estimating Standard Deviation
# ================================
# Scale The counts estimates
baseline["Cookies"] = 5000
baseline["Clicks"] = baseline["Clicks"]*(5000/40000)
baseline["Enrollments"] = baseline["Enrollments"]*(5000/40000)
baseline

# === Estimating Analytically
# =========================== 
# getting the p (probability) and n (sample size) needed for different metrics.
# computing the Stansard Deviation (sd).

# Gross Conversion (GC)
GC = {}
GC["d_min"] = 0.01
GC["p"] = baseline["GConversion"]
GC["n"] = baseline["Clicks"]
GC["sd"] = round(mt.sqrt((GC["p"]*(1-GC["p"]))/GC["n"]),4)
GC["sd"]

# Retention (R)
R = {}
R["d_min"] = 0.01
R["p"] = baseline["Retention"]
R["n"] = baseline["Enrollments"]
R["sd"] = round(mt.sqrt((R["p"]*(1-R["p"]))/R["n"]),4)
R["sd"]

# Net Conversion (NC)
NC = {}
NC["d_min"] = 0.0075
NC["p"] = baseline["NConversion"]
NC["n"] = baseline["Clicks"]
NC["sd"] = round(mt.sqrt((NC["p"]*(1-NC["p"]))/NC["n"]),4)
NC["sd"]

# === Experiment Sizing
# =====================
# get z-score critical value and Standard Deviations
def get_sds(p,d):
    sd1 = mt.sqrt(2*p*(1-p))
    sd2 = mt.sqrt(p*(1-p)+(p+d)*(1-(p+d)))
    x = [sd1,sd2]
    return x

# z-score for given alpha
def get_z_score(alpha):
    return norm.ppf(alpha)

def get_sds(p,d):
    sd1 = mt.sqrt(2*p*(1-p))
    sd2 = mt.sqrt(p*(1-p)+(p+d)*(1-(p+d)))
    sds = [sd1,sd2]
    return sds

# the minimum sample size required per group 
def get_sampSize(sds,alpha,beta,d):
    n = pow((get_z_score(1-alpha/2)*sds[0]+get_z_score(1-beta)*sds[1]),2)/pow(d,2)
    return n

# === Calculate Sample Size per Metric
# ====================================
# adding the d parameter to each of the metrics characteristics for each metric
GC["d"] = 0.01
R["d"] = 0.01
NC["d"] = 0.0075

# Gross Conversion
GC["SampSize"] = round(get_sampSize(get_sds(GC["p"],GC["d"]),0.05,0.2,GC["d"]))
GC["SampSize"]

# the total amount of samples per the Gross Conversion metric
GC["SampSize"] = round(GC["SampSize"]/0.08*2)
GC["SampSize"]

# Retention
R["SampSize"] = round(get_sampSize(get_sds(R["p"],R["d"]),0.05,0.2,R["d"]))
R["SampSize"]

R["SampSize"] = R["SampSize"]/0.08/0.20625*2
R["SampSize"]

# Net Conversion
NC["SampSize"] = round(get_sampSize(get_sds(NC["p"],NC["d"]),0.05,0.2,NC["d"]))
NC["SampSize"]

NC["SampSize"] = NC["SampSize"]/0.08*2
NC["SampSize"]

# === Analyzing the Experiment Results
# ====================================
# loading the dataset 
control = pd.read_csv("../input/control-data/control_data.csv")
experiment = pd.read_csv("../input/experiment-data/experiment_data.csv")
control.head()

# Number of rows in the control & experiment dataset
control.shape[0]
experiment.shape[0]

# == Sanity Checks
# Number of Pageviews in control & experiment group
pageviews_cont = control['Pageviews'].sum()
pageviews_exp = experiment['Pageviews'].sum()
pageviews_total = pageviews_cont+pageviews_exp
print ("number of pageviews in control:", pageviews_cont)
print ("number of pageviews in experiment:" ,pageviews_exp)

# Number of cookies who viewed the course overview page: Is p_hat within confidence interval range?
p = 0.5
alpha = 0.05

# Probability of the event to occur
p_hat=round(pageviews_cont/(pageviews_total),4)

# Sample size
n = pageviews_total

# Standard deviation
sd = mt.sqrt(p*(1-p)/n)

# Margin of error
ME = round(get_z_score(1-(alpha/2))*sd,4)
print ("The confidence interval is between",p-ME,"and",p+ME)
#------------------------------------------------------------------------------------------------
# Number of cookies who clicked the Free Trial Button: Is p_hat within confidence interval range?
clicks_cont = control['Clicks'].sum()
clicks_exp = experiment['Clicks'].sum()
clicks_total = clicks_cont+clicks_exp

p_hat = round(clicks_cont/clicks_total,4)
sd = mt.sqrt(p*(1-p)/clicks_total)
ME = round(get_z_score(1-(alpha/2))*sd,4)
print ("The confidence interval is between",p-ME,"and",p+ME)
#-----------------------------------------------------------------------------------------------
# Click-through-probability of the Free Trial Button: Is d_hat within confidence interval range?
ctp_cont = clicks_cont/pageviews_cont
ctp_exp = clicks_exp/pageviews_exp

d_hat = round(ctp_exp-ctp_cont,4)
p_pooled = clicks_total/pageviews_total
sd_pooled = mt.sqrt(p_pooled*(1-p_pooled)*(1/pageviews_cont+1/pageviews_exp))
ME = round(get_z_score(1-(alpha/2))*sd_pooled,4)
print ("The confidence interval is between",0-ME,"and",0+ME)
#-----------------------------------------------------------------------------------------------
# == Experiment Sizing
#=====================
# Number of total clicks from complete records 
clicks_cont = control["Clicks"].loc[control["Enrollments"].notnull()].sum()
clicks_exp = experiment["Clicks"].loc[experiment["Enrollments"].notnull()].sum()

# Gross Conversion - number of enrollments divided by number of clicks
enrollments_cont = control["Enrollments"].sum()
enrollments_exp = experiment["Enrollments"].sum()

GC_cont = enrollments_cont/clicks_cont
GC_exp = enrollments_exp/clicks_exp
GC_pooled = (enrollments_cont+enrollments_exp)/(clicks_cont+clicks_exp)
GC_sd_pooled = mt.sqrt(GC_pooled*(1-GC_pooled)*(1/clicks_cont+1/clicks_exp))
GC_ME = round(get_z_score(1-alpha/2)*GC_sd_pooled,4)
GC_diff = round(GC_exp-GC_cont,4)

print("The change due to the experiment is",GC_diff*100,"%")
print("Confidence Interval: [",GC_diff-GC_ME,",",GC_diff+GC_ME,"]")
print ("The change is statistically significant if the CI doesn't include 0. In that case, it is practically significant if",-GC["d_min"],"is not in the CI as well.")

# Net Conversion - number of payments divided by number of clicks
payments_cont = control["Payments"].sum()
payments_exp = experiment["Payments"].sum()

NC_cont = payments_cont/clicks_cont
NC_exp = payments_exp/clicks_exp
NC_pooled = (payments_cont+payments_exp)/(clicks_cont+clicks_exp)
NC_sd_pooled = mt.sqrt(NC_pooled*(1-NC_pooled)*(1/clicks_cont+1/clicks_exp))
NC_ME = round(get_z_score(1-alpha/2)*NC_sd_pooled,4)
NC_diff = round(NC_exp-NC_cont,4)

print("The change due to the experiment is",NC_diff*100,"%")
print("Confidence Interval: [",NC_diff-NC_ME,",",NC_diff+NC_ME,"]")
print ("The change is statistically significant if the CI doesn't include 0. In that case, it is practically significant if",NC["d_min"],"is not in the CI as well.")

# == Data Preparation 
# ===================
# Creating the dataset we need for this: starting by merging the two datasets
full = control.join(other=experiment,how="inner",lsuffix="_cont",rsuffix="_exp")
full.count()

# The complete data records
full = full.loc[full["Enrollments_cont"].notnull()]
full.count()

# Deriving a new column for each metric to have it's daily values:
# Gross Conversion
x = full['Enrollments_cont']/full['Clicks_cont']
y = full['Enrollments_exp']/full['Clicks_exp']
full['GC'] = np.where(x<y,1,0)

# Net Conversion
z = full['Payments_cont']/full['Clicks_cont']
w = full['Payments_exp']/full['Clicks_exp']
full['NC'] = np.where(z<w,1,0)
full.head()

GC_x = full.GC[full["GC"]==1].count()
NC_x = full.NC[full["NC"]==1].count()
n = full.NC.count()
print("No. of cases for GC:",GC_x,'\n',
      "No. of cases for NC:",NC_x,'\n',
      "No. of total cases",n)

# == Sign Test
# ============
# Function for calculating probability of x = number of successes
def get_prob(x,n):
    p = round(mt.factorial(n)/(mt.factorial(x)*mt.factorial(n-x))*0.5**x*0.5**(n-x),4)
    return p
# Function to compute the pvalue from probabilities of maximum x
def get_2side_pvalue(x,n):
    p = 0
    for i in range(0,x+1):
        p = p+get_prob(i,n)
    return 2*p

print ("GC Change is significant if",get_2side_pvalue(GC_x,n),"is smaller than 0.05")
print ("NC Change is significant if",get_2side_pvalue(NC_x,n),"is smaller than 0.05")
