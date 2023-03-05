import pandas as pd

from parameters.parameters import energy_file_path
from parameters.parameters import insurance_file_path


def get_data(f):
    
    """This is a function that takes a file path and 
    reads in data with pandas
    : f: filepath
    : df: resulting data
    """

    df = pd.read_csv(f)

    return df