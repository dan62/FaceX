import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function that converts 2D image to 3D model
def from2D(image_file):
    print('converting 2D images to 3D')
    img = plt.imread(image_file)

    # Define a grid matching the map size, subsample along with pixels
    theta = np.linspace(0, np.pi, img.shape[0])
    phi = np.linspace(0, 2*np.pi, img.shape[1])

    count = 180 # keep 180 points along theta and phi
    theta_inds = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
    phi_inds = np.linspace(0, img.shape[1] - 1, count).round().astype(int)
    theta = theta[theta_inds]
    phi = phi[phi_inds]
    img = img[np.ix_(theta_inds, phi_inds)]

    theta,phi = np.meshgrid(theta, phi)
    R = 1

    # sphere
    #x = R * np.sin(theta) * np.cos(phi)
    x = R * np.cos(phi) * 1.2 * 100
    y = R * np.sin(theta) * np.sin(phi) * 100
    z = R * np.cos(theta) *100

    # create 3d Axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1) # we've already pruned ourselves

    # make the plot more spherical
    ax.axis('off')
    ax.axis('scaled')
    #ax.set_facecolor((1.0, 0.47, 0.42))
