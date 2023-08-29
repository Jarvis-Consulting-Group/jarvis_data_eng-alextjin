import pandas as pd
import os
import sys

def find_members_by_city(input_file, city_name,  output_file):
 df = pd.read_csv(input_file)
 result = df[df.address.str.contains(city_name, case=False)]
 result.to_json(output_file)

find_members_by_city(sys.argv[1], sys.argv[2], sys.argv[3])
