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
    """
    Filter FASTQ reads by GC, length and quality.

    Arguments:
        input_fastq: Input FASTQ file.
        output_fastq: Output file name.
        gc_bounds: Allowed GC range.
        length_bounds: Allowed length range.
        quality_threshold: Minimum mean Phred quality.

    Returns:
        None. Saves reads to filtered/.
    """
    # create output folder
    if not os.path.exists("filtered"):
        os.mkdir("filtered")
    # set output path
    output_path = os.path.join("filtered", output_fastq)
    # open files
    with open(input_fastq, "r") as file_in, open(output_path, "w") as file_out:
        # read FASTQ records
        while True:
            record = read_fastq_record(file_in)
            if record is None:
                break
            # get sequence length
            seq = record[1]
            seq_length = len(seq) - 1
            # check length
            if not check_length(seq_length, length_bounds):
                continue
            # check GC
            if not check_gc(seq, gc_bounds):
                continue
            # check quality
            qual = record[3]
            if not check_quality(qual, quality_threshold):
                continue
            # save reads
            for line in record:
                file_out.write(line)


def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    """
    Convert multiline FASTA to one-line FASTA.

    Arguments:
        input_fasta: Input FASTA file.
        output_fasta: Output FASTA file (optional).

    Returns:
        None. Saves a new FASTA file.
    """
    # set output name
    if output_fasta is None:
        output_fasta = input_fasta + ".oneline.fasta"
    # convert FASTA
    write_oneline_fasta(input_fasta, output_fasta)


def parse_blast_output(input_file, output_file):
    """
    Get the best BLAST hit for each query.

    Arguments:
        input_file: Input BLAST report.
        output_file: Output text file.

    Returns:
        None. Saves sorted protein names.
    """
    # get protein names
    proteins = read_blast_hits(input_file)
    # save results
    with open(output_file, "w") as file_out:
        for protein in proteins:
            file_out.write(protein + "\n")
