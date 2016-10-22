def get_seq(chro, sta, end):
    fhchr = open("chromosomes/chr" + chro + "_straight.fa")
    offset = int(sta) - 1
    fhchr.seek(offset)
    seq = fhchr.read(int(end) - int(sta) + 1)
    return seq


if __name__ == '__main__':
    print('This script requires sequence files without change lines')
    import sys
    if len(sys.argv) == 4:
        print(get_seq(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        chro = raw_input("please input the number of the chromosome:\n")
        star = raw_input("please input the start of the sequence:\n")
        end = raw_input("please input the end of the sequence:\n")
        print(get_seq(chro, star, end))
