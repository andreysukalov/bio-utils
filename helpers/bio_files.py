def write_oneline_fasta(input_fasta, output_fasta):
    with open(input_fasta, "r") as file_in, open(output_fasta, "w") as file_out:
        sequence = ""

        for line in file_in:
            if line.startswith(">"):
                if sequence != "":
                    file_out.write(sequence + "\n")

                file_out.write(line)
                sequence = ""
            else:
                sequence += line.strip()

        if sequence != "":
            file_out.write(sequence + "\n")


def read_blast_hits(input_file):
    proteins = []

    with open(input_file, "r") as file_in:
        for line in file_in:
            if line.startswith("Sequences producing significant alignments:"):
                header = file_in.readline()
                file_in.readline()
                hit_line = file_in.readline()

                width = len(header.split("Scientific")[0])
                protein = hit_line[:width].strip()
                proteins.append(protein)

    proteins.sort()
    return proteins
