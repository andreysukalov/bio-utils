def read_fastq_record(file):
    """
    Read one FASTQ record.

    Arguments:
        file: Open FASTQ file.

    Returns:
        Four FASTQ lines or None.
    """
    # read header
    head = file.readline()
    # check end of file
    if head == "":
        return None
    # read other lines
    seq = file.readline()
    sep = file.readline()
    qual = file.readline()
    # return record
    return head, seq, sep, qual


def check_length(seq_length, length_bounds):
    """
    Check sequence length.

    Arguments:
        seq_length: Sequence length.
        length_bounds: Allowed length range.

    Returns:
        True or False.
    """
    # set length range
    if type(length_bounds) == int or type(length_bounds) == float:
        length_bounds = (0, length_bounds)
    # check length
    if seq_length < length_bounds[0]:
        return False
    elif seq_length > length_bounds[1]:
        return False
    else:
        return True


def check_gc(seq, gc_bounds):
    """
    Check GC percentage.

    Arguments:
        seq: DNA sequence.
        gc_bounds: Allowed GC range.

    Returns:
        True or False.
    """
    # set GC range
    if type(gc_bounds) == int or type(gc_bounds) == float:
        gc_bounds = (0, gc_bounds)
    # calculate GC
    gc = (seq.count("G") + seq.count("C")) / (len(seq) - 1) * 100
    # check GC
    if gc < gc_bounds[0]:
        return False
    elif gc > gc_bounds[1]:
        return False
    else:
        return True


def check_quality(qual, quality_threshold):
    """
    Check mean Phred quality.

    Arguments:
        qual: Quality string.
        quality_threshold: Minimum mean quality.

    Returns:
        True or False.
    """
    # calculate total quality
    qual = qual.strip()
    total = 0
    for char in qual:
        total += ord(char) - 33
    # calculate mean quality
    average = total / len(qual)
    # check quality
    if average >= quality_threshold:
        return True
    else:
        return False
