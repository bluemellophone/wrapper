/*
Source: 
http://nbviewer.ipython.org/github/pv/SciPy-CookBook/blob/master/ipython/Ctypes.ipynb

TO BEGIN:
1.) Search, replace __NAME__ with an all-caps moniker for the alrogithm
    Examples: 'HESAFF', 'RANDOM_FOREST', 'DPM_MKL'

1.) Search, replace __SHORT__ with a lowercase acronym for the alrogithm
    Examples: 'hesaff', 'rf', 'dpm'

2.) Search, replace __CLASS__ with the C++ class for the algorithm you intend
	to wrap.

3.) Include all C++ header files for the algorithm you intend to wrap

4.) Change the wrapper functions for all of the pre-set functions to 
    match the appropriate functions in the algorithm's C++ code
*/

#include <iostream>
#include <fstream>
#include <string>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "py__SHORT__.h"

// Include .h or .hpp C++ headers here

typedef unsigned char uint8;

#ifdef __cplusplus
    extern "C" {
#endif
    #define PYTHON___NAME__ extern DETECTOR_EXPORT

        //=============================
        // Algorithm Constructor
        //=============================
        PYTHON___NAME__ __CLASS__* constructor(
            int     param_int,
            float   param_float,
            bool    param_bool,
            char*	param_char
            )
        {
            __CLASS__* detector = new __CLASS__(
	            param_int,
	            param_float,
	            param_bool,
	          	param_char
            );
            return detector;
        }

        //=============================
        // Train Algorithm with Data
        //=============================
        PYTHON___NAME__ void train(__CLASS__* detector)
        {
            // detector->train();
        }

        //=============================
        // Run Algorithm
        //=============================
        
        PYTHON___NAME__ void detect(__CLASS__* detector)
        {
            // detector->detect();
        }

        PYTHON___NAME__ void segment(__CLASS__* detector)
        {
            // detector->segment();
        }

        //=============================
        // Load / Save Trained Data
        //=============================

        PYTHON___NAME__ int load(__CLASS__* detector)
        {
            // detector->load();
        }

        PYTHON___NAME__ void save(__CLASS__* detector)
        {
            // detector->save();
        }

        //=============================
        // Algorithm-specific Functions
        //=============================

        PYTHON___NAME__ void specific(__CLASS__* detector)
        {
            // pass
        }

#ifdef __cplusplus
    }
#endif
