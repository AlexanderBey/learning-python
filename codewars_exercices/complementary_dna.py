def DNA_strand(dna):
    dna_list = list(dna)
    replacement_letter_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    for index, letter in enumerate(dna_list):
        dna_list[index] = replacement_letter_dict[letter]
    return ''.join(dna_list)

print(DNA_strand('ATTGC'))
print(DNA_strand('GTAT'))




# better solution:

# def DNA_strand(dna):
#     return dna.translate(str.maketrans("ATCG","TAGC"))
#
# print(DNA_strand('ATTGC'))
# print(DNA_strand('GTAT'))
