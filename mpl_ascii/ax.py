# class AxesPlot:
#     def __init__(self, ax, colorbar=None) -> None:
#         self.ax = ax

#     def draw(self, all_plots, axes_height, axes_width, color_to_ascii):
#         return draw_ax(self.ax, all_plots, axes_height, axes_width, color_to_ascii)

def get_xrange(ax):
    x_range = ax.get_xlim()
    if x_range[1] < x_range[0]:
        x_range = x_range[1], x_range[0]
    return x_range

def get_yrange(ax):
    y_range = ax.get_ylim()
    if y_range[1] < y_range[0]:
        y_range = y_range[1], y_range[0]
    return y_range
