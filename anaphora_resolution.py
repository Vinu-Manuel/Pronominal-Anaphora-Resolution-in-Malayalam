
# Importing Malayalam Morphological Analyzer mlmoprh:

from mlmorph import Analyser
analyser = Analyser()

from mlmorph import Generator
generator = Generator()

# Creating an infinite loop:

while True:

# Creating user input and extracting information from user input:

    # creating user input:
    para = input("Input sentence here: ")
    # Splitting user inputed paragraph into sentences:
    sent = para.split('.')
    # Creating empty lists 'words', 'se', 'complist', 'wsf', 'reflxv'.
    words = []
    se = []
    complist = []
    wsf = []
    reflxv = []

    # For each sentence: 
    for w in range(len(sent)):
        # Splitting sentence into words:
        word = sent[w].split()

# Preperation for adding index of the sentence numbers.

        # Duplicating 'word' list:
        ws = word
        # Creating a list of word with the sentence number.
        for n in range(len(ws)):
            ws1 = [ws[n], w]
            wsf.append(ws1)
        

# Analyzing user input with a Morphological Analyzer:

        # Preparing morphological analyzer:
        analyser = Analyser()

        # For each word:
        for w1 in word:
            # Adding each word to list 'words':
            words.append(w1)
            # Analyzing each word using Morphological Analyzer
            wrdana = analyser.analyse(w1)
            

# Extracting information from the analysis:

            # Creating empty list 'anlyzd'
            anlyzd = []

            # For each analysis:
            for a1 in wrdana:
                # Converting tuple to list: 
                lst = list(a1)
                # For each item in the list:
                for i in lst:
                    # If item is a string:
                    if type(i) != int:
                        # Split item between '<'
                        wrd1 = i.split('<')
                        # For each item in the list:
                        for i2 in wrd1:
                            # If item is a string:
                            if type(i2) != int:
                                # Split item between '>':
                                wrd2 = i2.split('>')
                                # For each item in the list:
                                for i3 in wrd2:
                                    # Add item to the list 'anlyzd'
                                    anlyzd.append(i3)
                            # Else, continue the program.
                            else:
                                pass
                    # Else, continue the program.
                    else:
                        pass

            # Adding word to the analysis list:
            anlyzd.insert(0,w1)

            # Creating a list of analyzed information.
            complist.append(anlyzd)
    
    
# Creating an index for analyzed information:

    # Creating empty list:
    ind = []
    # Comparing analyzed word list and sentence word list:
    for w2 in range(len(complist)):
        for x in range(len(words)):
            # If words match:
            if complist[w2][0] == words[x]:
                # If word already exist in list 'ind':
                if words[x] in ind:
                    # Replace the word's index number.
                    complist[w2][-1] = w2
                else:
                    # Else, add index number.
                    complist[w2].append(x)
                    # Add word to the list 'ind'.
                    ind.append(complist[w2][0])
            else:
                pass
    

# Creating an index for sentence number.

    # Comparing the two lists 'wsf' and 'complist':
    for ws2 in range(len(wsf)):
        for co in range(len(complist)):
            # If words match:
            if co == ws2:
                # Inserting sentence number from list 'wsf' to 'complist'
                complist[co].insert(1,wsf[ws2][-1])
            else:
                pass



# Exracting noun and pronomina entities from the input:

    # Creating empty lists 'noun' and 'prnoun':
    noun = []
    prnoun = []

    # For each item in the list 'complist':
    for n in complist:
        # If item is noun:
        if 'np' in n:
            # Add item to the list 'noun':
            noun.append(n)
        # If item is pronoun:
        elif 'prn' in n:
            # Add item to the list 'prnoun':
            prnoun.append(n)
        else:
            pass

    
# Creating dialogue for output:

    anap = "The anaphora is : "
    ante = "The antecedent is : "
    noan = "There is no coreference for the pronoun"
    noant = "There is no antecedent in the input."
    noanp = "There is no anaphora in the input."


# Creating a list of 1st and 2nd person pronouns:

    prn1n2 = ['ഞാൻ', 'നീ', 'നിങ്ങൾ', 'ഞങ്ങൾ', 'നമ്മൾ', 'നാം', 'താങ്കൾ' ]

# Creating a list of reflexive pronouns:

    reflxv = ['തന്നെ', 'താനെ', 'സ്വയം', 'സ്വൻതം', 'സ്വന്തo'  ]

