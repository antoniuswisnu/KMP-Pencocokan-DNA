def match(string, substring):
    submatch = []
    index = []

    for i in range(len(string)-len(substring)):
        if (string[i] == substring[0]):
            submatch = []
            for j in range(len(substring)):
                if (string[i+j] == substring[j]):
                    submatch.append(string[i+j])
                else:
                    submatch = "".join(submatch)
                    for k in range(1,len(submatch)):
                        if (submatch[k:len(submatch)] == submatch[0:len(submatch)-k]):
                            i =  (i+j) - len(submatch[k:len(submatch)])
                            break
                        elif (k == len(submatch)-1):
                            i = i+j
                        else:
                            continue
                    break
                if (j == len(substring)-1):
                    index.append(i)
    return index

dna_ayah = "AACAGGGACTAAAGAGGTGATGATTATCGTGTGTGCCCCGTTATGGTCGTGTTCGATCAGAGCGCCCTTGCGAGCAGTCGTATGCTTTCTCGAATTCCGAGCGGTTAAGCGTGACAGTCCCAGCGAACCCACAAAACGTGATCGCAGTCCATGCGATCATACGCAAGAAGGAAGGTCCCCATACACCGACGCACCAGTTTACACGCCGTATGCATAAACGAGCTGCACAAACGAGAGTGTTTGAACTGGACCTCTAGTTCCTCTACAAAGAACACCTTGACCTGTTGCGAAGTTGCCTTGCCTAGATGCAATGTCGGACGTATCACTTTTGCCTCAACGACTGCTGCTTTCGCTGTAACCCAAGACAGACAACAGTAACCGCCTTTTGAAGGCAAGTCCTCCGCCTGTGACTAACTGTGCCAAATCGTCTTCCAAACCCCTTATCCAATTTAACTCACCAAATTATTGCGATACAGACCCTAATTTCACATCATATGACACTAATTGCCTCTGCCAAAATTCTGTCCTCAAGCGTTTTAGTTCGCCCCAGTAATGTTGCCAATAAGGACCACCAAATCCGCATGTTACAGGACTTCTTATAAATTCTTTTTTCGTGGGGAGCAGCGGATCTTAATGGATGGCGCCAGCTGGTATGGAAGCTAATAGCGCCGGTGAGAGGGTAATCAGCCGTCTCCACCAACACAACGCTATCGGGTCATATTATAAGATTCCGCAATGGGACTACTTATAGGTTGCCTTAACGATATCCGCAACTTGCGATGTGCCTGCTATGCTTAAATACATACCTCGCCCAGTAGCTTTCCAATATGGGAACATCAATTGTACATCGGGCCGGGATAATCATGTCGTCACGGAACTTACTGTAAGAGTAATAATTCAAAAGAGATGTCGGTTTGCTAGTTCACGTAAAGGTGCCTCGCGCCACCTCTAAGTAAGTGAGCCGTCGAGACATTATCCCTGATTTTCTCACTACTATTAG"
dna_anak = "TACTCACGGCGCAATACCACCACAGCCTTGTCTCGCCAGAATGCCGGTCAGCATATGGAAGAGCTCAAGGCAGGTCAATTCGCACTGTGAGGGTCACATGGGCGTTTGGCACTACCGACACGAACCTCAGTTAGCGTACATCCTACCAGAGGTCTGTGGCCCCGTGGTCAAAAGTGCGGGTTTCGTATTTGCTGCTCGTCTGTACTTTCAGAATCTTGACCTGCACGGCAAAGAGACGCTTTTTATGGAGCTCGACATGGCAACAACGCGACGGATCTACGTCACAACGAGAATAGTGTAAACGAAGCTGCTGACGGCGGAAGCGACATAGGGATCTGTGAGTTGTTATTCGCGAAAAACATCCGTCCCCGTGGGGGATAGTCACTGACGCGGTTTTGTAGAAGCCTAGGGGAACAGGTTAGTTTGACTAGCTTAAGAATGTAAATTCTGGGATTATACTGTAGTAATCACTAATTAACGGTGAGGGTTTTAAGACGGATCTTTGCAAATTCAAGCGAGGTGATTTCAACAAATTTTGCTGATGGTTTAGGCGTACAATCCCCTAAAGTATAATTAAGAAAATAGCATTCCTTGTCGCCTAGAATTACCTACCGGCGTCCACCATACCTTCGATATTCGCGCCCACTCTCCCATTAGTCGGCACAAGTGGATGTGTTGCGATTGCCCGCTAAGATATTCTAAGGCGTAACGCAGATGAATATTCTACAGAGTTGCCGTACGCGTTGAACACTTCACGGATGATAGGAATTTGCGTATAGAGCGGGTCATTGAAGGGTTATACACTCGTAGTTAACAACGGGCCCGGCTCTATCAGAACACGAGTGCCTTGAATAACATACTCATCACTAAACTTTCTCAACAGTCAATCGAGCAAGTCCATGACCAAGGAGTGCGATGCAGTTTTATTCTCTCGCCAGCACTGTAATAGGCACTAAAAGAGTGATGATAATCATGAGTGCTGAGCTAAGACGGCGTCGGT"
dna_ibu = "ACATAGCGGTCTTACGGTCAGTCGTAATTCCTCACGAGTCCCGTCCAGTTGAGCGTATCACTCCCAATGTACAAGCAACCCGAGAAGGCTGTGCTTGGAGTCAATCGGATGTAGGATGGTCTCCAGACACGGGGCCACCACTCTTCACGCGTAAAGCAAGAACGTCGAGCAGTCATGAAAGTCTTAGTACCGGACGTGCCGTTTTACTGCGAATATTACCTGAAGCTGTACCGTTATTGGGGGGCAAAGATGGAGTCCTCCTCTTATCATATTTGTATTGACGACAGCCGTGTTCCCGGTTTCCTCAGAGATTTAAGAATAAGGGCTTATTGTAGGCAGAGGGACGCCCTTTTAGTGGCTGGCGTAAAATATCTTCGGATCCCCTTGTCTAACCAGATTAATCGAATTCTCTCATTTAGGACCCTAGTAAGTCATCATTGGTGTTTAAATGCCACCCCGAAGAAACCGCCTAAAAATGTCTATGATTGGTCCACTAAAGTTGATTAAATCAACTCCTAAATCCGCGCGATAGGGCATTAGAGGTTTAATTTTGTATGGCAAGGTACTCCCGATCTTAATGAATGGCCGGAAGTGGTACGGACGCAATATGCGCGGGTGAGAGGGCAAATAGGCAGGTTCGCCTACGTTACGCTAGGGGGCGATTCTATAAGAATGCACATTGCATCGATACATAAGATGTCTCGACCGCATGCGCAACTTGTGAAGTGTCTACTATCCCTAAGCCCATTTCTCGCACAATAACCCCTGAATGTGTCCGCATCTGATGTTACCCGGGTTGAGTTAGTGTCGAGCTCGCGGAACTTATTGCATGAGTAGAGATATGTAAGAGCTGTTAGATAGCTCGCTGAGCTAATAGTTGCCCACAGAACGTCAAAATTAGAGAACGGTCGTAACATTATCGGTGGTTCTCTAACTACTATCAGTACCCATGACTCGACTCTGCCGCAGCTACCTATCGCCTGAAAGCCAGTTGGTGTTA"

cari_dna = "CACA"
matching_ayah = match(dna_ayah, cari_dna)
matching_anak = match(dna_anak, cari_dna)
matching_ibu = match(dna_ibu, cari_dna)

print("terdapat "+str(len(matching_ayah))+" DNA "+ cari_dna + " ayah")
print("terdapat "+str(len(matching_anak))+" DNA "+ cari_dna + " anak")
print("terdapat "+str(len(matching_ibu))+" DNA "+ cari_dna + " ibu")
print(end="\n")

cari_dna2 = "CATG"
matching_anak = match(dna_anak, cari_dna2)
matching_ibu = match(dna_ibu, cari_dna2)
print("terdapat "+str(len(matching_anak))+" DNA "+ cari_dna2 + " anak")
print("terdapat "+str(len(matching_ibu))+" DNA "+ cari_dna2 + " ibu")