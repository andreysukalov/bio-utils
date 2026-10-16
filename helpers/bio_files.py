def write_oneline_fasta(input_fasta, output_fasta):
    """
    Convert multiline FASTA to one-line FASTA.

    Arguments:
        input_fasta: Input FASTA file.
        output_fasta: Output FASTA file.

    Returns:
        None. Saves a new FASTA file.
    """

    # open files
    with open(input_fasta, "r") as file_in, open(output_fasta, "w") as file_out:
        sequence = ""
        # read FASTA lines
        for line in file_in:
            # check sequence header
            if line.startswith(">"):
                # save previous sequence
                if sequence != "":
                    file_out.write(sequence + "\n")
                # save header
                file_out.write(line)
                sequence = ""
            # collect sequence
            else:
                sequence += line.strip()
        # save last sequence
        if sequence != "":
            file_out.write(sequence + "\n")


def read_blast_hits(input_file):
    """
    Get the best BLAST hits.

    Arguments:
        input_file: Input BLAST report.

    Returns:
        Sorted list of protein names.
    """
    # create protein list
    proteins = []
    # open BLAST report
    with open(input_file, "r") as file_in:
        # find BLAST results
        for line in file_in:
            if line.startswith("Sequences producing significant alignments:"):
                # read header and first hit
                header = file_in.readline()
                file_in.readline()
                hit_line = file_in.readline()
                # get protein name
                width = len(header.split("Scientific")[0])
                protein = hit_line[:width].strip()
                # add protein to list
                proteins.append(protein)
    # sort protein names
    proteins.sort()
    # return list
    return proteins
