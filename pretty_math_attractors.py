# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:28:39 2021

@author: Angelo Rossi
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter, PillowWriter
from matplotlib.colors import ListedColormap, BoundaryNorm
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from collections import deque

%matplotlib qt
# =============================================================================
interval = 30 # delay between frames [ms]
animation_length = 1 # s
dpi = 200

resolution = 10 # points per frame
sigma = 10
beta = 8/3
rho = 28

line_count = 2
line_length = 100
axes_lims = [(-30, 30), (-30, 30), (-10, 50)]
axis_azimuth_speed = 0.1
axis_elevation_speed = 0.1
linewidth = 0.1
linelength = 100

file_name = r'D://OneDrive/Documents/Python Scripts/lorenz_attractor.mp4'
# =============================================================================
def lorentz(p):
    x, y, z = p
    dxdt = sigma*(y - x)
    dydt = x*(rho - z) - y
    dzdt = x*y - beta*z
    return [x + dxdt*dt,
            y + dydt*dt,
            z + dzdt*dt]

def initial(line_count):
    pis = []
    span = np.linspace(axes_lims[0][0], axes_lims[0][1], line_count)
    for i in span:
        for j in span:
            for k in span:
                pis.append([i, j, k])
    return pis

def trajectory(pi):
    p = pi
    ps = [p]
    for i in range(frames*resolution):
        p = lorentz(p)
        ps += [p]
    return np.array(ps)

def trajectories(pis):
    pss = []
    for pi in pis:
        ps = trajectory(pi)
        pss += [ps]
    return pss
        
def animate(i):
    for ps, line_plot in zip(pss, line_plots):
        xs, ys, zs = ps.T
        xline.append(xs[line_length*resolution])
        yline.append(ys[line_length*resolution])
        zline.append(zs[line_length*resolution])
        print(xline)
        line_plot.set_data(xline, yline)
        line_plot.set_3d_properties(zline)
    ax.view_init(axis_elevation_speed*i, axis_azimuth_speed*i)
    return line_plots 
# ============================================================================
fps = 1/(interval*1e-3)
frames = int(np.floor(fps*animation_length))
dt = 1/(resolution*fps)
pis = initial(line_count)
pss = trajectories(pis)
# ============================================================================

fig = plt.figure(dpi=dpi, figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1], projection='3d')
ax.view_init(0, 0)
ax.set_xlim(axes_lims[0])
ax.set_ylim(axes_lims[1])
ax.set_zlim(axes_lims[2])
ax.set_facecolor('xkcd:black')
line_plots = [ax.plot([], [], [], 'white', linewidth=linewidth)[0] for line in range(line_count)]
ax.axis('off')
# =============================================================================
xline, yline, zline = deque(maxlen=line_length), deque(maxlen=line_length), deque(maxlen=line_length)
anim = FuncAnimation(fig, 
                      animate, 
                      frames=frames, 
                      interval=interval, 
                      blit=True, 
                      repeat=False)
# writervideo = FFMpegWriter(fps=fps) 
# anim.save(file_name, writer=writervideo)

    
