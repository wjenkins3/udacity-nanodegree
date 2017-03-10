# Summary
This chart shows how NBA Hall of Fame players and the 2016 NBA All-Stars have
progressed over their careers. It shows all-time leaders in each statistical
category. The chart shows which 2016 All-Stars are on pace to become all-time
leaders and/or future Hall of Famers. There are current All-Stars that already outperform
previous Hall of Famers. The chart can be viewed
[here](https://wjenkins3.github.io/udacity-nanodegree/P6%20-%20Make%20Effective%20Data%20Visualization/).

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

End Result:
1. Multi-series line plot (statistic totals vs career-year)
2. Color encodings for player type (blue for All-Stars, black for Hall of Famers)
3. Changeable y-axis plots and scales

<img src="https://github.com/wjenkins3/udacity-nanodegree/raw/master/P6%20-%20Make%20Effective%20Data%20Visualization/images/initial.png" width="800" height="500">

After Feedback #1:

It was too difficult to single out a single player for comparing to other players. The
names were too small to see and it was difficult making a player selection.

- To the make the names easier to read and the comparison easier, the chart was changed
from line plots to a resemblance of stacked bar graphs. The change also makes it easier to place the
totals for each player on the y-axis.

- The font size of the player names was also increased.

- For comparison of a players progress over a career, clicking on a player name will show
the line plot of the player's stats. Up to 6 players can be selected for comparison.

End Result (differences): 
1. Bar chart (replaces multi-series line plot)
2. Player selection displays line plot showing career progression
3. Color encodings for player selections (up to six)

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

After Feedback #3:

- Changed the color of the bars

- Removed the blue and white lines under the names (they didn't add any value)

End Result (differences):
1. Contrasting colors for bars and display names

<img src="https://github.com/wjenkins3/udacity-nanodegree/raw/master/P6%20-%20Make%20Effective%20Data%20Visualization/images/after3.png" width="800" height="500">

After Feedback #4:
Overlapping names are still a problem so the bars will be removed and points will be placed next to the names.

End Result (differences):
1. Scatterplot for players' statistics (replaces bar chart)
2. Names that overlap have been removed
3. The points are clickable and hovering over the dots displays the name


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

### Feedback #3
I notice the relationship between players, the relationship between Hall of Famers and
potential future Hall of Famers. Barring injury or any other unforeseen circumstances the
blue names at the top of the bars should go on to become Hall of Famers. The chart does
show how the players progressed over the years. I like the transitions. One little
critique, though: the blue names on top of the blue bars can make it a little difficult to see.

### Feedback #4
While exploring the different statistics, I noticed that some of the player names overlap.
This makes it difficult to see and click on the right player for comparison. I get the
feeling that this might be somewhat difficult to change but this really hinders the
visualization. In some cases, the player names overlap to the point that neither is
readable.

# Resources
Inspiration: "UK Temperature History" by Peter Cook
(http://charts.animateddata.co.uk/uktemperaturelines/)

Data was compiled from these two sources: http://www.databasebasketball.com/ and
http://www.basketball-reference.com/
