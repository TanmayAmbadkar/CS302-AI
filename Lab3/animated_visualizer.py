import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animateTSP(history, points):

    key_frames_mult = len(history) // 1500

    fig, ax = plt.subplots()

    line, = plt.plot([], [], lw=2)

    def init():
        x = [points[i][0] for i in history[0]]
        y = [points[i][1] for i in history[0]]
        plt.plot(x, y, 'co')

        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax.set_ylim(min(y) - extra_y, max(y) + extra_y)

        line.set_data([], [])
        return line,

    def update(frame):
        x = [points[i, 0] for i in history[frame] + [history[frame][0]]]
        y = [points[i, 1] for i in history[frame] + [history[frame][0]]]
        line.set_data(x, y)
        return line

    ani = FuncAnimation(fig, update, frames=range(
        0, len(history), key_frames_mult), init_func=init, interval=3, repeat=False)

    plt.show()
