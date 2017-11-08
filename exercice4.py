def is_vowel (char):
    if len(char)==1 :
        if char in ['i','e','o','a','y','u','I','E','U','O','A','Y'] :
            return True
        else :
            return False
    else :
        print("enter one character")
