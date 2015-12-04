# airconics_setup.py Setup file: here you can specify top level system variables 
# ==============================================================================
# AirCONICS
# Aircraft CONfiguration through Integrated Cross-disciplinary Scripting 
# version 0.2.1
# Andras Sobester, 2015.
# Bug reports to a.sobester@soton.ac.uk or @ASobester please.
# ==============================================================================
import sys
import os
import urllib

# *** There are NO entries to edit here ***

# Check if using unix style system or windows:
#   RhinoVerison = 1 for windows
#   RhinoVersion = 2 for mac
if os.name in ['posix','mac']:
	RhinoVersion = 2
elif os.name == 'nt':
	RhinoVersion = 1

# This line should produce the string name of the Airconics path - this will
# be added to the python path when this setup file is run
AirCONICSpath = os.path.dirname(__file__)

# The line below should produce the path to your library of Selig-formatted
# airfoils. When this setup script is run, it will check if the directory
# exists and then download from source:
# NOTE: If you are having trouble here, the source url may be deprecated. 
SeligPath = os.path.join(AirCONICSpath + 'coord_seligFmt')    



# ==============================================================================
print "System variables initialised."
if AirCONICSpath not in sys.path:
	sys.path.append(AirCONICSpath)
