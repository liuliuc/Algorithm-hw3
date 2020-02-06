
kmer = 4
reads = ['actctcattg','acttttcaacattgactc']
reads = ['ACGGATGATCGATCAAGT', 'GATCAAGTATCCGAAGCT', 'TTCACGGAGATCAAGT']

#build dictionary for kmer to reads
def BuildIndex(reads,kmer):
    ind_dict = {}
    for seq in reads:
        for pos in range(0,len(seq)-kmer+1):
            kmer_seq = seq[pos:pos+kmer]
            if kmer_seq in ind_dict:
                ind_dict[kmer_seq].add(seq)
            else:
                ind_dict.update({kmer_seq:{seq}})
    return ind_dict

#fetch any sequence match suffix
def fetch_match(ind_dict,seq,kmer):
    suffix = seq[0:kmer]
    #print(suffix)
    if suffix in ind_dict:
        return ind_dict[suffix]

#find overlap for all matches if exist    
def find_overlap(match,seq,kmer):
    ol_list = []
    for s_match in match:
        if(s_match != seq):
            #overlap_result = overlap(seq,s_match,kmer)
            overlap_result = overlap(s_match,seq,kmer)
            #print(overlap_result)
            if overlap_result > 0:
                ol_list.append(s_match)
    return seq,ol_list

#overlap two sequece, return the final length        
def overlap(a, b, min_length=3):
    start = 0
    '''return length of longest suffix of 'a' matching a prefix of 'b' that is at least 'min_length' characters long. if no such overlap exists, return 0. '''
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start +=1


#find all overlap
def find_alloverlap(reads,kmer):
    #build kmer dict for entire reads
    ind_dict = BuildIndex(reads,kmer)
    #for every seq in reads
    for seq in reads:
        #find match for this seq
        match = fetch_match(ind_dict,seq,kmer)       
        #find overlap for this seq
        seq,ol_list = find_overlap(match,seq,kmer)
        print(seq)
        print(ol_list)
        

find_alloverlap(reads,kmer)
    