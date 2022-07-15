import math
import numpy as np
import scipy as sp
import xarray as xr

def gaussian_plume_2d(lon_da, lat_da, time_da, params):
    """
    arguments:
        xarray.DataArray lon_da: longitude array
        xarray.DataArray lat_da: latitude array
        xarray.DataArray time_da: datetime array
        dictionary params: Gaussian distribution parameters
            float lon_0: initial center longitude
            float lat_0: initial center latitude
            float u_0: constant eastward center velocity
            float v_0: constant northward center velocity
            float sigma: standard deviation
    returns:
        xarray.DataArray
    """

    # nominal Earth equatorial radius (meter)
    R_earth = 6378100.0

    # spherical coordinates of initial center position
    theta_0 = np.pi * (1 - params['lat_0'] / 180)
    phi_0 = np.pi * params['lon_0'] / 180

    # unit vectors
    e_x = np.array([1.0, 0, 0])
    e_y = np.array([0, 1.0, 0])
    e_z = np.array([0, 0, 1.0])

    # unit vectors at initial center position
    e_rho   =   np.cos(phi_0) * e_x + np.sin(phi_0) * e_y
    e_phi   = - np.sin(phi_0) * e_x + np.cos(phi_0) * e_y
    e_r     = np.sin(theta_0) * e_rho + np.cos(theta_0) * e_z
    e_theta = np.cos(theta_0) * e_rho - np.sin(theta_0) * e_z

    # velocity vector of plume center
    V = params['u_0'] * e_phi - params['v_0'] * e_theta
    V_norm = np.sqrt(np.dot(V, V))
    # unit vector in direction of velocity vector
    V_0 = V / V_norm
    # angular velocity along trajectory
    omega = V_norm / R_earth

    # great circle X(t) = cos(omega t) X_0 + sin(omega t) V_0
