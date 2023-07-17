import pandas as pd
import os
import sys

def csv_2_json(input_file, output_file):
 print('Start ingesting file below file: {}/{} \n'.format(os.getcwd(), input_file))
 df = pd.read_csv(input_file)
 print('File ingested, please find below for details. Transformation is gettingn started/')
 df.info()
 df.to_json(path_or_buf=output_file)
 print('Transformation completed, json file is exported in below path: \n {}/{}'.format(os.getcwd(), output_file))
csv_2_json(sys.argv[1], sys.argv[2])
