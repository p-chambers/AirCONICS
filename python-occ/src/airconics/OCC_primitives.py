# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:31:35 2015

@author: pchambers
"""
import os
import pkg_resources

class airfoil:
    """ Lifting surface section primitive class """

    def __init__(self,
                LeadingEdgePoint,
                ChordLength,
                Rotation=0,
                Twist=0,
                Type='Selig',
                SeligProfile='',
                EnforceSharpTE = False):
        """Class Constructor:
        Parameters
        ----------
        LeadingEdgePoint - array of float (,3)
            (x, y, z) origin of the airfoil LE
            
        ChordLength - 
        
        Rotation - 
        
        Twist - 
        
        Type - 
        
        SeligProfile - string
            Type of airfoil to create:
                - 'Selig' (default) = curve from 'Seligprofile'
                # TODO
                - 'Naca4' = curve from NACA 4 digit profile
                - 'Naca5' = curve from NACA 5 digit profile
        
        EnforceSharpTE - bool
            #TODO
        
        Returns
        -------
        """
        self._LeadingEdgePoint = LeadingEdgePoint
        self._ChordLength = ChordLength
        self._Rotation = Rotation
        self._Twist = Twist
#        self.EnforceSharpTE = EnforceSharpTE
        self._C, self._Chrd = self.make_airfoil(Type)
        return None
        
        def make_airfoil(Type):
            """Selects airfoil 'add' function based on 'type' input
            """
            if Type == 'Selig':
                return AddAirfoilFromSeligFile(SeligProfile)
            elif Type == 'Naca4':
                raise NotImplementedError("Oops, This function is not yet\
                    implemented for Naca 4 digit profiles")
            elif Type == 'Naca5':
                raise NotImplementedError("Oops, This function is not yet\
                    implemented for Naca 5 digit profiles")
            else:
                raise TypeError("Wrong airfoil type: see help(airfoil)")
                
    def _AirfoilPointsSeligFormat(self, SeligProfile):
        """Extracts airfoil coordinates from a file
        
        Assumes input selig files are specified in the Selig format, i.e., 
        header line, followed by x column, z column, from upper trailing edge 
        to lower trailing edge.
        Parameters
        ----------
        FileNameWithPath - string
            
        Returns
        -------
        x - array of float
            x coordinates of airfoil curve
        
        z - array of float
            z coordinates of airfoil curve
        """
        assert(pkg_resources.resource_exists(__name__, SeligProfile)),\
            "Airfoil database for {} not found.".format(SeligProfile)
        
        x, z = pkg_resources.resource_string(__name__, SeligProfile)
        print(x, z)
        return None
#        
#        
#        with open(FileNameWithPath,'r') as f:
#            lines = f.readlines()
#        f.close()
#        x = []
#        z = []
#        for l in lines:
#            try:
#                l = l.split()
#                newx = float(l[0])
#                newz = float(l[1])
#                list.append(x, newx)
#                list.append(z, newz)
#            except:
#                pass
#        return x, z
                
        def AddAirfoilFromSeligFile(self, SeligProfile, Smoothing=1):
            """Adds an airfoil generated by fitting a NURBS curve to a set 
            of points whose coordinates are given in a Selig formatted file
            Parameters
            ----------
            
            Returns
            -------
            
            """
            assert(SeligProfile != ''), "No Selig Profile given (string)"
            x, z = self._AirfoilPointsSeligFormat(SeligProfile)
            C = self._fitAirfoiltoPoints(x, z)
#            if 'Smoothing' in locals():
#                self.SmoothingIterations = Smoothing
#                C, Chrd = self._TransformAirfoil(C)
            return C, Chrd