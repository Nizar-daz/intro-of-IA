#!/usr/bin/env python
# coding: utf-8

# In[1]:


# question 1: Division par 7

# programme devision par 7
dl=[] 
for i in range(2000, 3200): 
    if (i%7==0) and (i%5!=0):
        dl.append(str(i))
print(dl)
    


# In[3]:


# question 2: Factorielle d'un nombre entier

n = int (input('saisie un nombre: '))
def factorialle(n): 
    if n < 0: 
        print("Factorialle d'un nombre négative n'existe pas")

    elif n == 0: 
        return 1
        
    else: 
        fact = 1
        while(n > 1): 
            fact *= n 
            n -= 1
        return fact 

print("Factorialle de",n,"et", factorialle(n))


# In[4]:


# question 3: Carrée d'un dictionnair de n entier

n = int(input("donner un nombre entier: "))

# on crée un dictionnaire vide pour le nombre n et leur carré
d = dict({})

# on fait le parcourt des entiers de 1 à n
for i in range(1 , n+1):
    d[i] = i*i

print(d)


# In[5]:


# question 4: Supprimer un caractère d'une chaine donnée avec index specifier

chaine = str (input('saisie une chaine de caractère: '))

#calculer la taille de la chaine
n= len(chaine)
print(n)

x = int (input('saisie index de caractère à supprimer: '))

# supprimer un caractère à un index specifique
for i in range(0, n-1):
    if (i == x):
        chaine = chaine[:i] + chaine[i+1:]

print(chaine)


# In[6]:


# question 5: Array to liste

import numpy as np

#creation d'un array numby
tableau_orig = np.array([[0,1], [2, 3], [4, 5]])
print(f'Numpy tableau original:\n{tableau_orig}')

# utiliser methode to_list() 
liste = tableau_orig.tolist()
print(f' liste : {liste}')


# In[7]:


# question 6: Covariance

import numpy as np

# creation des tableaux
tab1 = np.array([0,1,2])
tab2 = np.array([2,1,0])

# covariance par 2 methode
# 1er methode on utlilise stack
table = np.stack((tab1, tab2), axis=0)
np.cov(table)

# 2eme methode cov de deux tableux
np.cov(tab1, tab2)


# In[9]:


# question 7: Racine carrée avec formule sqrt[(2*C*D)/H]

import numpy as np

numbers = input("Donner D: ")
numbers = numbers.split(',')

D_list = []
for D in numbers:
    Q = round(np.sqrt(2 * 50 * int(D) / 30))
    D_list.append(Q)

print(D_list)


# In[ ]:




