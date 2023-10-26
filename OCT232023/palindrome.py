def palindrome(original_str):
    rev_string=''
    for i in  original_str:
        rev_string=  i + rev_string
    return rev_string

original_str="NAMA"
print(palindrome(original_str))

def palindrom(original_str):
    return ''.join(reversed(original_str))

print(palindrom(original_str))
