#write a function that takes a string and returns the count of vowels and consonants separately
def count_Vowle_Consonant(userInput):
    vowels= "aeiouAEIOU"
    countVowel =0
    countConsonants= 0

    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):

                countVowel=countVowel+1
            else :
                countConsonants+=1
    return countVowel,countConsonants

#Function call
vowel,consonant= count_Vowle_Consonant("Ajeet Prasad")
print(vowel,consonant)

    