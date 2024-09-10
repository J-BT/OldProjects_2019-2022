# PiDart
#### Pi approximation through Monte-Carlos' method:
#### -----------------------------------------------------------------

Through Monte-Carlos' method we can approximate the value of pi according
to the circumference of a circle.

Let's imagine the circle is a darts game's target. The target is surrounded
by a square, with sides lenght equals to the target's diameter.
We try to reach the target throwing darts.

The principle is as follows: 

We throw a large number of darts and we calculate the success ratio using
areas of the target and the square. 
The more darts are thrown the closer we get to pi value.


I used C programming language alonside Python in order to demonstrate their
speed differences.

#### NB: 
For now you can use the API as follows :

`https://pi.pandasprojects.com/api/getPiApproximation/{language}/{throws}`

- You can replace {language} by `python` or `c`
- {throws} must be lower than 10 000 000

for instance:

`https://pi.pandasprojects.com/api/getPiApproximation/c/100000`