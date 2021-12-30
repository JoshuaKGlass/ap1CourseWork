# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
from matplotlib.widgets import Slider, Button



# Create triangulation.
x = np.asarray([5,2, 2])  # x points
y = np.asarray([2,2, 5])  # y points

triang = mtri.Triangulation(x,y, triangles=None)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.triplot(triang, 'bo-', lw=2)
ax.set_title('triplot of Delaunay triangulation')
ax.set_xlim(1, 7)
ax.set_ylim(1, 8)

ax.set_xlabel('Base')

axcolor = 'lightgoldenrodyellow'
ax.margins(x=0)

# adjusting the main plot to make space for our sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Base',
    valmin=0.1,
    valmax=30,
    valinit=0,
)

# Make a vertically oriented slider to control the amplitude
axamp = plt.axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=0,
    orientation="vertical"
)


# Function to be rendered anytime a slider's value changes
# update y
def updateY(val):
    ax.set_ydata()
    fig.canvas.draw_idle()

# Function to be rendered anytime a slider's value changes
# update x
def updateX(val):
    ax.set_xdata()
    fig.canvas.draw_idle()


# Registering the update function with each slider Update
freq_slider.on_changed(updateY)
amp_slider.on_changed(updateX)

# Create a `matplotlib.widgets.Button` to reset
# the sliders to initial parameters.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    freq_slider.reset()
    amp_slider.reset()


button.on_clicked(reset)


plt.show()
