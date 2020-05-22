import csv
import string

def check_punctuation(term):
    punct = False
    for c in term:
        if c in string.punctuation:
            punct = True
            break
    return punct

def clean_term(term):
    if len(term.split()) < 5 and check_punctuation(term) == False:
        return True
    else:
        return False

c = 0
terms = []
with open('term_list_et.csv', 'r') as f:
    next(f)
    for line in f:
        try: 
            idn,src,tar = line.strip().split(';')  
            #print(src, clean_term(src), '---', tar, clean_term(tar))
            if clean_term(src) == True and clean_term(tar) == True:
                c = c + 1
                terms.append((idn, src, tar))
        except: ## 76 terms have synonyms separated by ; we only take the first one
            line = line.strip().split(';')
            idn = line[0].strip()
            src = line[1].strip().strip('"')
            tar = line[-1].strip().strip('"') 
            if clean_term(src) == True and clean_term(tar) == True:
                c = c + 1
                terms.append((idn, src, tar))

print(c)

with open('term_list_et_clean.csv', 'w') as wf:
    w = csv.writer(wf, delimiter=';')
    w.writerows(terms)
