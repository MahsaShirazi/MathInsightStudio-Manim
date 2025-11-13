from manim import *
import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
from utils import set_zoom

# Define the Lorenz system of differential equations

def lorenz_system(t, state, sigma=10, rho=28, beta=8/3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt])

def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, time),
        y0=state0,
        t_eval = np.arange(0, time, dt)
    )
    return solution.y.T

class LorenzAttractor(ThreeDScene):
    def construct(self):
        # Print which renderer is being used
        print(f"Using renderer: {config.renderer}")
        # give the camera a 3D angle
        self.set_camera_orientation(phi=76*DEGREES, theta=35*DEGREES)

        # Set zoom depending on renderer
        set_zoom(self, 0.7)

        #set up axes
        axes = ThreeDAxes(
            x_range = (-50, 50, 5),
            y_range = (-50, 50, 5),
            z_range = (-30, 50, 5),
            x_length = 16,
            y_length = 16,
            z_length =10,
        )
        axes.set_width(config.frame_width)
        axes.center()
        self.add(axes)

        #initial state - good starting point for Lorenz attractor
        state0 = np.array([10,10,10])
        points = ode_solution_points(lorenz_system, state0, time=10, dt=0.01)  # increased time to see more of the attractor
        curve = VMobject().set_points_as_corners([axes.c2p(*point) for point in points])
        self.add(curve)