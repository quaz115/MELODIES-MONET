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
            lon0: initial center longitude (float)
            lat0: initial center latitude (float)
            u0: constant eastward center velocity (float)
            v0: constant northward center velocity (float)
            sigma: standard deviation (float)
    returns:
       field (xarray.DataArray) 
    """
    pass
