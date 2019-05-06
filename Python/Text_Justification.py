#Question: A list of words and the maxWidth of a line, return a list of the justified text
#Solution: Loop through the words, for each line add in a space between the words round-robin until the maxWidth is reached
#Difficulty:  Hard
#Time Complexity: O(n)
#Space Complexity: O(n)

from typing import List

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
  #Variables to store the final outpur, the current sentence, and the number of letters
  justified, current, letterCount = [], [], 0

  #Loop through all words
  for i, word in enumerate(words):

      #If the length of word + current + number of letters is greater than maxWidth
      #The letterCount tells us the length of the letters and len(current) tells the length of the min spaces needed
      #If the length of the sentence (with minimal spacing) + the length of the current word is more than the maxWidth, the current word cannot fit in the sentence
      if (letterCount + len(current)) + len(word) > maxWidth:

          #For each space left over from the maxWidth
          for i in range(maxWidth - letterCount): 
              #Add spaces round-robin to each word, except for the last word
              #This is why we subtract 1 from the length, also, if the length - 1 is 0 mod by 1 instead
              current[i % (len(current) - 1 if len(current) - 1 else 1)] += " "

          #Once we're finished justifying add the sentence to the result and reset the current line and letter count
          justified += ["".join(current)]
          current, letterCount = [], 0

      #Once we've looped through a word, append it to the current line and increment the letter count by its length
      current += [word]
      letterCount += len(word)
  
  #Return the result + the last line, which is simply left aligned with padding on the right
  return justified + [" ".join(current).ljust(maxWidth)]

print(fullJustify(["Listen","to","many,","speak","to","a","few."], 20))
                