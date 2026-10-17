from bio_utils import filter_fastq

# set file paths
input_fastq = "example_data/example_fastq.fastq"
output_fastq = "result.fastq"
# set filter parameters
min_gc = float(input("Minimum GC (%): "))
max_gc = float(input("Maximum GC (%): "))
min_quality = float(input("Minimum Phred quality: "))
# filter FASTQ
filter_fastq(
    input_fastq,
    output_fastq,
    gc_bounds=(min_gc, max_gc),
    quality_threshold=min_quality,
)
# show result
print("Saved to filtered/" + output_fastq)
