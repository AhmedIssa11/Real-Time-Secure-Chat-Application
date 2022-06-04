import numpy as np
import random
from math import sqrt

XA=1
q=1
a=1

def setXA(num):
    XA = num

def getXA():
    return XA

def setq(num):
    q=num

def getq():
    return q


def seta(num):
    a =num


def geta():
    return a



def power(x, y, p):
    res = 1  # Initialize result

    x = x % p  # Update x if it is more
    # than or equal to p

    while (y > 0):

        # If y is odd, multiply x with result
        if (y & 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


# Utility function to store prime
# factors of a number
def findPrimefactors(s, n):
    # Print the number of 2s that divide n
    while (n % 2 == 0):
        s.add(2)
        n = n // 2

    # n must be odd at this point. So we can
    # skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)), 2):

        # While i divides n, print i and divide n
        while (n % i == 0):
            s.add(i)
            n = n // i

    # This condition is to handle the case
    # when n is a prime number greater than 2
    if (n > 2):
        s.add(n)


# Function to find smallest primitive
# root of n
def findPrimitive(n):
    s = set()




    # Find value of Euler Totient function
    # of n. Since n is a prime number, the
    # value of Euler Totient function is n-1
    # as there are n-1 relatively prime numbers.
    phi = n - 1

    # Find prime factors of phi and store in a set
    findPrimefactors(s, phi)

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):

        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:

            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if (power(r, phi // it, n) == 1):
                flag = True
                break

        # If there was no power with value 1.
        if (flag == False):
            return r


    # If no primitive root found
    return -1






#import randint as rand
#########key generation by alice##########
#q = prime number  ////////// done

#a<q    a primitive root with q  /////////////done
#XA<q-1//done generated randomly
#YA=a^XA mod q //done
#public key pu = {q,a,YA}
#privatekey=XA

#q=10
#generaate prime number

def generate_public_key():

    while (1):
        q = random.randrange(100, 999)
        i = q - 1
        ct = 0

        while (i >= 5):
            if (q % i == 0):
                ct += 1
                break
            i -= 1

        if (ct == 0):
            print("prime random number q generated", q)
            break

    # a primitive root with q

    # Driver Code
    print("finding primitive number for the prime number q")
    a = 15#findPrimitive(q)
    seta(a)
    print(a)


    XA = random.randrange(0, q - 1)
    print("private key XA is generated=", XA)


    # YA=a^XA mod q
    temp = a ** XA
    YA = temp % q



    publickey = [q, a, YA, XA]
    print("public key YA is generated=",YA)
    #print("the public key is",publickey)
    return publickey

#generate_public_key()
########encryption by bob with alice's puplic key ################
#plain text    m<q
#select random integer k     k<q
#calculate K = YA^k mod q
#Calculate C1 = a^k mod q
#calculate C2 = KM mod q
#cipher text =(C1.C2)
def incrypt_gamal(q,a,YA,text):#{q, a, YA, XA}
    print("=======================================>start el_gammal encrypting")

    text=list(text)

    #print(text)

    asc = []
    for i in range(len(text)):
        asc.append(ord(text[i]))

    # M=len(text)#M calc
    M = asc

    # random integer k
    k = random.randrange(0, q)

    print("k generating must be between 0 ,q is generated ", k)
    # calculate K
    temp = YA ** k
    K = temp % q  # Kcalculated

    print("K = ", K)

    temp = a ** k
    C1 = temp % q  # C1 calculated
    print("generated Cipher 1= ", C1)

    # C2 calculation

    C2 = []
    for i in range(len(M)):
        temp = K * M[i]
        out = temp % q
        C2.append(out)

    # temp = K*M
    # C2 = temp %q
    print("generated Cipher 2 = ", C2)




    returnedvalue = ""
    returnedvalue+= str(C1) + ","

    for i in range(len (C2)):
        returnedvalue += str(C2[i])+","

    returnedvalue+=  str(q)

    print("returned value = ",returnedvalue)
    return returnedvalue





#{m,k,K,C1,C2} done
#cipher text = (C1,C2)







#########decryption by alice by alice's private key###############
#ciper text = (C1.C2)
#calculate K = C1^XA mod q
#plain text M=(c2*k^-1) mod q

def decrept_gamal(messagecopy,XA):
    #{q, a, YA, XA}
    print("======================================================>start decryption")
    #print("coming messagecopy=",messagecopy)
    #
    tempmessage = messagecopy.split(",")

    C1 = int(tempmessage[0])
    q=int(tempmessage[-1])
    C2=[]
    for i in range(len(tempmessage)):
        if i!=0 and i!=len(tempmessage)-1:
            C2.append(int(tempmessage[i]))






    print("tempmessage after spliting",tempmessage)

    #C2 = [int(i) for i in C2]


    #q=getq()
    #XA=getXA()

    #q = int(tempmessage[2])




    #print("full message=", messagecopy)
    print("Received Cipher 1 = ", C1)
    print("Received Cipher 2 = ", C2)

    #print("Q = ", q)
    #print("current XA",XA)

    temp = C1 ** XA
    #print("C1 power XA=",temp)
    K = temp % q
    print("K = ", K)
    # kinverse = q% K
    kinverse = K
    ct = 1
    while ((kinverse * ct) % q != 1):
        ct += 1

    kinverse = ct
    print("finding K inverse= ", kinverse)

    output = []
    for i in range(len(C2)):
        temp = C2[i] * kinverse
        letter = temp % q
        output.append(letter)

    # temp= C2 * kinverse
    # line = temp % q

    print("the output is", output)

    decryptedText = ""
    for i in range(len(output)):
        temp = chr(output[i])
        decryptedText = decryptedText + temp
        # decryptedText.append(temp)

    print("Decrypted Text =", decryptedText)

    return decryptedText




