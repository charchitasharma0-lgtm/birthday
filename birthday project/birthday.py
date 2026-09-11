import turtle
import random
import math
 
# ---------- Setup ----------
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#241129")
screen.title("Happy Birthday Cuteii Patuti")
screen.tracer(0)  # manual control of screen updates for smooth animation
 
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("#FFD166")
 
artist = turtle.Turtle()
artist.hideturtle()
artist.speed(0)
artist.penup()
 
confetti_turtles = []
balloon_turtles = []
 
 
# ---------- Helper: draw filled circle ----------
def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
 
 
# ---------- Draw stars in background ----------
def draw_stars():
    star_t = turtle.Turtle()
    star_t.hideturtle()
    star_t.penup()
    star_t.color("white")
    for _ in range(60):
        x = random.randint(-390, 390)
        y = random.randint(-280, 280)
        star_t.goto(x, y)
        size = random.choice([1, 1, 2])
        star_t.dot(size * 2)
 
 
# ---------- Draw the cake ----------
def draw_cake():
    # bottom tier
    artist.color("#FF9EC4")
    artist.goto(-70, -140)
    artist.setheading(0)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(140)
        artist.left(90)
        artist.forward(50)
        artist.left(90)
    artist.end_fill()
 
    # middle tier
    artist.color("#FFD9A0")
    artist.goto(-55, -90)
    artist.setheading(0)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(110)
        artist.left(90)
        artist.forward(35)
        artist.left(90)
    artist.end_fill()
 
    # top tier
    artist.color("#C9A6FF")
    artist.goto(-35, -55)
    artist.setheading(0)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(70)
        artist.left(90)
        artist.forward(30)
        artist.left(90)
    artist.end_fill()
 
    # candle stick
    artist.color("#FFE6C2")
    artist.goto(-3, -25)
    artist.setheading(0)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(6)
        artist.left(90)
        artist.forward(28)
        artist.left(90)
    artist.end_fill()
 
    # sprinkles on bottom tier
    for _ in range(8):
        x = random.randint(-65, 65)
        y = random.randint(-135, -95)
        draw_circle(artist, x, y, 3, "white")
 
 
def draw_flame(offset=0):
    """Flickering flame - offset changes size slightly each frame."""
    artist.color("#FFB84D")
    x, y = 0, 5 + offset
    draw_circle(artist, x, y, 9 + offset * 0.3, "#FFB84D")
    draw_circle(artist, x, y - 2, 4, "#FFF3B0")
 
 
# ---------- Balloons ----------
def make_balloons():
    colors = ["#FF6FA5", "#FFD166", "#C9A6FF", "#FFB88C", "#8FE3CF"]
    xs = [-330, -200, 200, 300, 60]
    for x, c in zip(xs, colors):
        b = turtle.Turtle()
        b.hideturtle()
        b.speed(0)
        b.penup()
        b.shape("circle")
        b.shapesize(2.2, 1.8)
        b.color(c)
        b.goto(x, -320)
        b.showturtle()
        balloon_turtles.append(b)
 
 
def animate_balloons():
    for b in balloon_turtles:
        x, y = b.pos()
        if y < 330:
            b.sety(y + random.uniform(1.5, 2.8))
            b.setx(x + math.sin(y / 30) * 1.2)
        else:
            b.hideturtle()
 
 
# ---------- Confetti ----------
def make_confetti(n=40):
    colors = ["#FF6FA5", "#FFD166", "#C9A6FF", "#FFB88C", "#8FE3CF", "#ffffff"]
    for _ in range(n):
        c = turtle.Turtle()
        c.hideturtle()
        c.speed(0)
        c.penup()
        c.shape("square")
        c.shapesize(0.3, 0.5)
        c.color(random.choice(colors))
        c.goto(random.randint(-390, 390), random.randint(200, 320))
        c.showturtle()
        confetti_turtles.append(c)
 
 
def animate_confetti():
    for c in confetti_turtles:
        x, y = c.pos()
        if y < -300:
            c.goto(random.randint(-390, 390), random.randint(280, 340))
        else:
            c.sety(y - random.uniform(2, 5))
            c.setx(x + math.sin(y / 20) * 2)
        c.right(6)
 
 
# ---------- Text ----------
def draw_text():
    writer.goto(0, 250)
    writer.color("#FFD166")
    writer.write("WISHING YOU A", align="center", font=("Arial", 12, "bold"))
 
    writer.goto(0, 210)
    writer.color("#FF6FA5")
    writer.write("Happy Birthday", align="center", font=("Arial", 32, "bold"))
 
    writer.goto(0, 165)
    writer.color("#C9A6FF")
    writer.write("Cuteii Patuti 🎂", align="center", font=("Arial", 26, "bold"))
 
    writer.goto(0, -190)
    writer.color("#e9d8f0")
    writer.write(
        "Happy Birthday, Cuteii Patuti 🥹💗Stay happy, keep smiling, and always be the amazing person you are. 🎂✨",
        align="center", font=("Arial", 13, "normal"),
    )
 
 
# ---------- Main animation loop ----------
def main():
    draw_stars()
    make_balloons()
    make_confetti(40)
    draw_text()
 
    frame = 0
    while True:
        artist.clear()
        draw_cake()
        flicker = math.sin(frame / 3) * 1.5
        draw_flame(flicker)
 
        animate_balloons()
        animate_confetti()
 
        screen.update()
        frame += 1
 
        # stop after ~20 seconds, click window to exit early / restart
        if frame > 1200:
            break
 
    writer.goto(0, -250)
    writer.color("#FFD166")
    writer.write("Click anywhere to close", align="center", font=("Arial", 10, "italic"))
    screen.exitonclick()
 
 
if __name__ == "__main__":
    main()