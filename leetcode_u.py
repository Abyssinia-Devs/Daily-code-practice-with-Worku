import string
class Solution:
    
    def isValid(self, word):
        leng = len(word) >= 3

        # Define character sets
        letters_set = set(string.ascii_letters)
        punctuation_set = set(string.punctuation)
        vowels_set = set('aeiouAEIOU')

        # Check for invalid characters
        symbl = all(ch.isalnum() or ch in letters_set for ch in word)

        # Extract letters only
        letters = [ch for ch in word if ch in letters_set]

        # Extract vowels and consonants
        vow = [ch for ch in letters if ch in vowels_set]
        con = [ch for ch in letters if ch not in vowels_set]

        # Final check
        return all([leng, symbl, vow, con])
s1 = Solution()
x= 'xnvvc_='  
check = s1.isValid(x)
if __name__ == '__main__':
    print(check) #false


        