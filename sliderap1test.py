import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Polygon

# The parametrized function to be plotted
# a = alt, b = base, c = hyp

a = [2, 5]
b = [2, 2]
c = [np.sqrt(5 ** 2 - 2 ** 2), 2]
# pts = np.array([a, b, [np.sqrt(5 ** 2 - 2 ** 2), 2]])
#
# p = Polygon(pts, closed=False)
#
# ax = plt.gca()
# ax.add_patch(p)
#
# ax.set_xlim(1, 7)
# ax.set_ylim(1, 8)
# print(a, b, c)

# Defining the initial parameters
init_alt = 5
init_base = 3

print(a, b, c)

# plot triangle based on c
# Creating the figure and the graph line that we will update
fig, ax = plt.subplots()
pts = np.array([a, b, c])
p = Polygon(pts, closed=False)
ax.add_patch(p)
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
    valinit=b[1],
)

# Make a vertically oriented slider to control the amplitude
axamp = plt.axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=a[1],
    orientation="vertical"
)


# Function to be rendered anytime a slider's value changes
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()


# Registering the update function with each slider Update
freq_slider.on_changed(update)
amp_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset
# the sliders to initial parameters.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    freq_slider.reset()
    amp_slider.reset()


button.on_clicked(reset)

plt.show()
