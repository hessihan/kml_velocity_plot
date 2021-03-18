# convert nmea to csv
# https://stackoverflow.com/questions/65394166/how-to-read-an-nmea-file-with-python
# http://navspark.mybigcommerce.com/content/NMEA_Format_v0.1.pdf

import csv

# adapt this to your file
INPUT_FILENAME = './data/input/original/2021-02-28_16-50-59.nmea'
OUTPUT_FILENAME = './data/input/processed/2021-02-28_16-50-59.csv'

# open the input file in read mode
with open(INPUT_FILENAME, 'r') as input_file:

    # open the output file in write mode
    with open(OUTPUT_FILENAME, 'wt') as output_file:

        # create a csv reader object from the input file (nmea files are basically csv)
        reader = csv.reader(input_file)

        # create a csv writer object for the output file
        writer = csv.writer(output_file, delimiter=',', lineterminator='\n')

        # iterate over all the rows in the nmea file
        for row in reader:

            # write the calculated/formatted values of the row that we just read into the csv file
            writer.writerow(row)