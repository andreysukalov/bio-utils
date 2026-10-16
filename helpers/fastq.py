def read_fastq_record(file):
    head = file.readline()
    if head == "":
        return None
    seq = file.readline()
    sep = file.readline()
    qual = file.readline()
    return head, seq, sep, qual


def check_length(seq_length, length_bounds):
    if seq_length < length_bounds[0]:
        return False
    elif seq_length > length_bounds[1]:
        return False
    else:
        return True
