def count_words(book:str) -> int:
    words:list = book.split()
    return len(words)

def get_num_words(book:str)-> list:
    seen = set()
    num_char = {}
    num_char[' '] = book.count(" ")
    words:list = book.lower().split()
    for word in words:
        for char in word:
            if char not in seen:
                seen.add(char)
                num_char[char] = 1
            else:
                num_char[char] += 1
                
    result = list(num_char.items())  
    result.pop(0)    
    return sorted(result, key=lambda item:item[1], reverse=True)