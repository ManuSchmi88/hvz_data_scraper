from extract_data import *

def main():
    '''
    Created by Manuel Schmid, 12.10.2018

    Calls the hvz-specific functions from the src/extract_data.py file 
    and saves the current gauge-value to a .txt file
    '''

    datafile = get_datafile_from_server()
    split_datafile = load_js_datafile(datafile)
    data_array = js_splitlines(split_datafile)

