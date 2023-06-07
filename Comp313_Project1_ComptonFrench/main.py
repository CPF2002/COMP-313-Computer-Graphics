'''
Student Author Name: Compton French
Group Name: Cool Train
Project 1
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''


import matplotlib.pyplot as plt
import numpy as np
import trainBody


def main():
    figure, axes = plt.subplots()
    plt.grid(False)
    axes.set_aspect('equal')
    #plt.title('Cool Train')
    plt.axis('off')

    x1 = 0
    x2 = 400
    y1 = 120
    y2 = -30
    plt.axis([x1, x2, y1, y2])

    '''
    # grid
    dx = 5
    dy = -5
    for x in np.arange(x1, x2, dx):
        for y in np.arange(y1, y2, dy):
            plt.scatter(x, y, s=1, color='lightgray')
    '''
    # runs trainBody.py file
    trainBody.draw_train_body()
    # Text group and name
    plt.text(70, 110, "Cool Train, Compton French", fontsize=10)

    plt.show()


main()

