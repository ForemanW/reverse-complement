'''Outputs the reverse complement of a DNA sequence'''
def reverse_complement(input_seq):
    #first, reverse the sequence
    reverse = input_seq[::-1]


    #Now we need to use a dictionary, where the keys are the DNA bases and values are the respective complements
    complements = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}

    #now we build the reverse complement as a list
    reverse_comp = []
    for base in reverse:
        reverse_comp.append(complements.get(base))

    #great, now we convert to a string and output
    result = ''.join(reverse_comp)

    return print("reverse complement strand: " + result)

if __name__ == "__main__":
    user_input = input("Please paste the DNA sequence you'd like to reverse complement: ")
    reverse_complement(user_input)

