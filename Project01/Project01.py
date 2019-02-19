"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: RICHARD MANASSEH

"""
from sys import argv

# Read and process SP1.fq and return in lines of 4
def process(lines=None):
    ks = ['name', 'sequence', 'optional', 'quality']
    return {k: v for k, v in zip(ks, lines)}

def get_main(fq):
    """Extract a single read from a FASTQ file.

    Reads in a FASTQ file are stored in 4 lines that contain the
    sequence_id, nucleotide sequence, a second id, and a series of
    characters represeting quality scores.

    :param fq: A file handle for the FASTQ file

    :type fq: An io.TextIOBase object (created using the open() function).

    :return: a list containing 4 strings: the sequence ID, nucleotide sequence,
        second ID, and the quality score sequence. If there are no more
        sequences in the FASTQ file then this function returns False.
    :rtype: a list with four elements

    """
    # list where the newly read dictionaries will be appended
    record = []
    fq = argv[1]
    n = 4

    with open(fq, 'r') as fh:
        lines = []
        for line in fh:
            lines.append(line.rstrip())
            if len(lines) == n:
                record.append(dict(process(lines)))


                lines = []

    return record

def trim_read_front(read, min_q, min_size):
    min_size = 30
    min_q = 30

    read = get_main(argv) # to fetche list returned from get_main above

    rm = [] # list of reads to be removed
    kept = 0

    # loop to iterate through list and return dictionary pair @ each iteration
    for i in read:

        quality = i['quality'] # iterare with key quantity

        sequence =i['sequence'] # iterate with key sequence

        # loop to iterate for value of quality
        for j in quality:

            # to find quality, considering ascii:
            asciiq = ord(j) - 33

            if asciiq <= min_q:
                quality = quality.replace(j, "")
                sequence = sequence[1:len(sequence)]

            elif asciiq > min_q: # if more, break
                break


        if len(quality) < min_size: # if less than min_size, append to rm inorder to del...
            rm.append(i)

    removed = len(rm) # number of nucleotides removed

    for l in rm: # del items in rm from main read list
        index = read.index(l)
        del read[index]

    for t in read: # counts trimmed and kept
        kept+=1

    # terminal prints statements:
    print(str(len(get_main(argv)))+" reads were found")
    print(str(removed)+" reads were removed")
    print(str(kept)+" reads were trimmed and kept")

    return read

#
# The main function for the script.
#
def main(argv):
    """The main function of this script.

    After trimming is completed, the fucntion prints out three status lines. The
    first indicates the total number of reads that were found. The second
    indicates how many reads were removed for being too short after trimming and
    the third indicates how many reas were trimmed and kept.

    The script will create a new FASTQ file of just the trimmed reads and name
    it according to the argument provided by the user when running the script.

    :param argv:  The incoming arguments to this script as
       provided by the sys.argv variable.  There must be four total arguments
       provided to the script must be in the following order

       - The filename for the input FASTQ file
       - The filename for the new output FASTQ file that this script creates
       - An integer for the minimum quality score. Anything below this at the
         beginning of each read's nucleotide sequence is trimmed off.
       - An integer indicating how large a read's nucleotide sequence must
         be after trimming in order to keep it.
    """
    print("Opening Sp1.fq for reading ...")
    print("Opening SP1.trim.fq for writing.....")

    with open("SP1.trim.fq",'w') as f: # open sp1.trim.fq in write mode

        input = trim_read_front(argv,min_q=argv,min_size=argv) # reading trimmed input file...

        # iterate through trimmed input file  and write to sp1.trim.fq
        for items in input:
            for k in items:
                f.write(items[k]+"\n")

# Begin the program by calling the main function.
main(argv)
