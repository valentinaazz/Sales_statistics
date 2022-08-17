import pandas as pd
#
# # IMPORTUL UNUI FISIER CSV
#
df = pd.read_csv('export_comenzi.csv')
print(df)

# -----------------------------------------------------------------------------------------------------------------------

# UTILIZAREA LISTELOR

produse = df['Order Items: Product Name.1']
print('-----produse-----')
print(produse)

# Transformare in lista
lista_produse = list(produse)

# Adaugare produs in lista
lista_produse.append('Fusta midi 9675 - XS')
print('\nAdaugare produs la final')
print(lista_produse)

lista_produse.insert(0, 'Fusta midi 9675 - XS')
print('\nAdaugare produs pe prima pozitie')
print(lista_produse)

# Stergere produs din lista
print('\nStergere produs - TRENING SCURT GRI 8937 - S')
lista_produse.remove('TRENING SCURT GRI 8937 - S')
print(lista_produse)

print('\nPop-', lista_produse.pop())

# Stergere lista
del lista_produse

# -----------------------------------------------------------------------------------------------------------------------

# DEFINIREA SI APELAREA FUNCTIILOR
# UTILIZAREA STRUCTURILOR CONDITIONALE
# UTILIZAREA STRUCTURILOR REPETITIVE

# Sa se defineasca functia care calculeaza numarul de bucati vandute
# din marimea introdusa ca parametru
def vanzariMarimi(lista, marime):
    nrProduse = 0;
    for produs in lista:
        if str(produs).count(marime)!=0:
            nrProduse += 1
    print('S-au vandut '+str(nrProduse)+' articole din marimea '+marime)
    return nrProduse


lista_produse = list(produse)

marimea_S=vanzariMarimi(lista_produse,"S")
marimea_M=vanzariMarimi(lista_produse,"M")

if(marimea_S>marimea_M):
    print('Avem o vanzare mai mare de articole marimea S')
else:
    print('Avem o vanzare mai mare de articole marimea M')


# -----------------------------------------------------------------------------------------------------------------------


# ACCESAREA DATELOR CU LOC SI ILOC


# Sa se selecteze randurile 1, 3, 5 si coloana 2
print("-----randurile 1, 3, 5 si coloana 2-----")
print(df.iloc[[0, 2, 4], [1]])

# Sa se selecteze pentru randurile 10-25 primele 4 coloane
print("\n-----randurile 10-25 primele 4 coloane-----")
print(df.iloc[10:26, :4])

# Sa se afiseze inregistrarile 2, 4, 6 pentru coloana DATE
print("\n-----inregistrarile 6, 8, 9 pentru coloana DATE-----")
print(df.loc[[5, 7, 8], ["Date"]])

# Sa se afiseze inregistrarea 10 pentru coloanele First Name, Last name
print("\n-----inregistrarea 10 pentru coloanele First Name, Last name-----")
print(df.loc[[9], ["First Name", "Last Name"]])

# Sa se afiseze numele clientilor care au plasat comanda in Bucuresti
print("\n-----numele clientilor care au plasat comanda in Bucuresti-----")
print(df.loc[(df['City'] == 'Bucuresti'), ['First Name']])

# Sa se afiseze cantitatea comandata pentru comenzile care au valoarea peste 800 de lei
print("\n-----cantitatea comandata pentru comenzile care au valoarea peste 800 de lei-----")
print(df.loc[(df['Total'] > 800), ['Quantity']])

# Sa se selecteze numele clientilor care au comandat peste 5 bucati si au plasat comanda in Brasov
print("\n-----numele clientilor care au comandat peste 5 bucati si au plasat comanda in Brasov-----")
print(df.loc[(df['Quantity'] > 5 & (df['City'] == 'Brasov')), ['First Name', 'Last Name']])

# Sa se afiseze totalul comenzilor care au fost plasate in Iasi si Pitesti
print("\n-----totalul comenzilor care au fost plasate in Iasi si Pitesti-----")
print(df.loc[df['City'].isin(['Iasi', 'Ploiesti']), ['Total']])

# -----------------------------------------------------------------------------------------------------------------------


# MODIFICAREA DATELOR IN PACHETUL PANDAS


# Sa se modifice statusul comenzilor care au totalul peste 1500 de lei
print("\n-----statusul initial comenzilor care au totalul peste 1500 de lei-----")
print(df.loc[(df['Total'] > 1500), ['Status']])
df.loc[(df['Total'] > 1500), ['Status']] = "pending"
print("\n-----statusul comenzilor care au totalul peste 1500 de lei dupa modificare-----")
print(df.loc[(df['Total'] > 1500), ['Status']])

