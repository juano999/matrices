#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=1
b=1.0


# In[2]:


a


# In[3]:


b


# In[5]:


type(a)


# In[6]:


type(b)


# In[7]:


c=2+3


# In[8]:


c


# In[9]:


c= 2-3
c


# In[10]:


c=2**3


# In[11]:


c


# In[12]:


c=2//3
c


# In[13]:


c=2%3
c


# In[14]:


3>2
3<2
2>=1+1
4-2<=1
6/2 != 3


# In[15]:


print(3>2)
print(3<2)
print(2>=1+1)
print(4-2<=1)


# In[16]:


3>2


# In[17]:


print(3>2)
print(3<2)
print(2>=1+1)
print(4-2<=1)


# In[18]:


print(4== 3+1 > 2)
print(2!=1+1>0)


# In[19]:


cadena= int(input("ingrese su edad"))


# In[20]:


peso = float(input("ingrese su peso  en kg: "))
estatura= float(input("ingrese su altura  en metros: "))
imc = peso / (estatura**2)
print(round(imc))


# In[26]:


peso = float(input("ingrese su peso  en kg: "))
estatura= float(input("ingrese su altura  en metros: "))
imc = peso / (estatura**2)
print("Tu indice de masa corporal es " + str(round(imc, 2)))


# In[27]:


s="Hola a (todos)"
s


# In[28]:


type(s)


# In[29]:


s.lenght


# In[32]:


s.find("a ")


# In[33]:


s.count


# In[34]:


cadena1="Python"


# In[35]:


cadena1


# In[39]:


print(cadena1[:1])


# In[40]:


print(cadena1[-1:])


# In[41]:


print(cadena1[:-1])


# In[44]:


print(cadena1[:2*-2])


# In[46]:


s= s.replace("Hola ", "Chao")
s


# In[47]:


cadena=" esta cadena tiene espacios a los lados "
cadena.strip()


# In[48]:


cadena.lstrip()


# In[49]:


cadena.rstrip()


# In[50]:


cadena.upper()


# In[51]:


cadena.lower()


# In[52]:


cadena.capitalize()


# In[53]:


nombres = "Carlos|Cristina|Rodrigo|Hugo"
nombres.split("|")


# In[54]:


caracter = "|"
nombres2=["Carlos","Cristina","Rodrigo"]
print(caracter.join(nombres2))


# In[55]:


cuadrados=[1,4,9,16,25]
cuadrados


# In[56]:


cuadrados[-1]


# In[57]:


cuadrados[-3]
cuadrados[2]


# In[58]:


cubos=[1,8,27,64]


# In[59]:


cubos.append(6**3
            )


# In[60]:


cubos


# In[61]:


lista1 = [1,2,3]
lista2 = [a,b,c]


# In[62]:


x=[lista1,lista2]


# In[63]:


x[1
 ]


# In[64]:


x[1]


# In[65]:


x[2]


# In[67]:


x[1][3]


# In[4]:


x[0]


# In[69]:


palabras =["gato", "perro", "campana"]
for p in palabras:
    print (p, len(p))


# In[72]:


for i in range(10):
    print(i)


# In[3]:


x[1]


# In[5]:



x=[[],[],[]]


# In[6]:


x[0][0]=1


# In[7]:


c=[1,2,3]
c.append(4)
c


# In[2]:


b=[]


# In[3]:


b.append([1,2,4,5])
b.append([-1,-2])


# In[4]:


b[1][0]


# In[5]:


b.append(int(input("numero: ")))


# In[6]:


b[2]


# In[7]:


b[0].append(9)


# In[8]:


b[0]


# In[9]:


f=[0]


# In[12]:


g=[[]]


# In[13]:


g[0].append([1,2])


# In[ ]:




