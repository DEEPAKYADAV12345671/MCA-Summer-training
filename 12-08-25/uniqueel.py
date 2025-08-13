def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
sample_list = [1, 2, 2, 3, 4, 1, 5]
print(unique_elements(sample_list))  

#List rotation
def rotate_list(input_list, n):
    """Rotate the list to the right by n positions."""
    n = n % len(input_list)  # Handle n > len(input_list)
    return input_list[-n:] + input_list[:-n]

# Example usage:
rotated = rotate_list([1, 2, 3, 4, 5], 2)
print(rotated)
#Find longest Word 
def longest_word(sentence):
    """Return the longest word from a given sentence."""
    words = sentence.split()
    if not words:
       return None
    longest = words[0]  
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
sentence = "Python is an amazing programming language"
print(longest_word(sentence)) 
#Sum of digitis
def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    print(total)
sum_of_digits(12345)
#Character of frequency
# ...existing code...

# Character Frequency Counter
def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
print(char_frequency("hello")) 
#divisible 3&5
def divisible(start,end):
    for num in range(start,end+1):
        if(num%3==0)^(num%5==0):
            print(num,end='')
            print()
divisible(1,100)
#reverse wordspyr
words=input("Enter the words")
for i in range(len(words)-1,-1,-1):
    print(words[i])
def reverse_words(sentence):
    words = []
    word = ""
    for char in sentence:
        if char == " ":
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    if word:
        words.append(word)
    reversed_sentence = ""
    for i in range(len(words)-1, -1, -1):
        reversed_sentence += words[i]
        if i != 0:
            reversed_sentence += " "
    print(reversed_sentence)
reverse_words("Python is fun")  
#guess the num
secnum=8
while True:
    guess=int (input("Enter the num:"))
    if guess==secnum:
        print("Correvt You guessed")
        break
    else:
        print("Wrong")
        #count of constant 
def const(s):
            consonants="skjhggdtifsfvkxdigoudod"
            count=0
            for i in s:
                for s in consonants:
                    count+=1
                    print(count)
const("hello word") 


