"""
Write a function named codon.
The function takes 2 arguments:
a file name of a codon table (as string)
and a file name of a DNA sequence, reads the two files,
uses a codon table to decipher the DNA sequence to a protein,
and returns a list of the deciphered sequence of amino acids.
The codon table file is a simple text file,
written in a simple format:
each line contains one codon and its corresponding amino acid
with a "=" in between.
(Note: fun gene data can be downloaded from
NCBI GenBank, looking for download "FASTA")
"""

def read_codons(fname):
    d = {}
    with open(fname, 'r') as f:
        for line in f:
            k, v = line.strip().split('=')
            d[k] = v
    return d

def codon(codon_table, gene):
    cod_tab = read_codons(codon_table)

    # 1. Read DNA sequence and skip the header line
    dna = ""
    with open(gene, 'r') as f:
        # Skip the first line (header)
        f.readline()
        # Read the rest of the file and remove newlines
        dna = "".join(line.strip() for line in f)

    # 2. Translate each 3-letter set in DNA sequence to an amino acid
    polypep = []
    # Loop through the DNA string in steps of 3
    for i in range(0, len(dna), 3):
        codon_seq = dna[i:i+3]
        
        # 3. Handle cases where the codon is not a full 3-base sequence
        if len(codon_seq) == 3:
            # 4. Look up the codon in the dictionary
            # If the codon is found, append the amino acid. Otherwise, append '?'
            polypep.append(cod_tab.get(codon_seq, '?'))

    return polypep

if __name__ == '__main__':
    # Invocation example 1
    res1 = codon('codons.txt', 'homo_sapiens_mitochondrion.txt')
    print(res1)
    print(len(res1))
    
    # Invocation example 2 (from note)
    # This example requires a file named 'homo_sapiens_insulin.txt'
    # res2 = codon('codons.txt', 'homo_sapiens_insulin.txt')
    # print(res2)
    # print(len(res2))