#creating an array

a=[1,2,3,5,6,7]

# coverting array to bytearray not bytes
x=bytearray(a)

#define a print function to reuse ahead

def printing():
    for i in x:
        print(i)

printing()

#editing bytearray

x[0]=99
x[1]=100

printing()

