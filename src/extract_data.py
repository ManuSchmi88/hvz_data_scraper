"""
Set of functions to extract valuable datapoints from the hvz_peg_stm.js file
"""

import os
import shutil
import urllib.request
import datetime

def get_datafile_from_server():
    """
    downloads the newest datafile from the hvz_page
    """
    print('Beginning file download.')
    
    current_time = str(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M'))
    
    url  = 'https://www.hvz.baden-wuerttemberg.de/js/hvz_peg_stm.js'
    save_path = '../js_basefiles/js_files/'
    filename  = 'hvz_peg_stm' + current_time + '.js'
    complete_save_path = save_path + filename
    
    urllib.request.urlretrieve(url, complete_save_path)
    
    print('finished downloading. file saved to: ' + filename)
    
    return complete_save_path


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