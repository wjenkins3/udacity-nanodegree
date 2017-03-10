# Test a Perceptual Phenomenon

## Statistics: The Science of Decisions Project

### Background Information

In a Stroop task, participants are presented with a list of words, with each word displayed in a
color of ink. The participant’s task is to say out loud the color of the ink in which the word is
printed. The task has two conditions: a congruent words condition, and an incongruent words
condition. In the congruent words condition, the words being displayed are color words whose
names match the colors in which they are printed **(a)**. In the incongruent words condition, the words displayed are color words whose names do not match the colors in
which they are printed **(b)**. In each case, we measure the time it takes to name the ink colors in equally­sized lists. Each participant will go through and record a
time from each condition.<br/><br/>
**(a)**<img src="https://github.com/wjenkins3/udacity-nanodegree/raw/master/P1/images/stroopa.gif" height="150" width="350">
**(b)**<img src="https://github.com/wjenkins3/udacity-nanodegree/raw/master/P1/images/stroopb.gif" height="150" width="350">

Data: [View CSV](https://drive.google.com/file/d/0B9Yf01UaIbUgQXpYb2NhZ29yX1U/view?usp%3Dsharing&sa=D&ust=1472584192608000&usg=AFQjCNEOK0r3Z3Nx5nZgDecW7514UX07vw)

### Stroop Effect Investigation
1. Our independent variable is the task word congruency condition; there are two conditions: a
congruent words condition and an incongruent words condition. Our dependent variable is the time
it takes to name the ink colors in the Stroop task.

2. The null hypothesis is completing the Stroop task will not take a longer time in the incongruent
words condition than in the congruent words condition and may actually take less time. The
alternative hypothesis is completing the Stroop task takes a longer time in the incongruent words
condition than in the congruent words condition.<br/>
H<sub>0</sub> : &mu;<sub>I</sub> &le; &mu;<sub>C</sub><br/>
H<sub>A</sub> : &mu;<sub>I</sub> > &mu;<sub>C</sub><br/>
&mu;<sub>C</sub>, mean time the task takes with congruent words<br/>
&mu;<sub>I</sub>, mean time the task takes with incongruent words<br/>

  We only have a sample of the population and the results of their participation in the Stroop task. We
  do not know the population mean or standard deviation. Each participant performs the same task
  with two different conditions. This is a repeated measures test where the measured times from each
  condition and task combination are being compared. And according to Wikipedia, "when the name
  of a color...is printed in a color not denoted by the name..., naming the color of the word takes longer
  and is more prone to errors than when the color of the ink matches the name of the color." Therefore we
  will use a one-tailed, dependent samples t-test.

3. We have a sample of 24 participants. The mean time it took to complete the task with the congruent
condition was 14.05 seconds with sample standard deviation of 3.56. The mean time it took to
complete the task with the incongruent condition was 22.02 seconds with standard deviation of
4.80. The mean time difference between the incongruent and congruent condition task times is 7.96
seconds with standard deviation of 4.86.<br/><br/>
x&#772;<sub>C</sub> = 14.05, s<sub>C</sub> = 3.56<br/>
x&#772;<sub>I</sub> = 22.02, s<sub>I</sub> = 4.80<br/>
x&#772;<sub>D</sub> = 7.96, s<sub>D</sub> = 4.86<br/>

4. In Figure 1 and Figure 2, we can see that for each condition there is a normal sample distribution of
the times it takes to complete the task.

  <img src="https://github.com/wjenkins3/udacity-nanodegree/raw/master/P1/images/image01.png">
  <br/>
  Figure 1. Frequency of task times with the congruent words condition  
  <img src="https://github.com/wjenkins3/udacity-nanodegree/raw/master/P1/images/image02.png">
  <br/>
  Figure 2. Frequency of task times with the incongruent condition
  
5. Reminder of our hypotheses:<br/>
H<sub>0</sub> : &mu;<sub>I</sub> &le; &mu;<sub>C</sub><br/>
H<sub>A</sub> : &mu;<sub>I</sub> > &mu;<sub>C</sub><br/>
&mu;<sub>C</sub>, mean time the task takes with congruent words<br/>
&mu;<sub>I</sub>, mean time the task takes with incongruent words<br/>
x&#772;<sub>D</sub> = 7.96, s<sub>D</sub> = 4.86<br/>
SE = 0.99<br/>
t<sub>critical</sub>(23) = 2.5, &alpha; = .01, one-tailed<br/>
t(23) = 8.02, p < .0001, one-tailed<br/><br/>
At &alpha; = .01, we reject the null hypothesis. As expected, the Stroop task takes a significantly longer
time with words in the incongruent condition with p < .0001. It does take longer to name the color
of the ink in which color words are printed when the names and colors do not match.<br/><br/>
Confidence interval on the mean difference, or additional time it takes to complete the task with the
incongruent condition (in seconds); 99% CI = (5.18,10.75)

6. Cohen's d = 1.64<br/>
r<sup>2</sup> = 0.74<br/>
We can attribute 74% of the effects to the incongruent words condition. Other reasons for the
effects observed could possibly be attributed to the task order influences and/or carry-over effects
from the initial part of the experiment. When I participated in the second part of the Stroop task, my
brain was primed with colors I expected to see from the first part. The order of the tasks performed
could attribute to the differences in the times. An alternative task would be to perform the Stroop
task in the opposite order, i.e. with the incongruent condition task followed by the congruent
condition task.

### Resources
Stroop effect. (2015, October 16). In Wikipedia, The Free Encyclopedia. Retrieved 15:26, November 2,
2015, from <https://en.wikipedia.org/w/index.php?title=Stroop_effect&oldid=686068625>

