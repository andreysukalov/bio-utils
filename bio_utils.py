import os
from helpers.fastq import read_fastq_record, check_length, check_gc, check_quality


def filter_fastq(
    input_fastq,
    output_fastq,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    output_path = os.path.join("filtered", output_fastq)
    with open(input_fastq, "r") as file_in, open(output_path, "w") as file_out:
        while True:
            record = read_fastq_record(file_in)
            if record is None:
                break
            seq = record[1]
            seq_length = len(seq) - 1
            if not check_length(seq_length, length_bounds):
                continue
            if not check_gc(seq, gc_bounds):
                continue
            qual = record[3]
            if not check_quality(qual, quality_threshold):
                continue
            for line in record:
                file_out.write(line)