# Analysing reflexive pronoun in the input and labelling them:

    # For each pronoun
    for p in range(len(prnoun)):
        # If pronoun is in the list 'reflxv':
        if prnoun[p][0] in reflxv:
            # If the pronoun is not the first word of the sentence:
            if prnoun[p][-1] != 0:
                # If the word precceding the pronoun is a noun or a pronoun:
                if complist[prnoun[p][-1]-1] in noun or complist[prnoun[p][-1]-1] in prnoun:
                    # Insert 'reflx' in the pronoun's and the preceeding word's analysis data: 
                    complist[prnoun[p][-1]-1].insert(5,'reflx')
                    prnoun[p].insert(5,'reflx')
                else:
                    pass
            else:
                pass
        else:
            pass


# Defining function for 1st and 2nd person pronoun:

    def p1n2():
        # Creating empty list:
        m = []
        # for each pronoun:
        for pr in prnoun[p]:
            # if pronoun in list prn1n2
            if pr in prn1n2:
                # Adding pronoun to list 'm' if not present:
                if 'm' not in m:
                    m.append('m')
                else:
                    pass
            else:
                pass
        # If list 'm' is not empty:
        if len(m) == 0:
            # Print as instructed:
            print(anap, prnoun[p][0])
            print(ante, sub[0][2])
        # Else, print as instructed. 
        else:
            print(noan, prnoun[p][0])

# Defining function for affirmation:

    def affr():
        # Creating empty list:
        aff = []
        # for each word in the sentence containing the pronoun:
        for ws in range(len(wis)):
            # If affirmation present in the word:
            if 'aff' in wis[ws]:
                # Add word to the list 'wis':
                aff.append(wis[ws])
            else:
                pass
        # If the list 'aff' is not empty:    
        if len(aff) > 0:
            # Print as instructed.
            print(anap, prnoun[p][0])
            print(ante, sub[0][2])
        else:
            # Else, run function 'out'.
            out()
            

# Defining function for negation:

    def negt():
        # Creating empty list:
        neg = []
        # for each word in the sentence containing the pronoun:
        for ws in range(len(wis)):
            # If the word contain negation:
            if 'neg' in wis[ws]:
                # Add word to the list 'neg':
                neg.append(wis[ws])
            else:
                pass
        # If the list 'neg' is not empty:
        if len(neg) > 0:
            # Print as instructed:
            print(noan, prnoun[p][0])
        else:
            # Else, run function 'affr'.
            affr()


# Defining function for output:

    def out():
        # If the number of nouns in the sentence containing the pronoun is 1: 
        if len(nis) == 1:
            # If the number of nouns in the sentence preceeding the sentence containing the pronoun is 1: 
            if len(nbs) > 0:
                # Print as instructed.
                print(anap, prnoun[p][0])
                print(ante, nbs[-1][2])
            # If the number of nouns in the sentence preceeding the sentence containing the pronoun is 1: 
            elif len(nfs) > 0:
                # Print as instructed.
                print(anap, prnoun[p][0])
                print(ante, nfs[0][2])
            # Else, print as instructed.
            else:
                print(noan, prnoun[p][0])
        # Else, # If the number of nouns in the sentence containing the pronoun is more than 1: 
        else:
            # If the number of possible antecedent candidates is more than 0:
            if len(psscan) > 0:
                # Print as instructed.
                print(anap, prnoun[p][0])
                print(ante, psscan[-1][2])
            # Else if the number of possible antecedent candidates is 0:
            else:
                # If the number of nouns in the sentence preceeding the sentence containing the pronoun is 1: 
                if len(nbs) > 0:
                    # Print as instructed.
                    print(anap, prnoun[p][0])
                    print(ante, nbs[-1][2])
                # If the number of nouns in the sentence preceeding the sentence containing the pronoun is 1: 
                elif len(nfs) > 0:
                    # Print as instructed.
                    print(anap, prnoun[p][0])
                    print(ante, nfs[0][2])
                # Else, print as instructed.
                else:
                    print(noan, prnoun[p][0])
            

