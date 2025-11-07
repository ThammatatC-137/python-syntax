"""
Dict is natural for counting. Write a function named word_freq
to take a string as its argument, count occurrences of each word,
and return the count as a dict.
"""

def clean_txt(msg):
    # The problem note specifies to clean off period, comma, and semicolon.
    # It also says upper case stays, which means we should not use .lower().
    msg = msg.replace('.', ' ')
    msg = msg.replace(';', ' ')
    msg = msg.replace(',', ' ')
    msg = msg.replace('\n', ' ')
    
    # Replace multiple spaces with a single space to avoid empty strings after splitting.
    while '  ' in msg:
        msg = msg.replace('  ', ' ')
        
    return msg.strip()

def word_freq(msg):
    cleaned = clean_txt(msg)
    words = cleaned.split()

    wfreq = {}
    for word in words:
        # The problem requires discarding any word of length 1 or less.
        # This is the key reason for the mismatch.
        if len(word) > 1:
            if word in wfreq:
                wfreq[word] += 1
            else:
                wfreq[word] = 1

    return wfreq

if __name__ == '__main__':
    txt = ("Evil is done by oneself; " +
           "by oneself is one defiled. \n " +
           "Evil is left undone by oneself; " +
           "by oneself is one cleansed. \n" +
           "Purity and impurity are one's own doing. \n" +
           "No one purifies another. \n" +
           "No other purifies one.")

    print(txt)

    wf = word_freq(txt)
    print('\nCount:')
    print(wf)