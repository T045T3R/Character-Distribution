"""
distribution.py
Author: Johannes Testorf
Credit: Wilson Rimberg

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
letters = input("Please enter a string of text (the bigger the better): ")
letters = letters.lower()
def compare(a, b):
    """
    compare - generic comparison function for testing two elements.
    """
    if b==a:
        return a>=b
    else:
        return b<=a

def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it
                    

acount=str(letters).count('a')
bcount=str(letters).count('b')
ccount=str(letters).count('c')
dcount=str(letters).count('d')
ecount=str(letters).count('e')
fcount=str(letters).count('f')
gcount=str(letters).count('g')
hcount=str(letters).count('h')
icount=str(letters).count('i')
jcount=str(letters).count('j')
kcount=str(letters).count('k')
lcount=str(letters).count('l')
mcount=str(letters).count('m')
ncount=str(letters).count('n')
ocount=str(letters).count('o')
pcount=str(letters).count('p')
qcount=str(letters).count('q')
rcount=str(letters).count('r')
scount=str(letters).count('s')
tcount=str(letters).count('t')
ucount=str(letters).count('u')
vcount=str(letters).count('v')
wcount=str(letters).count('w')
xcount=str(letters).count('x')
ycount=str(letters).count('y')
zcount=str(letters).count('z')



tosort = [acount, bcount, ccount,dcount,ecount,fcount, gcount,hcount,icount,jcount,kcount,lcount,mcount,ncount,ocount,pcount, qcount,rcount,scount,tcount,ucount,vcount,wcount,xcount,ycount,zcount]
poopy = list(zip(tosort,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))
tosort = tosort[::-1]
poopy=poopy[::-1]
bsort(poopy, compare)
letterorder = ([y for x,y in poopy])
numberorder = ([x for x,y in poopy])


n=0
for x in range(0 , 26):
    if numberorder[x]<=numberorder[x+1]:
        print(str(letterorder[x+1])*numberorder[x+1])
        print(str(letterorder[x])*numberorder[x])
        x=x+1
    else:
        if numberorder[x]<=numberorder[x+1] and numberorder[x+1]<=numberorder[x+2]:
            print(str(letterorder[x+2])*numberorder[x+2])
            print(str(letterorder[x+1])*numberorder[x+1])
            print(str(letterorder[x])*numberorder[x])
            x=x+2
        else:
            print(str(letterorder[x])*numberorder[x])
    
    