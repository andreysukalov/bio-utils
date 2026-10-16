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
