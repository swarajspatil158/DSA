
# Stack Implementation -->
class Stack:
    def __init__(self) -> None:     # constructor initializes stack
        self.array = []

    def push(self,element) -> None: # append element
        self.array.append(element)

    def pop(self) -> None:          # pop(remove and return last element) 
        return self.array.pop()     # element from stack

    def is_empty(self):             # check if stack is empty or not
        return self.array == []

    def peek(self) -> None:         # returns last element, if exists
        if not self.is_empty():
            return self.array[-1]

    def get_stack(self):            # print stack
            return self.array


# -------------------------------------------------
# Determine if brackets are balanced

def is_match(p1,p2):
    if p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    else:
        return False

# --------------------------------------------------
def is_paren_balanced(paren_string):
    st = Stack()
    is_balanced = True
    index = 0
    while index < str_length and is_balanced:
        paren = paren_string[index]
        if paren in "{[(":
            st.push(paren)
        else:
            if st.is_empty():
                is_balanced = False
                break
            else:
                top = st.pop()
                if not is_match(top,paren):
                    is_balanced = False
                    break
        index+=1
    if st.is_empty() and is_balanced:
        return True
    else:
        return False
# ----------------------------------------------
paren_str = "{{{)}]"
str_length = len(paren_str)
print(is_paren_balanced(paren_str))

# ----------------------------------------------
# Reverse String

def reverse_string(inp):
    rev_str = Stack()
    for letter in inp:
        rev_str.push(letter)
    final_str = ""
    while not rev_str.is_empty():
        final_str+=rev_str.pop()
    return final_str

inp = "Hello"
print(reverse_string(inp))

# -----------------------------------------------
# Decimal to binary

def dec_to_bin(num):
    binary =Stack()
    remainder=0
    while num > 0:
        remainder = num%2
        binary.push(remainder)
        num =num//2
    final_bin = ""
    while not binary.is_empty():
        final_bin+=str(binary.pop()) 
    return final_bin
print(dec_to_bin(242))
        