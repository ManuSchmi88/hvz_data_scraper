"""
Set of functions to extract valuable datapoints from the hvz_peg_stm.js file
"""

import os
import shutil

def load_js_datafile(filename):
    """
    Opens op the .js datafile for post-processing
    """
    file_object = open(filename, 'r')
    
    file_object_split = file_object.read().splitlines()
    
    return file_object_split

def js_splitlines(data_object):
    """
    Splits the lines of the file_object for each , to create array with each index beeing a different river
    """
    
    river_array = [lines.split(',') for lines in data_object]
    
    return river_array

def extract_time_kill_header(processed_data_object):
    """
    Get the time of data-extractiond and then kill the header of the file.
    Maybe unnecessary, also maybe a bad idea. I need to check if the HVZ changes
    the format of the file from time to time...
    
    Right now, header is always 5 lines long. 
    """
    
    extraction_time = processed_data_object[0][1].strip()
    list_without_header = processed_data_object[6:]
    
    return extraction_time, list_without_header
    