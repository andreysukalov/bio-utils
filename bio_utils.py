import os
from helpers.fastq import read_fastq_record, check_length, check_gc, check_quality
from helpers.bio_files import write_oneline_fasta, read_blast_hits


def filter_fastq(
    input_fastq,
    output_fastq,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    if not os.path.exists("filtered"):
        os.mkdir("filtered")

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


def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    if output_fasta is None:
        output_fasta = input_fasta + ".oneline.fasta"

    write_oneline_fasta(input_fasta, output_fasta)


def parse_blast_output(input_file, output_file):
    proteins = read_blast_hits(input_file)

    with open(output_file, "w") as file_out:
        for protein in proteins:
            file_out.write(protein + "\n")
