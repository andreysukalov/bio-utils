# Bio Utils
A simple tool for processing biological sequences. It can filter FASTQ files, convert FASTA files and parse BLAST results.

## Installation
Clone the repository from GitHub:
```bash
git clone -b HW4 https://github.com/andreysukalov/bio-utils.git
cd bio-utils
```

Check the Python version:
```bash
python --version
```

## Dependencies
Python 3 (developed with Python 3.14.8).
No external libraries are required.

## Project structure
```text
bio-utils/
├── bio_utils.py
├── run_filter.py
├── helpers/
│   ├── bio_files.py
│   └── fastq.py
└── README.md
```

## Functions
### FASTQ filtering
`filter_fastq()` filters FASTQ reads by:
- GC percentage
- Sequence length
- Mean Phred quality

The output is saved in the `filtered/` folder.

### FASTA conversion
`convert_multiline_fasta_to_oneline()` converts multiline FASTA sequences into one-line sequences.

### BLAST parsing
`parse_blast_output()` gets the best hit for each query and saves protein names in alphabetical order.

## Usage
### FASTQ
Run the interactive script:
```bash
python run_filter.py
```
Enter minimum GC, maximum GC and minimum Phred quality.

Input and output file paths can be changed in `run_filter.py`.

### FASTA
```python
from bio_utils import convert_multiline_fasta_to_oneline
convert_multiline_fasta_to_oneline("input.fasta")
```

The result is saved as `input.fasta.oneline.fasta`.

### BLAST
```python
from bio_utils import parse_blast_output
parse_blast_output("blast.txt", "proteins.txt")
```

The result is saved in `proteins.txt`.
