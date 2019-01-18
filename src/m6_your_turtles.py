"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Killian Bailey.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
Phillip = rg.SimpleTurtle('turtle')
Phillip.pen=rg.Pen('pink',3)
Phillip.speed=10
size=50
k=20

for k in range (10):
    Phillip.forward(50 + k)
    Phillip.right(90)
    Phillip.forward(50 - k)
    Phillip.draw_circle(size)
import rosegraphics as rg
Alice = rg.SimpleTurtle('turtle')
Alice.pen=rg.Pen('black',8)
Alice.speed=10
size=25
k=20
for k in range (20):
    Alice.forward(25 + k)
    Alice.right(45)
    Alice.forward(25 + k)
    Alice.draw_square(size)
