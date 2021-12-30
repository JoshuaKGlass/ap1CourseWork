import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Polygon


def calculatepointc(pointA, pointB):
    # a**2 = b**2 + c**2
    # c**2 = a**2 - b**2
    pointC = [np.sqrt(pointA[1] ** 2 - pointB[0] ** 2), pointB[1]]
    print(pointA, pointB, pointC)
    return pointC


def createtriangle(pointA, pointB, pointC):
    print(pointA, pointB, pointC)
    return Polygon(np.array([pointA, pointB, pointC]))


# init values
# x, y
a = [2, 5]
b = [2, 2]
c = calculatepointc(a, b)

# plot triangle
fig, ax = plt.subplots()
tri = createtriangle(a, b, c)
ax.add_patch(tri)
ax.set_xlim(1, 10)
ax.set_ylim(1, 10)

ax.set_xlabel('Base')

axcolor = 'lightgoldenrodyellow'
ax.margins(x=0)

# adjusting the main plot to make space for our sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
xaxis = plt.axes([0.25, 0.1, 0.65, 0.03])
xaxis_slider = Slider(
    ax=xaxis,
    label='Base',
    valmin=b[0],
    valmax=30,
    valinit=c[0],
    # orientation="horizontal" is Default
)

# Make a vertically oriented slider to control the amplitude
yaxis = plt.axes([0.1, 0.25, 0.0225, 0.63])
yaxis_slider = Slider(
    ax=yaxis,
    label="Amplitude",
    valmin=b[1],
    valmax=10,
    valinit=a[1],
    orientation="vertical"
)


# Function to be rendered anytime a slider's value changes
def update(val):
    x = [xaxis_slider.val, c[1]]
    y = [a[0], yaxis_slider.val]
    print(x, b, y)
    # clear previous patch and create new one
    # if i don't remove then there will be loads of triangles
    # on the canvas at one time
    ax.patches.pop()
    ax.add_patch(createtriangle(y, b, x))
    fig.canvas.draw_idle()


# Registering the update function with each slider Update
xaxis_slider.on_changed(update)
yaxis_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset
# the sliders to initial parameters.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    xaxis_slider.reset()
    yaxis_slider.reset()


button.on_clicked(reset)

plt.show()
