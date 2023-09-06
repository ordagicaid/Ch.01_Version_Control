'''
1.0 Jedi Training (17pts)  Name:Aidan Ordagic


1. Define Forking (1pt): 

2. Define Cloning (1pt): 

3. Define Branching (1pt):

4. Define Committing (1pt): 

5. Define Merging (1pt): 

6. Define Pushing (1pt):

7. Define Pull Request (1pt):


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#9a9b9d")
yoda.goto(40, -20)
yoda.goto(0, 0)
yoda.goto(-40, -20)
yoda.goto(-40, -100)
yoda.penup()
yoda.goto(40, -20)
yoda.pendown()
yoda.goto(40, -100)
yoda.penup()
yoda.goto(0, 0)
yoda.pendown()
yoda.goto(0, -70)
yoda.goto(40, -100)
yoda.goto(0, -70)
yoda.goto(-40, -100)
yoda.goto(-40, -20)
yoda.goto(-100, 30)
yoda.goto(-160, -20)
yoda.goto(-160, -90)
yoda.penup()
yoda.goto(0, 0)
yoda.pendown()
yoda.goto(-60, 50)
yoda.goto(-100, 30)
yoda.goto(-160, -20)
yoda.goto(-160, -90)
yoda.goto(-40, -100)
yoda.penup()
yoda.goto(40, -20)
yoda.pendown()
yoda.goto(100, 30)
yoda.goto(160, -20)
yoda.goto(160, -90)
yoda.goto(40, -100)
yoda.goto(40, -20)
yoda.goto(0, 0)
yoda.goto(60, 50)
yoda.goto(100, 30)
yoda.fillcolor("#616265")
yoda.begin_fill()
yoda.goto(60, 50)
yoda.goto(0, 0)
yoda.goto(40, -20)
yoda.end_fill()
yoda.begin_fill()
yoda.goto(40, -100)
yoda.goto(160, -90)
yoda.goto(160, -20)
yoda.goto(100, 30)
yoda.goto(40, -20)
yoda.end_fill()
yoda.begin_fill()
yoda.goto(40, -100)
yoda.goto(40, -20)
yoda.goto(0, 0)
yoda.goto(0, -70)
yoda.goto(40, -100)
yoda.end_fill()
yoda.goto(0, -70)
yoda.fillcolor("#3f3d5c")
yoda.begin_fill()
yoda.goto(-40, -100)
yoda.goto(-40, -20)
yoda.goto(0, 0)
yoda.end_fill()
yoda.begin_fill()
yoda.goto(-60, 50)
yoda.goto(-100, 30)
yoda.goto(-40, -20)
yoda.goto(0, 0)
yoda.end_fill()
yoda.goto(-40, -20)
yoda.begin_fill()
yoda.goto(-100, 30)
yoda.goto(-160, -20)
yoda.goto(-160, -90)
yoda.goto(-40, -100)
yoda.end_fill()


yoda.write('Aidan Ordagic', font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
