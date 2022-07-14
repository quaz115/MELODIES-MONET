import math
import numpy as np
import scipy as sp
import xarray as xr

def gaussian_plume_2d(lon_da, lat_da, time_da, params):
    """
    arguments:
        lon_da: longitude array (xarray.DataArray)
        lat_da: latitude array (xarray.DataArray)
        time_da: datetime array (xarray.DataArray)
        params: Gaussian distribution parameters (dictionary)
            lon_0: initial center longitude (float, degrees East)
            lat_0: initial center latitude (float, degrees North)
            u_0: constant eastward center velocity (float)
            v_0: constant northward center velocity (float)
            sigma: standard deviation (float)
    returns:
        field (xarray.DataArray)
    """

    # great circle X(t) = cos(omega t) X_0 + sin(omega t) V_0

    theta_0 = np.pi * (1 - params['lat_0'] / 180)
    phi_0 = np.pi * params['lon_0'] / 180
    X_0 = np.array([np.sin(theta_0) * np.cos(phi_0),
                    np.sin(theta_0) * np.sin(phi_0),
                    np.cos(theta_0)])
