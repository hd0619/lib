#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import pandas as pd
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame_column_by_index = data_frame.ix[:, [0, 3]]

print data_frame_column_by_index
#data_frame_column_by_index.to_csv(output_file, index=False)
