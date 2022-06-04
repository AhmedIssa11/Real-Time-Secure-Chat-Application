
from email.message import Message
from random import randint
import math
from unicodedata import decimal
import  binascii
  # String to hexadecimal converstion
def str2hex(word):
    word_2byte = bytes(word,'ascii')  
    word_hex = binascii.hexlify(word_2byte).decode().upper()
    return word_hex
    
# Hexadecimal to binary conversion
def hex2bin(s):
    mp = {'0' : "0000",
        '1' : "0001",
        '2' : "0010",
        '3' : "0011",
        '4' : "0100",
        '5' : "0101",
        '6' : "0110",
        '7' : "0111",
        '8' : "1000",
        '9' : "1001",
        'A' : "1010",
        'B' : "1011",
        'C' : "1100",
        'D' : "1101",
        'E' : "1110",
        'F' : "1111" }
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin
    
# Binary to hexadecimal conversion
def bin2hex(s):
    mp = {"0000" : '0',
        "0001" : '1',
        "0010" : '2',
        "0011" : '3',
        "0100" : '4',
        "0101" : '5',
        "0110" : '6',
        "0111" : '7',
        "1000" : '8',
        "1001" : '9',
        "1010" : 'A',
        "1011" : 'B',
        "1100" : 'C',
        "1101" : 'D',
        "1110" : 'E',
        "1111" : 'F' }
    hex = ""
    for i in range(0,len(s),4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
    return hex

# Binary to decimal conversion
def bin2dec(binary):

    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

# Decimal to binary conversion
def dec2bin(num):
    res = bin(num).replace("0b", "")
    if(len(res)%4 != 0):
        div = len(res) / 4
        div = int(div)
        counter =(4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res 
def hexadecimalToDecimal(hexval):

    # Finding length
    length = len(hexval)

    # Initialize base value to 1,
    # i.e. 16*0
    base = 1
    dec_val = 0

    # Extracting characters as digits
    # from last character
    for i in range(length - 1, -1, -1):

        # If character lies in '0'-'9',
        # converting it to integral 0-9
        # by subtracting 48 from ASCII value
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base

            # Incrementing base by power
            base = base * 16

        # If character lies in 'A'-'F',converting
        # it to integral 10-15 by subtracting 55
        # from ASCII value
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base

            # Incrementing base by power
            base = base * 16

    return dec_val


def preprocess_message(message,n):
    mes=[]
    m=message
    m=str2hex(m)
    me=hex2bin(m)
    print(me)
    me=hexadecimalToDecimal(m)
    print("message in  decimal: ",me)
    def ConvertToInt(message):
    
        l = len(message)
        arra = []
        i = 0
        while(i<l):
            j=ord(message[i])
            arra.append(j)
            i += 1
        return arra
    mes=ConvertToInt(message)
    print("messege in ASCii :  ",mes)
    s=[str(i) for i in mes]
    stri=int("".join(s))
    print(stri)
    m=stri


###########################################################################################################################









#  x= P=[] + "," +Q=[]+","+phy_n+","+n+","+E+","+D

    message=[]
    Cipher=[]

    #Cipher=[]

    mess=m
    me=m
    ct=0
    ct2=0
    num=n
    while(mess!=0):
        mess//=10
        ct2+=1
    print(ct2)

    while(num!=0):
        num//=10
        ct+=1
    print (ct)

    n_num=10**ct

    ctemp=ct-2
    k=0
    i=0
    no=n_num
    while(k<=ct2):
        mo=str(me)
        message.append(mo[k:ctemp])

        k=ctemp
        ctemp+=ct-1

    pla=[]
    for i in range(len(message)):
        if(message[i]!=""): 
            pla.append(int(message[i]))   
    print(pla)

    return pla,mes


def calc():
    j=999

    def checkprime_p(p):
        for i in range(100,j):
            if(p==i):
                return True
                
            if(p%i==0):
                return False
    def checkprime_q(q):
        for i in range(j,j*10):
            if(q==i):
                return True
                
            if(q%i==0):
                return False
    
    for k in range(j):
        p=randint(100,j)
        q=randint(j,j*10)

        if(p!=q):
            if(checkprime_p(p)==True) &  (checkprime_q(q)==True):
            
                    print("good")
                    break
    
    pr=p
    counter=0
    P=[971,157,127,211,421]
    Q=[4783,3709,7547,6869,3001]
    r=randint(0,4)











    n=P[r]*Q[r]
    num=n
    phy_n=(P[r]-1)*(Q[r]-1)
 
    def GCD(m,n):
            if(m==0):
                return n
            return GCD(n%m,m)


            
            

    for e in range(2,phy_n):
            if(GCD(e,phy_n)==1):         
                E = e
                break














    def calc_d(E,phy_n):


        a,bhy,u= 0,phy_n,1
        e=E
        while (e>0):
            R=bhy//e
            e,a,bhy,u= bhy%e,u,e,a-R*u
        if(bhy==1):
            return a%phy_n


                    

        # for d in range(2,phy_n):
        #     res=(E*d)%phy_n
        #     if(res==1):
        #         D=d
        #         break
        # return D
    D = calc_d(E,phy_n)


    return n,E,D
message="HEY"
n,E,D=calc()
pla,mes=preprocess_message(message,n)

def to_cipher(E,n,pla):
    c=[] 
    for k in range(len(pla)):
        ce=pla[k]**E%n
        c.append(ce)   
    return c
Cipher= to_cipher(E,n,pla)
print("cipher is ",Cipher)

def to_plain(D,n,Cipher,mes):
    d_inbin=dec2bin(D)
    flag=0
    res=1
    res2=1
    inbin=[]
    inbin = list(map(int,d_inbin))
    print(inbin)
    i=0
    plain=[]
    l=0 

    # for i in Cipher:
    #     temp=Cipher[l]**D
    #     m=temp%n
    #     plain.append(m)
    #     l+=1
    # return plain

    
    print("from RSA:",Cipher)

    for k in range(len(Cipher)):  
        i=0 
        res=1
        for i in range(len(inbin)):


            if(inbin[i]==1):
                flag=1
                
            if(flag==1):
            
                if(inbin[i]==1):
                    res=(res**2)%n

                    res=(res*Cipher[k])%n

        
                if(inbin[i]==0):
                    res=(res**2)%n
        


        plain.append(res)    






    print("plain back: ",plain)
    s = [str(i) for i in plain]
    strplain="".join(s)

    tex=[]
    temp=[]
    temp=mes
    k=0
    textt=[]

    for i in range(len(mes)):
        textt.append(mes[i])
    for i in range(len(mes)):
        count=0
        k=0
        while(temp[i]!=0):
            temp[i]//=10
            count+=1  
        if(strplain[i]!=''):
                if(mes[i]==int(strplain[k:k+count])):
                    tex.append(mes[i])

        k+=count




    print("textt: ",textt)


    string_ints = [chr(int) for int in textt]
    str_of_ints = "".join(string_ints)
    print(str_of_ints)
    return str_of_ints
plain = to_plain(D,n,Cipher,mes)
print("Plain back: ",plain)










   

    


 
   



                


# P=[]
# Q=[]  

# P,Q,phy_n,n,E,D=calc() 
mess="how old are you soly iam tell you that you are so good student and each one have a good day and it's so good yaaaaaaaaa issssaaaaaaaaa"
#RSA(mess,n,E,D)