# Defining function for determinig the antecedent depending on the case of the pronoun:

    def case():
        # If case of pronoun is accusative:
        if 'accusative' in prnoun[p]:
            # Run function 'out':
            out()
        # If case of pronoun is genetive:
        elif 'genitive' in prnoun[p]:
            # If noun occurs before pronoun:
            if sub[0][-1] < prnoun[p][-1]:
                # Creating empty list 'per':
                per = []
                # For each word in the sentence:
                for ws in range(len(wis)):
                    # If word 'പേര്' in the sentence:
                    if 'പേര്' in wis[ws]:
                        # Add word to the list 'per'
                        per.append(wis[ws])
                # If the list 'per' is not empty:
                if len(per) > 0:
                    # Print as instructed:
                    print(anap, prnoun[p][0])
                    print(ante, sub[0][2])
                # Else, run function p1n2():
                else:
                    p1n2()
            # Else if noun occurs after pronoun: 
            else:
                # Creating empty list 'per':
                per = []
                # For each word in the sentence:
                for ws in range(len(wis)):
                    # If word 'പേര്' in the sentence:
                    if 'പേര്' in wis[ws]:
                        # Add word to the list 'per'
                        per.append(wis[ws])
                # If the list 'per' is not empty:
                if len(per) > 0:
                    # Print as instructed:
                    print(anap, prnoun[p][0])
                    print(ante, sub[0][2])
                # Else, run the function 'out'.
                else:
                    out()
        # If case of pronoun is instrumental:
        elif 'instumental' in prnoun[p]:
            # If the case of noun is accusative or instrumental or dative or locative:
            if 'accusative' in sub[0] or 'instrumental' in sub[0] or 'dative' in sub[0] or 'locative' in sub[0]:
                # Run function 'out':
                out()
            # Else if noun occurs before pronoun:
            else:
                if sub[0][-1] < prnoun[p][-1]:
                    # Run function 'p1n2':
                    p1n2()
                # Else, run function 'out':
                else:
                    out()
        # Else if case of pronoun is dative:
        elif 'dative' in prnoun[p]:
            # Check if case of noun is accusative or instrumental or locative: 
            if 'accusative' in sub[0] or 'instrumental' in sub[0] or 'locative' in sub[0]:
                # Run function 'out':
                out()
            # Else is noun or pronoun is affirmative:
            elif 'aff' in sub[0] or 'aff' in prnoun[p]:
                # Print as instructed
                print(anap, prnoun[p][0])
                print(ante, sub[0][2])                
            else:
                # Else if noun occurs before pronoun:
                if sub[0][-1] < prnoun[p][-1]:
                    # Run function 'p1n2':
                    p1n2()
                else:
                    # Else, run function 'out':
                    out()
        # Else if case of pronoun is locative:
        elif 'locative' in prnoun[p]:
            # If case of noun is accusative or instrumental or locative:
            if 'accusative' in sub[0] or 'instrumental' in sub[0] or 'locative' in sub[0]:
                # Run function 'out'.
                out()
            # Else if noun occurs before proonoun:
            else:
                if sub[0][-1] < prnoun[p][-1]:
                    # Run function 'p1n2'
                    p1n2()
                else:
                    # Else, run function 'out'
                    out()
        # Else if case of pronoun is sociative:
        elif 'sociative' in prnoun[p]:
            # If case of noun is accusative or instrumental or dative or sociative:
            if 'accusative' in sub[0] or 'instrumental' in sub[0] or 'dative' in sub[0] or 'sociative' in sub[0]:
                # Run function 'out'.
                out()
            else:
                # Else if noun occurs before atecedent:
                if sub[0][-1] < prnoun[p][-1]:
                    # Run function 'p1n2':
                    p1n2()
                else:
                    # Run function 'out':
                    out()
        # Else, if case of noun is sociative: 
        else:
            if 'sociative' in sub[0]:
                # If noun occurs before pronoun:
                if sub[0][-1] < prnoun[p][-1]:
                    # Run function 'p1n2':
                    p1n2()
                else:
                    # Run function 'out':
                    out()
            # Else if case of noun is not accusative or genitive or instrumental or locative or sociative:
            elif 'accusative' not in sub[0] and 'genitive' not in sub[0] and 'instrumental' not in sub[0] and 'locative' not in sub[0] and 'sociative' not in sub[0]:
                # If case of noun is dative:
                if 'dative' in sub[0]:
                    # Run function 'affr':
                    affr()
                else:
                    # Else, run functiono 'negt':
                    negt()
            else:
                # Else, run function 'out':
                out()


    
# Procedure for resolving anaphora resolution:        
                         
    #  If the number of nouns or pronouns is 0:          
    if len(noun) == 0 or len(prnoun) == 0:
        # If the number of nouns is 0:
        if len(noun) == 0:
            # Print as instructed:
            print(noant)
        # If the number of pronouns is 0:        
        elif len(prnoun) == 0:
            # Print as instructed:
            print(noanp)
    # Else:
    else:
        # For each pronouns:
        for p in range(len(prnoun)):
            # Creating empty lists 'nis', 'nbs', 'nfs', 'wis', 'dfp', 'sdn', 'msdn', 'smsdn', 'psscan', 'nbp':
            nis = []
            nbs = []
            nfs = []
            wis = []
            dfp = []
            sdn = []
            msdn = []
            smsdn = []
            psscan = []
            nbp = []
            

