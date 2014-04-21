/*
	Do not modify this file!
*/
#ifndef DETECTOR_DLL_DEFINES_H
	#define DETECTOR_DLL_DEFINES_H

	#ifdef WIN32
	    #ifndef snprintf
	    	#define snprintf _snprintf
	    #endif
	#endif

	#define DETECTOR_EXPORT
	
	#ifndef FOO_DLL
	    #ifdef DETECTOR_EXPORTS
	        #define DETECTOR_EXPORT __declspec(dllexport)
	    #else
	        //#define DETECTOR_EXPORT __declspec(dllimport)
	    #endif
	#else
		#define DETECTOR_EXPORT
	#endif
#endif
