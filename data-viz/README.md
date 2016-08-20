# Summary
This chart shows how NBA Hall of Fame players and the 2016 NBA All-Stars have
progressed over their careers. It shows all-time leaders in each statistical
category. The chart shows which 2016 All-Stars are on pace to become all-time
leaders and/or future Hall of Famers. The chart can be viewed [here](https://wjenkins3.github.io/udacity-nanodegree/data-viz/).

# Design 
Initial design:

- I wanted to show how the all-stars have progressed over the years in comparison
to the Hall of Famers so I changed their color so they would stick out. Now you can
distinguish which active players could go on to become future Hall of Famers.

- In a straight on viewing of the chart, the line plots were clustered around years
1-5. Some of the all-stars have only been in the NBA for five years. I changed the
perspective so that every player can be singled out and compared to the rest of the
plotted lines.

- In the perspective view, the vertical axis was placed in the back of the chart so the
statistical leaders set the baseline viewing of line plots. The 20-year careers set the
bar and the other players can be compared to it.

- Animation was added to the changing of the different viewing selections to make it
obvious the data being view was changing and the change was taking effect.

- Highlighting was added to a selected player to distinguish its plot from the rest of the chart.

After Feedback #1:

It was too difficult to single out a single player for comparing to other players. The
names were too small to see and it was difficult making a player selection.

- To the make the names easier to read and the comparison easier, the chart was changed
from line plots to a resemblance of stacked bar graphs. The change also makes it easier to place the
totals for each player on the y-axis.

- The font size of the player names was also increased.

- For comparison of a players progress over a career, clicking on a player name will show
the line plot of the player's stats. Up to 6 players can be selected for comparison.

After Feedback #2:

Some players stand out for the different statistics, so that's good. The
names can still be hard to see and single out, but sometimes the data points
are really that close together. The following changes help to alleviate some of the
difficulty and possibly enhance the experience:

- The chart was made responsive to the viewport. The scale on the y-axis will spread out
and so the names will not lay on top of each other.

- The summary paragraph becomes a modal box when the screen size is small, giving more
real estate to the chart. Now it fades out when the screen size is below the threshold.

- The names were spaced out a bit from their line markers. This was causing the text to
appear smaller when the all-stars were filtered out.

- Removed the bugs in the player selection and highlighting

# Feedback
Feedback received from others on the visualization:

### Feedback #1
It's not clear what interactive functionality is included with the chart. For instance, I
did not know you could click on the player names for a summary of the player stats. The
player names are too small to see, and it is difficult distinguishing an individual
player's line. Also the Sort by options do not appear on the same line (in Internet
Explorer).

### Feedback #2
First of all, I really like watching the transitions. Second, Kobe!!!! And wow at Steph
Curry and the 3FGs. However, the names are too close together. You cannot always see who
is who. Also when the All-Stars are filtered out, the names look like they are getting
smaller. They were already hard to see. Lastly, something weird is happening with the
selections and the players being displayed; I can't quite explain it.

# Resources
Inspiration: "UK Temperature History" by Peter Cook
(http://charts.animateddata.co.uk/uktemperaturelines/)

Data was compiled from these two sources: http://www.databasebasketball.com/ and
http://www.basketball-reference.com/
