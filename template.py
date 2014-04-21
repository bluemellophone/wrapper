#!/usr/bin/env python

'''

TO BEGIN:
0.) Get Python modules at: https://github.com/bluemellophone/modules

1.) Search, replace __NAME__ with an all-caps moniker for the alrogithm
    Examples: 'HESAFF', '__NAME__', 'DPM_MKL'

2.) Search, replace __SHORT__ with a lowercase acronym for the alrogithm
    Examples: 'hesaff', 'rf', 'dpm'

3.) Search, replace __LIBRARY__ with the C++ class for the algorithm you intend
	to wrap.

4.) Search, rpelace __DIRECTORY__ with the directory of the build script

5.) Change the wrapper functions for all of the pre-set functions to 
    match the appropriate functions in the C-Types C wapper code

6.) Rename all template files py__SHORT__.extension (.py, .h, .cpp)

'''

from __future__ import print_function, division
# Standard
from os.path import realpath, dirname
from ordereddict import OrderedDict as odict
import ctypes_interface
import ctypes as C
# Scientific
import numpy as np
import cv2
from PIL import Image
import os
import sys
import time
import threading
from directory import Directory

__VERBOSE__ = True

#============================
# CTypes Interface Data Types
#============================

# Bindings for Numpy Arrays
FLAGS_RW = 'aligned, c_contiguous, writeable'
CNPFLOAT = np.ctypeslib.ndpointer(dtype=np.float32, ndim=2, flags=FLAGS_RW)
CNPINT   = np.ctypeslib.ndpointer(dtype=np.uint8,   ndim=2, flags=FLAGS_RW)

# Bindings for C Variable Types
COBJ	 = C.c_void_p
CCHAR	= C.c_char_p
CINT	 = C.c_int
CBOOL	= C.c_bool
CFLOAT   = C.c_float

#=================================
# Default / Constructor Parameters
#=================================
'''
	This defines the default constructor parameters for the algorithm. 
	These values may be overwritten by passing in a dictionary to the 
	class constructor using kwargs

	constructor_parameters = [
		(parameter type, parameter name, parameter default value),	
	]

	IMPORTANT: 
	The order of this list must match the C++ constructor parameter order
'''
constructor_parameters = [	
	(CINT,  	'param_int',	1),   
	(CFLOAT, 	'param_float'	1.0)
	(CBOOL, 	'param_bool',	True),   
	(CCHAR, 	'param_char',	'1'),
]

# Do not touch
PARAM_ODICT = odict([(key, val) for (_type, key, val) in constructor_parameters])
PARAM_TYPES = [_type for (_type, key, val) in constructor_parameters]

#============================
# Python Interface
#============================

def _build_shared_c_library(rebuild=False):
	os.system("cd __DIRECTORY__")
	if rebuild:
		os.system("rm -rf build")

	retVal = os.system("./build_template_unix.sh")

	if retVal != 0:
		print("*" * 45)
		print("C Shared Library failed to compile")
		sys.exit(0)

	print("C Shared Library built")


class __NAME___Detector(object):

	#=============================
	# Algorithm Constructor
	#=============================
	def __init__(__SHORT__, libname='__LIBRARY__', **kwargs):
		'''
		Loads the compiled lib and defines its functions
		'''
		root_dir = realpath(dirname(__file__))
		__SHORT__.CLIB, LOAD_FUNCTION = ctypes_interface.load_clib(libname, root_dir)
		
		'''
		def_lib_func is used to expose the Python bindings that are declared
		inside the .cpp files to the Python clib object.

		def_lib_func(return type, function name, list of parameter types)

		IMPORTANT:
		For functions that return void, use Python None as the return value.
		For functions that take no parameters, use the Python empty list [].
		'''
		LOAD_FUNCTION(COBJ, 'constructor',  PARAM_TYPES)
		LOAD_FUNCTION(None, 'train',		[COBJ])
		LOAD_FUNCTION(None, 'detect',	   	[COBJ])
		LOAD_FUNCTION(None, 'segment',	  	[COBJ])
		LOAD_FUNCTION(CINT, 'load',		 	[COBJ])
		LOAD_FUNCTION(None, 'save',		 	[COBJ])
		# Add any algorithm-specific functions here

		'''
		Create the C object using the default parameter values and any updated
		parameter values from kwargs
		'''
		_PARAM_ODICT = PARAM_ODICT.copy()
		_PARAM_ODICT.update(kwargs)

		if __VERBOSE__:
			print('[__SHORT__] New __NAME__ Object Created')
			print('[__SHORT__] Algorithm Settings=%r' % (_PARAM_ODICT,))
		
		PARAM_VALUES = _PARAM_ODICT.values() # pass all parameters to the C constructor
		__SHORT__.detector = __SHORT__.CLIB.constructor(*PARAM_VALUES)

	def _run(__SHORT__, target, args):
		t = threading.Thread(target=target, args=args)
		t.daemon = True
		t.start()
		while t.is_alive(): # wait for the thread to exit
			t.join(.1)

	#=============================
	# Train Algorithm with Data
	#=============================

	def train(__SHORT__):
		__SHORT__._run(__SHORT__.CLIB.train, [__SHORT__.detector])

	def retrain(__SHORT__):
		__SHORT__._run(__SHORT__.CLIB.retrain, [__SHORT__.detector])

	#=============================
	# Run Algorithm
	#=============================
	
	def detect(__SHORT__):
		__SHORT__._run(__SHORT__.CLIB.detect, [__SHORT__.detector])

	def segment(__SHORT__):
		__SHORT__._run(__SHORT__.CLIB.segment, [__SHORT__.detector])

	#=============================
	# Load / Save Trained Data
	#=============================

	def load(__SHORT__):
		__SHORT__.CLIB.load(__SHORT__.detector) # for functions that return, call directly

	def save(__SHORT__):
		__SHORT__._run(__SHORT__.CLIB.save, [__SHORT__.detector])

	#=============================
	# Algorithm-specific Functions
	#=============================

	def specific(__SHORT__):
		__SHORT__._run(__SHORT__.CLIB.specific, [__SHORT__.detector])


if __name__ == '__main__':

	_build_shared_c_library(rebuild=False)
	print("[Testing __NAME__]")

	# Add test code for the class
	