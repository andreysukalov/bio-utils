def read_fastq_record(file):
    head = file.readline()
    if head == "":
        return None
    seq = file.readline()
    sep = file.readline()
    qual = file.readline()
    return head, seq, sep, qual


def check_length(seq_length, length_bounds):
    if type(length_bounds) == int or type(length_bounds) == float:
        length_bounds = (0, length_bounds)
    if seq_length < length_bounds[0]:
        return False
    elif seq_length > length_bounds[1]:
        return False
    else:
        return True


def check_gc(seq, gc_bounds):
    if type(gc_bounds) == int or type(gc_bounds) == float:
        gc_bounds = (0, gc_bounds)
    gc = (seq.count("G") + seq.count("C")) / (len(seq) - 1) * 100
    if gc < gc_bounds[0]:
        return False
    elif gc > gc_bounds[1]:
        return False
    else:
        return True


def check_quality(qual, quality_threshold):
    total = 0
    for char in qual[:-1]:
        total += ord(char) - 33
    average = total / (len(qual) - 1)
    if average >= quality_threshold:
        return True
    else:
        return False
