def read_fastq_record(file):
    head = file.readline()
    seq = file.readline()
    sep = file.readline()
    qual = file.readline()
    return head, seq, sep, qual
