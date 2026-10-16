import os
from helpers.fastq import read_fastq_record, check_length


def filter_fastq(input_fastq, output_fastq, length_bounds=(0, 2**32)):
    output_path = os.path.join("filtered", output_fastq)
    with open(input_fastq, "r") as file:
        while True:
            record = read_fastq_record(file)
            if record is None:
                break
            seq = record[1]
            seq_length = len(record[1]) - 1
            if not check_length(seq_length, length_bounds):
                continue
