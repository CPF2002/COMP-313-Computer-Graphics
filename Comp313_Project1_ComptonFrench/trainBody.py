'''
Student Author Name: Compton French
Group Name: Cool Train
Project 1
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''

import numpy as np
import matplotlib.pyplot as plt

# variables
top = 54  # used to be 59
second_line = 57  # used to be 60.5
third_line = 63  # used to be 64
fourth_line = 65  # used to be 65.5
fifth_line = 67  # used to be 67
ceiling_line = 22  # used to be 26.5
bottom_window = top - 5
window_indent = ceiling_line + 2  # was 28
radius = 2
center_window_curve = bottom_window - radius  # used to be 52.5


def draw_train_body():
    coloring()
    draw_outline()
    draw_innerlines()
    draw_windows()


def draw_outline():
    # main cart
    x = [60, 200, 200, 60, 60]
    y = [4, 4, 70, 70, 4]
    plt.plot(x, y, linewidth=1, color='k')


def draw_innerlines():
    # line separations upper horizontally
    plt.plot([60, 200], [6, 6], linewidth=1, color='k')
    plt.plot([60, 200], [8, 8], linewidth=1, color='k')
    plt.plot([60, 200], [12, 12], linewidth=1, color='k')
    plt.plot([60, 200], [15, 15], linewidth=1, color='k')
    plt.plot([60, 197], [22, 22], linewidth=1, color='k')

    # line separations vertically
    plt.plot([64.5, 64.5], [ceiling_line, 67], linewidth=1, color='k')
    plt.plot([66, 66], [ceiling_line, 67], linewidth=1, color='k')
    plt.plot([67, 67], [ceiling_line, 70], linewidth=1, color='k')

    plt.plot([197, 197], [ceiling_line, 67], linewidth=1, color='k')
    plt.plot([195.5, 195.5], [ceiling_line, 67], linewidth=1, color='k')
    plt.plot([194, 194], [ceiling_line, 67], linewidth=1, color='k')

    plt.plot([163, 163], [ceiling_line, 70], linewidth=1, color='k')
    plt.plot([98.5, 98.5], [ceiling_line, 70], linewidth=1, color='k')

    plt.plot([193, 193], [67, 70], linewidth=1, color='k')

    # lower horizontal section
    plt.plot([60, 64.5], [top, top], linewidth=1, color='k')
    plt.plot([67, 192], [top, top], linewidth=1, color='k')

    plt.plot([60, 64.5], [second_line, second_line], linewidth=1, color='k')
    plt.plot([67, 194], [second_line, second_line], linewidth=1, color='k')
    plt.plot([197, 200], [second_line, second_line], linewidth=1, color='k')

    plt.plot([60, 64.5], [third_line, third_line], linewidth=1.5, color='gold')
    plt.plot([67, 194], [third_line, third_line], linewidth=1.5, color='gold')
    plt.plot([197, 200], [third_line, third_line], linewidth=1.5, color='gold')

    plt.plot([60, 64.5], [fourth_line, fourth_line], linewidth=1.5, color='gold')
    plt.plot([67, 194], [fourth_line, fourth_line], linewidth=1.5, color='gold')
    plt.plot([197, 200], [fourth_line, fourth_line], linewidth=1.5, color='gold')

    plt.plot([60, 200], [fifth_line, fifth_line], linewidth=1.5, color='gold')




def draw_windows():
    # right door
    xrd = [191, 191, 192, 192, 165, 165, 166, 166]
    yd = [ceiling_line, window_indent, window_indent, top, top,
          window_indent, window_indent, ceiling_line]
    plt.plot(xrd, yd, linewidth=1, color='k')
    # left door
    xld = [95.5, 95.5, 96.5, 96.5, 69, 69, 70, 70]
    plt.plot(xld, yd, linewidth=1, color='k')

    # windows
    plt.plot([102.5, 102.5], [window_indent, center_window_curve], linewidth=1, color='k')
    plt.plot([128.75, 128.75], [window_indent, center_window_curve], linewidth=1, color='k')
    plt.plot([132.75, 132.75], [window_indent, center_window_curve], linewidth=1, color='k')
    plt.plot([159, 159], [window_indent, center_window_curve], linewidth=1, color='k')

    plt.plot([104.5, 126.75], [bottom_window, bottom_window], linewidth=1, color='k')
    plt.plot([134.75, 157], [bottom_window, bottom_window], linewidth=1, color='k')

    xllw = [104,  104, 102.5]
    yw = [ceiling_line, window_indent, window_indent]
    plt.plot(xllw, yw, linewidth=1, color='k')

    xlrw = [127.25, 127.25, 128.75]
    plt.plot(xlrw, yw, linewidth=1, color='k')

    xrlw = [134.25, 134.25, 132.75]
    plt.plot(xrlw, yw, linewidth=1, color='k')

    xrrw = [157.5, 157.5, 159]
    plt.plot(xrrw, yw, linewidth=1, color='k')

    # arcs at bottom of window (made function below)
    draw_arc(126.75, center_window_curve, radius, 0, 90)
    draw_arc(157, center_window_curve, radius, 0, 90)
    draw_arc(104.5, center_window_curve, radius, 90, 180)
    draw_arc(134.75, center_window_curve, radius, 90, 180)


def draw_arc(xc, yc, rad, ang1, ang2):
    density = 50
    p1 = ang1 * np.pi / 180
    p2 = ang2 * np.pi / 180
    dp = (p2 - p1) / density
    xlast = xc + rad * np.cos(p1)
    ylast = yc + rad * np.sin(p1)
    for p in np.arange(p1 + dp, p2, dp):
        x = xc + rad * np.cos(p)
        y = yc + rad * np.sin(p)
        plt.plot([xlast, x], [ylast, y], color='black', linewidth=1)
        xlast = x
        ylast = y


def coloring():
    # red background
    plt.fill([60, 60, 200, 200], [ceiling_line, 70, 70, ceiling_line], color='tab:red')

    # yellow layer
    plt.fill([67, 67, 194, 194], [ceiling_line, 60.5, 60.5, ceiling_line], color='gold')

    # blue in windows
    # right door
    xrd = [191, 191, 192, 192, 165, 165, 166, 166]
    yrd = [ceiling_line, window_indent, window_indent, top, top, window_indent, window_indent, ceiling_line]
    plt.fill(xrd, yrd, color='cyan')
    # left door
    xld = [95.5, 95.5, 96.5, 96.5, 69, 69, 70, 70]
    yld = [ceiling_line, window_indent, window_indent, top, top, window_indent, window_indent, ceiling_line]
    plt.fill(xld, yld, color='cyan')
    # windows
    # https://www.statology.org/matplotlib-circle/
    # gca() allows me to not make a new subplot and puts it right on the existing axis
    # using circles to fill in the curves on the window
    c1 = plt.Circle((104.5, center_window_curve), radius=2, alpha=1, color='cyan')
    plt.gca().add_artist(c1)
    c2 = plt.Circle((126.75, center_window_curve), radius=2, alpha=1, color='cyan')
    plt.gca().add_artist(c2)
    c3 = plt.Circle((134.75, center_window_curve), radius=2, alpha=1, color='cyan')
    plt.gca().add_artist(c3)
    c4 = plt.Circle((157, center_window_curve), radius=2, alpha=1, color='cyan')
    plt.gca().add_artist(c4)
    # fill rest of the area
    xlw = [104, 104, 102.5, 102.5, 104.5, 104.5, 126.75, 126.75, 128.75, 128.75, 127.25, 127.25, 104]
    yw = [ceiling_line, window_indent, window_indent, center_window_curve, center_window_curve,
          bottom_window, bottom_window, center_window_curve, center_window_curve, window_indent, window_indent,
          ceiling_line, ceiling_line]
    plt.fill(xlw, yw, color='cyan')
    xrw = [134.25, 134.25, 132.75, 132.75, 134.75, 134.75, 157, 157, 159, 159, 157.5, 157.5, 134.25]
    plt.fill(xrw, yw, color='cyan')

    # top fill white
    plt.fill([60, 200, 200, 60], [4, 4, 22, 22], color='white')

