def count_kmer(kmer, text):
    count = 0
    k = len(kmer)
    for i in range(len(text) - k + 1):
        if text[i:i+k] == kmer:
            count += 1
    return count


if __name__ == "__main__":
    r = count_kmer('ACTAT', 'ACAACTATGCATACTATCGGGAACTATC')
    print(r)

    r = count_kmer('AC', 'ACAACTATGCATACTATCGGGAACTATC')
    print(r)

    r = count_kmer('ATA', 'CGATATATCCATAG')
    print(r)
