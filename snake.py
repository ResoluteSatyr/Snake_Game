from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # For loop iterates through list (we add -1 because range starts at zero and len starts at 1)
        """We are adjusting the animation so that all snake blocks move together as one"""
        #                              Start↓,   Stop↓, Step↓
        for seg_num in range(len(self.segments) - 1, 0, -1):
            """ Takes the coordinates of the second to last item"""
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            """ Adds the second to last item coordinates values to the last item in the list"""
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Sets turtle head to the UP position unless turtle is facing DOWN"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Sets turtle head to the DOWN position unless turtle is facing UP"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Sets turtle head to the LEFT position unless turtle is facing RIGHT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Sets turtle head to the RIGHT position unless turtle is facing LEFT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
