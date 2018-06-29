# solo
Python module to ensure only a single instance of a program is running. 

## Synopsis

To check for other instances of a python script that is running and stop these other instances (assuming you have privilge of course)

import solo
solo.chk_and_stopall(__file__)

To check for other instances of a python script that is running and stop self (sys.exit(-1)

import solo
solo.chk_and_stopself(__file__)


## Dependencies

Uses psutil which gives cross platform magic 

