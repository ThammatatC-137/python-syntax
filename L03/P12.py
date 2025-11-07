import math

def clean_words(m):
    m = m.replace('\n', ' ')
    m = m.replace('.', ' ')
    m = m.replace('  ', ' ')
    m = m.lower()
    return m

def nice_print2Ddict(d):
    dkeys = list(d.keys())
    dkeys.sort()
    for k in dkeys:
        print('\n', k)
        d2 = d[k]
        k2s = list(d2.keys())
        k2s.sort()
        
        output_parts = []
        for k2 in k2s:
            output_parts.append("{}:{:.3f}".format(k2, d2[k2]))
        
        # แก้ไขการพิมพ์ให้ตรงกับตัวอย่าง
        print('* ' + '; '.join(output_parts) + ';')

def culture_tf_idf(culture_list):
    Ftd = {}
    for c in culture_list:
        d = {}
        try:
            with open(c, 'r') as f:
                header = f.readline()
                msg = f.read()
                if header[-1] == '\n':
                    header = header[:-1]
                msg = clean_words(msg)
                words = msg.split()
                for t in words:
                    d[t] = d.get(t, 0) + 1
            Ftd[c] = d
        except FileNotFoundError:
            print("Error: File {} not found.".format(c))
            return None

    N = len(Ftd)
    
    Nt = {}
    for doc_name in Ftd:
        term_freq = Ftd[doc_name]
        for t in term_freq:
            Nt[t] = Nt.get(t, 0) + 1

    TF_IDF = {}
    for doc_name in Ftd:
        term_freq = Ftd[doc_name]
        sum_all_ftd = sum(term_freq.values())
        tfidf_ = {}
        
        for t in term_freq:
            tf = term_freq[t] / sum_all_ftd
            idf = math.log(N / Nt[t])
            tfidf_score = tf * idf
            tfidf_[t] = tfidf_score
        

        TF_IDF[doc_name] = {k: v for k, v in tfidf_.items() if v > 0}
        
    return TF_IDF

if __name__ == '__main__':
    cultures = ['./short/chinese.txt',
                './short/thai.txt',
                './short/japanese.txt']
    res = culture_tf_idf(cultures)
    if res:
        nice_print2Ddict(res)