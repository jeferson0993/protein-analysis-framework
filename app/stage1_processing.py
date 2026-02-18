from Bio import SeqIO

def clean_sequences(input_fasta):
    records = list(SeqIO.parse(input_fasta, "fasta"))
    filtered = [r for r in records if len(r.seq) > 50]
    return filtered
