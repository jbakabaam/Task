# Usage: python script.py input.txt output.pickle
# For: chr1~chr22

import argparse
import pickle

class DataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.result = {}
        
    def process_data(self):
        with open(self.input_file, 'r') as f:
            header = f.readline().strip().split("\t")
            del header[0]
            del header[1:5]
            rs_cols = header
            del rs_cols[0]
#             rs_cols = header[1:5]
            nums = 1

            for line in f:
                fields = line.strip().split('\t')
                del fields[0]
                del fields[1:5]

                key = fields[0]
                values = fields[1:]

                self.result[key] = {}
                for i in range(len(rs_cols)):
                    self.result[key][rs_cols[i]] = values[i]

                print('*** row:', nums, '***')
                nums += 1

            with open(self.output_file, "wb") as fw:
                pickle.dump(self.result, fw)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process input and output files')
    parser.add_argument('input_file', type=str, help='input file')
    parser.add_argument('output_file', type=str, help='output file')
    args = parser.parse_args()
    processor = DataProcessor(args.input_file, args.output_file)
    processor.process_data()
    print('*'*7)
    print('* END *')
    print('*'*7)
