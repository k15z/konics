import numpy as np
from ..core import World
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def make_preview(track, world=None, title=None):
    fig = Figure()
    if title: fig.suptitle(title)

    canvas = FigureCanvas(fig)
    ax = fig.gca()

    ts = np.linspace(0.0, track.e_t, num=1000)
    x = [track.x_t(t) for t in ts]
    y = [track.y_t(t) for t in ts]
    ax.plot(x, y)

    if not world: world = World()
    track.add_to(world)
    x = [x for x, y, a in world.cones]
    y = [y for x, y, a in world.cones]
    ax.scatter(x, y)

    canvas.draw()
    image = np.fromstring(canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(canvas.get_width_height()[::-1] + (3,))
    return image
