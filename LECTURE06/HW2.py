def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    #your code here
    new = []
    new2 = []
    for i in words:
        for a in i :
            new.append(a)
    for i in range(0,len(new)+1):
        for a in range(0+i,len(new)+1):
            new2.append(list(set(new[i:a])))
    
    

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

#words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
#print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])
