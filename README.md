# A/B-Testing Project Instructions:
This program provides a walkthrough of the A/B testing course's final project provided by an online learning platform named Udacity. 
The primary goal of Udacity is to decrease early cancellation to improve the overall student experience and coaches' capacity to support students who are likely to complete the course.


#### Experiment Overview: Free Trial Screener
At the time of this experiment, Udacity courses currently have two options on the course overview page: start free trial, and access course materials.

- If the student clicks start free trial, they will be asked to enter their credit card information, and then they will be enrolled in a free trial for the paid version of the course. After 14 days, they will automatically be charged unless they cancel first.

- If the student clicks access course materials, they will be able to view the videos and take the quizzes for free, but they will not receive coaching support or a verified certificate, and they will not submit their final project for feedback.

#### Experiment Description
In the experiment, Udacity tested a change where if the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated 5 or more hours per week, they would be taken through the checkout process as usual. If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity courses usually require a greater time commitment for successful completion, and suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead. This screenshot shows what the experiment looks like.


#### Null Hypothesis
This approach might not make a significant change and might not be effective in reducing the early Udacity course cancellation.

#### Alternative Hypothesis
This might reduce the number of frustrated students who left the free trial because they didn’t have enough time, without significantly reducing the number of students to continue past the free trial and eventually complete the course.

#### Pre-experiment Analysis
We need to perform a pre-experiment analysis before running the experiment:

- Choosing the unit of diversion
- Choosing metrics
- Calculating the required sample size

#### Unit of diversion
The unit of diversion is a cookie, although if the student enrolls in the free trial, they are tracked by user-id from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.

#### Metric Choices: Invariant/Evaluation

##### Invariant metrics
Invariant metrics are the ones used for sanity checks and will remain invariant throughout the experiment.

- Number of cookies: The number of unique cookies to view the course overview page. (dmin=3000)
- Number of clicks: The number of unique cookies to click the “Start free trial” button (which happens before the free trial screener is a trigger).(dmin=240)
- Click-through-probability: The number of unique cookies to click the “Start free trial” button divided by number of unique cookies to view the course overview page.(dmin=0.01)

##### Evaluation Metrics
Evaluation metrics are the ones that we care about, the metrics that must be observed for consideration in the decision to launch the experiment.

- Gross conversion: The number of user-ids to complete checkout and enroll in the free trial divided by the number of unique cookies to click the “Start free trial” button. (dmin= 0.01)
- Retention: The number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by number of user-ids to complete checkout. (dmin=0.01)
- Net conversion: The number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by the number of unique cookies to click the “Start free trial” button. (dmin= 0.0075)

#### Experiment Sizing
Given α=0.05 (significance level ) and β=0.2, we want to estimate how many pageviews total we need to collect in the experiment. This amount will be divided into two groups: control and experiment.

#### Calculate Sample Size per Metric
Calculate the number of samples required for the experiment per metric. 