# Creating a list of words in the sentence containing the pronoun.

            # For each word in the input:
            for wr in range(len(complist)):
                # If the words are in the sentence containing the pronoun:
                if complist[wr][1] == prnoun[p][1]:
                    # Add word to the list 'wis'
                    wis.append(complist[wr])


# Creating lists of nouns depending on the place of occurence:                    

            # For each noun:
            for nn in range(len(noun)):
                # If the noun occur in the same sentence containing the pronoun:
                if noun[nn][1] == prnoun[p][1]:
                    # Add noun to the list 'nis':
                    nis.append(noun[nn])
                # If the noun occur in the sentence preceding the sentence containing the pronoun:
                elif noun[nn][1] < prnoun[p][1]:
                    # Add noun to the list 'nbs':
                    nbs.append(noun[nn])
                # If the noun occur in the sentence succeeding the sentence containing the pronoun:
                elif noun[nn][1] > prnoun[p][1]:
                    # Add noun to the list 'nfs':
                    nfs.append(noun[nn])
                else:
                    pass

                
                # If the noun occur before the pronoun in the sentence:
                if noun[nn][-1] < prnoun[p][-1]:
                    # Add noun to the list 'nbp':
                    nbp.append(noun[nn])

# Calculating the distance of each noun from the pronoun and adding it to the analysis:

                # Calculating the distance of noun from the pronoun:
                dfpu = abs(prnoun[p][-1] - noun[nn][-1])
                # Adding the distance value to the list 'dfp':
                if dfpu not in dfp:
                    dfp.append(dfpu)
                else:
                    pass
                # Adding the distance value to the noun:
                noun[nn].insert(-1,dfpu)
                
            # Sort the list 'dfp' in the ascending order of the distance value:
            dfp.sort()

            # For each noun:
            for nn in range(len(noun)):
                # If the noun is the closest to the pronoun:
                if dfp[0] == noun[nn][-2]:
                    # Add noun to the list 'sdn':
                    sdn.append(noun[nn])            

            # For each noun:
            for nn in range(len(noun)):
                # If the noun is not in the list 'sdn':
                if noun[nn] not in sdn:
                    # Add noun to the list 'psscan':
                    psscan.append(noun[nn])
                

# Anaphora resolution based on the number of nouns in the sentence:

            # If the number of nouns is 0:
            if len(nis) == 0:
                # If the number of nouns in the sentence preceding the sentence containing the pronoun is more than 0:
                if len(nbs) > 0:
                    # Print as instructed:
                    print(anap, prnoun[p][0])
                    print(ante, nbs[-1][2])
                # Else, if the number of nouns in the sentence succeeding the sentence containing the pronoun is more than 0:
                elif len(nfs) > 0:
                    # Print as instructed:
                    print(anap, prnoun[p][0])
                    print(ante, nfs[0][2])
                # Else, print as instructed:
                else:
                    print(noant)

    # Evaluating reflexive pronouns:
            # If the pronoun is reflexive:
            elif 'reflx' in prnoun[p]:
                # If the number of nouns in the sentence preceding the sentence containing the pronoun is more than 0:
                if len(nbp) > 0:
                    # Print as instructed:
                    print(anap, prnoun[p][0])
                    print(ante, nbp[-1][2])
                # Else, print as instructed:
                else:
                    print(noan, prnoun[p][0])
                
            # If the number of nouns in the sentence containing the pronoun is 1:
            elif len(nis) == 1:
                sub = nis
                # Run function 'case':
                case()
                    
            # If the number of nouns in the sentence containing the pronoun is more than 1:
            elif len(nis) > 1:
                # If the number of nouns in the list 'sdn' is 1:
                if len(sdn) == 1:                    
                    sub = sdn
                    # Run function 'case':
                    case()
                        
                # Else, if the number of nouns in the list 'sdn' is more than 1:
                else:
                    # For each noun in the list 'sdn':
                    for sn in range(len(sdn)):
                        # Add noun's occurence number to the list 'msdn': 
                        msdn.append(sdn[sn][-1])
                    # Sort list according to the occurence number:
                    msdn.sort()
                    # For every noun in the list 'sdn':
                    for sn in range(len(sdn)):
                        # If the noun's occurence number is the same as the last occurence number:
                        if sdn[sn][-1] == msdn[-1]:
                            # If the noun not already in list 'smsdn':
                            if sdn[sn] not in smsdn:
                                # Add noun to list 'smsdn':
                                smsdn.append(sdn[sn])
                                
                    sub = smsdn
                    # Run function case():
                    case()

                    

