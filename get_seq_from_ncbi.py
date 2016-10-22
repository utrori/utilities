def getc(chrom, start, end, strand):
    """getc(chrom, start, end, strand)"""

    from Bio import Entrez, SeqIO
    f = open('/mnt/c/study/Analysis_Paired/chromosomeGI.txt')
    chr_number2chr_id = {}
    for line in f:
        chr_number2chr_id[line.split()[1]] = line.split()[0]

    stranddic = {}
    stranddic['+'] = 1
    stranddic['-'] = 2

    Entrez.email = "yhori@bs.s.u-tokyo.ac.jp"     # Always tell NCBI who you are
    handle = Entrez.efetch(db="nucleotide", id=chr_number2chr_id[str(chrom)], rettype='fasta', strand=stranddic[strand], seq_start=start, seq_stop=end)
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return record.seq


if __name__ == '__main__':
    import sys
    print(getc(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
