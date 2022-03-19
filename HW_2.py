
def reverse(sentence, reverse_word):    
    
    if(type(sentence)!= str or type(reverse_word)!= str):
        return "invalid input" 
        
    if(reverse_word  not in sentence):
        return "The word was not found"
    
    x = sentence.split()
    new = ''
    
    for i in range(0, len(x)):

        if x[i] == reverse_word:

            new = new + reverse_word[::-1]+ ' '

        else:
            new = new + x[i]+ ' '

    return new


