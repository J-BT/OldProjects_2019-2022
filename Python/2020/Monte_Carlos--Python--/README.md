Pi approximation
through Monte-Carlos' method:
-----------------------------------
(Project realized during my first week's training at digifab school 
in early 2020)

Through Monte-Carlos' method we can approximate the value of pi according
to the circumference of a circle.

Let's imagine the circle is a darts game's target. The target is surrounded
by a square, with sides lenght equals to the target's diameter.
We try to reach the target throwing darts.

- The ones hiting the target are colored in blue
- The ones missing the target are colored in red

The principle is as follows: 

We throw a large number of darts and we calculate the success ratio using
areas of the target and the square. 

The more darts are thrown the closer we get to pi value.

NB: In order to represent the darts game, I used a small module created
by the author of Python Programming: An Introduction to Computer
 Science, 3rd Edition. The module mentioned above, called graphics.py,
is also available at https://mcsp.wartburg.edu/zelle/python/graphics.py
