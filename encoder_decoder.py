# 1. take input whether to decode or encode 
# 2. To encode: a)half b)reverse second half c)attach it in front of text and length of text in between first and second half
#3. To decode: a)half b)reverse first half c)attach it at end of second hal( that doesnot include text)



task = input("Do you want to do encode or decode? ")
text = input(f"Enter text to {task}: ")
text = text.split(" ")


def encode(text):
    ans =""
    for words in text:
        length, half_length = get_half_length(words)

        first_half = substring(words, 0,half_length)
        second_half = substring(words, half_length, length)
        rev = reverse(second_half)

        l = str(length)
        ans =  ans+ " " + (rev + l + first_half)
    return ans

def substring(words, first, second):
    first_half = words[first:second]
    return first_half

def get_half_length(words):
    length = len(words)
    half_length = length//2
    return length,half_length

def reverse(half):
    rev=""
    for c in half:
        rev = c + rev
    return rev

def decode(text):
    ans=""
    for words in text:
        length, half_length = get_half_length(words)

        first_half = substring(words, 0,half_length)
        second_half = substring(words, half_length+1, length)
        rev= reverse(first_half)
        ans = ans + " " +second_half + rev

    return ans
ans=""
if( task == "encode" ):
    ans = encode(text)
    print(ans)
elif task == "decode":
    ans = decode(text)
    print(ans)
else:
    print("INVALID INPUT")