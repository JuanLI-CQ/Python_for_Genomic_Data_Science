#!/usr/bin/python3
"""
The purpose is to finish the final exam of course Python for Genomic Data Science.
"""
def process_fasta(filename):
    "This function is used to process fasta file."
    try:
        f = open(filename)
    except IOError:
        print("The file myseq.fa does not exist!!!")
    
    seqs={}
    for line in f:
        line = line.rstrip()
        if line[0]==">":
            words=line.split()
            name=words[0][1:]
            seqs[name]=''
        else:
            seqs[name]=seqs[name] + line

    f.close()

    seqs_len={name: len(seq) for name,seq in seqs.items()}
    
    lgst_seq_id = [k for k,v in seqs_len.items() if v==max(seqs_len.values())]
    stst_seq_id = [k for k,v in seqs_len.items() if v==min(seqs_len.values())]

    return len(seqs),max(seqs_len.values()),min(seqs_len.values()),lgst_seq_id,stst_seq_id, seqs


filename = "myseq.fa"
result = process_fasta(filename)
if result:
    fasta_len, maxlen, minlen, lgst_seq_id, stst_seq_id, seqs_dict = result
    print(f"The number of sequences in the file {filename} is {fasta_len}")
    print(f"The length of the longest sequence in the file {filename} is {maxlen} with sequence ids {lgst_seq_id}")
    print(f"The length of the shortest sequence in the file {filename} is {minlen} with sequence ids {stst_seq_id}")
else:
    print("Processing failed. Please check the imput file.")

def reading_frame(filename):
    "This function is to identify if a sequence has reading frame with a start and stop codon, and to list out all possible reading frame of each sequence."
    # codons_found=False
    start_codons=["ATG"]
    stop_codons=["TAA", "TAG", "TGA"]
    seqs_orf={}
    for name, seq in seqs_dict.items():
        seq_orfs=[]
        for i in range(0,len(seq)):
            start_codon=seq[i:i+3]
            if start_codon in start_codons:
                for j in range(i+3,len(seq)):
                    stop_codon=seq[j:j+3]
                    if stop_codon in stop_codons:
                        seqs_orf[name]=seq_orfs.append(seq[i:j+3])
    return seqs_orf

reading_frame_result = reading_frame(filename)