# Sa se ofere un discount comenzilor care contin mai mult de 10 bucati
print("\n-----valoarea initiala a comenzilor-----")
print(df.loc[(df['Quantity'] > 10), ['Total']])
print("\n-----valoarea comenzilor dupa discount-----")
df.loc[(df['Quantity'] > 10), ['Total']] = df.loc[(df['Quantity'] > 10), ['Total']] - df.loc[
    (df['Quantity'] > 10), ['Total']] * 0.1
print(df.loc[(df['Quantity'] > 10), ['Total']])

# -----------------------------------------------------------------------------------------------------------------------


# TRATAREA VALORILOR LIPSA

print('\n-----inlocuire valori lipsa cu sirul "lipsa"-----')
print(df.fillna('lipsa'))

print('\n-----inlocuire valori lipsa cu media valorilor-----')
valoare_medie = int(df['Total'].mean())
df['Total'] = df['Total'].fillna(value=valoare_medie)
print(df.Total)

# -----------------------------------------------------------------------------------------------------------------------

# STERGEREA DE COLOANE SI INREGISTRARI

# Stergerea coloanelor "Order Items: Product Name"
print('\n-----stergerea coloanelor "Order Items: Product Name"-----')
df1 = df.drop(['Order Items: Product Name.25', 'Order Items: Product Name.26'], axis=1)
print(df1.head())

# Stergerea coloanei Status si salvarea intr-un nou fisier
df2 = df.drop('Status', axis=1)
df2.to_csv('export_df.csv', index=False)

# Stergerea primelor 3 randuri
print('\n-----stergerea primelor 3 randuri-----')
df3 = df.drop([1, 2, 3])
print(df3)

# Stergerea clientilor care au plasat comanda in Ploiesti
print('\n-----stergerea clientilor care au plasat comanda in Ploiesti-----')
df4 = df.set_index('City')
df4.drop('Ploiesti', axis=0, inplace=True)
print(df4)

# -----------------------------------------------------------------------------------------------------------------------


# # PRELUCRARI STATISTICE, GRUPAREA SI AGREGAREA DATELOR IN PACHETUL PANDAS ----------------------------------------------

# Sa se afiseze sumarul statistic pentru totalul comenzilor
print("\n-----sumarul statistic pentru totalul comenzilor-----")
print(df['Total'].describe())

print('\n')

print('Suma totala', df['Total'].sum(), ' lei')
print('Suma medie', df['Total'].mean(), ' lei')
print('Comanda maxima', df['Total'].max(), ' lei')
print('Comanda minima', df['Total'].min(), ' lei')

# Sa se afiseze suma cantitatilor comandate zilnic
print("\n-----suma cantitatilor comandate zilnic-----")
print(df.groupby('Date')['Quantity'].sum())

print("\n-----valoarea maxima cantitatilor comandate zilnic-----")
print(df.groupby('Date')['Quantity'].sum().max())

# Sa se afiseze suma totala a comenzilor zilnice
print("\n-----suma totala a comenzilor zilnice -----")
print(df.groupby('Date')['Total'].sum())

print("\n-----valoarea maxima a comenzilor zilnice -----")
print(df.groupby('Date')['Total'].sum().max())

# Sa se calculeze cantitatea totala comandata la nivel de oras
print("\n-----cantitatea totala comandata la nivel de oras -----")
print(df.groupby(['City']).agg({'Quantity': sum}))

# Sa se calculeze totalul, minimul si maximul comenzilor zilnice
print("\n-----totalul, minimul si maximul comenzilor zilnice -----")
print(df.groupby(['Date']).agg({'Total': [min, max, sum]}))

# # ---------------------------------------------------------------------------------------------------------------------

# # REPREZENTARE GRAFICA A DATELOT CU PACHETUL MATPLOTLIB

import matplotlib.pyplot as plt

# Reprezentarea grafica cantitati comandate
df['Quantity'].plot(kind='hist')
plt.xlabel('Quantity')
plt.show()

# Reprezentarea grafica a totalului comandat la nivel de oras
plot_data=df[df['Quantity']>7]
plot_data=plot_data.groupby('City')['Total'].sum()
plot_data.sort_values().plot(kind='bar')
plt.show()



# # ---------------------------------------------------------------------------------------------------------------------

