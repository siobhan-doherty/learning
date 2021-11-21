# find out the reversed form of a string

class myStr(str):
    def __str__(self):
        return self[::-1]


reversed_string = input("Enter something: ")
s = myStr(reversed_string)
print(s)
