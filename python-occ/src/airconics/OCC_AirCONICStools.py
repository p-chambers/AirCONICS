# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:58:52 2015

@author: pchambers
"""
from OCC.BRepBndLib import brepbndlib_Add
from OCC.Bnd import Bnd_Box


def ObjectsExtents(ObjectIds, tol=1e-6, as_vec=False):
    """Compute the extents in the X, Y and Z direction (in the current 
    coordinate system) of the objects listed in the argument.
    
    Parameters
    ----------
    ObjectIds - 
    
    Returns
    -------
    if `as_vec` is True, return a tuple of gp_Vec instances
         for the lower and another for the upper X,Y,Z values representing the
         bounding box

    if `as_vec` is False, return a tuple of lower and then upper X,Y,Z values
         representing the bounding box
    """

    BB = OCC.Bnd_Box()
    BB.SetGap(tol)
    
    for shape in ObjectIds:
        brepbndlib_Add(shape, bbox)
        
    xmin, ymin, zmin, xmax, ymax, zmax = bbox.Get()
    if as_vec is False:
        return xmin, ymin, zmin, xmax, ymax, zmax
    else:
        return gp_Vec(xmin, ymin, zmin), gp_Vec(xmax, ymax, zmax)
    