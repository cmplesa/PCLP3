import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cerinta 1

filename = 'train.csv'
def request1(df):
    nr_cols = df.shape[1]
    # iau numarul de coloane
    print(f'Number of columns: {nr_cols}')
    data_types = df.dtypes
    # iau numarul de tipuri de date
    print('Data types:')
    print (data_types)
    print('\n')
    # aflu numaru de valori lipsa
    missing_values = df.isnull().sum()
    print(f'Missing values: \n{missing_values}')
    nr_rows = df.shape[0]
    # aflu numarul de linii
    print(f'Number of rows: {nr_rows}')
    # daca are/nu are duplicatele
    has_duplicates = df.duplicated().sum()
    print(f'Has duplicates: {has_duplicates}')

# Cerinta 2
def request2(df):
    # procentajul de supravietuitori
    survived = df['Survived'].value_counts(normalize=True) * 100
    print(f'Survived: \n{survived}')
    # procentajul din fiecare clasa
    pclass = df['Pclass'].value_counts(normalize=True) * 100
    print(f'Pclass: \n{pclass}')
    # procentajul fiecarui sex
    sex_percent = df['Sex'].value_counts(normalize=True) * 100
    print(f'Sex percentage:\n{sex_percent}')
    
    # realizare grafic pentru vizualizarea rezultatelor
    ig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # Realizeaza un grafic cu procentajul de supraviețuitori
    axs[0].bar(survived.index, survived.values)
    axs[0].set_title('Survived percentage')

    # Realizeaza un grafic cu procentajul fiecărei clase
    axs[1].bar(pclass.index, pclass.values)
    axs[1].set_title('Pclass percentage')

    # Realizeaza un grafic cu procentajul fiecărui sex
    axs[2].bar(sex_percent.index, sex_percent.values)
    axs[2].set_title('Sex percentage')

    # Ajusteaza layout-ul si afiseaza graficele
    plt.tight_layout()
    plt.show()

# Cerinta 3
def request3(df):
    # Selecteaza coloanele numerice din dataframe
    numeric_cols = df.select_dtypes(include=[np.number])
    # Obtine numarul de coloane numerice
    num_cols = len(numeric_cols.columns)
    # Creeaza subplot-uri pentru histograme
    fig, axs = plt.subplots(num_cols, 1, figsize=(20, num_cols*2))
    # Pentru fiecare coloana numerica, creeaza o histograma
    for i, col in enumerate(numeric_cols.columns):
        axs[i].hist(df[col], bins=40, edgecolor='black')
        axs[i].set_title(f'Histogram of {col}')
    # Afiseaza figura
    plt.tight_layout()
    plt.show()

def request4(df):
    # Obtine lista coloanelor care au valori lipsa
    colos_missing_values = df.columns[df.isnull().any()].tolist()
    for col in colos_missing_values:
       # Calculeaza numarul și procentajul de valori lipsa pentru fiecare coloana
       num_missing = df[col].isnull().sum()
       proportion_missing = num_missing / len(df) * 100
       print(f'Column: {col}, Number of Missing Values: {num_missing}, Proportion: {proportion_missing}%')
    
    for class_ in df['Survived'].unique():
        # Selecteaza randurile care corespund cu clasa curenta
        df_class = df[df['Survived'] == class_]
        for col in colos_missing_values:
            # Calculeaza numarul si procentajul de valori lipsa pentru fiecare coloana si clasa
            num_missing = df_class[col].isnull().sum()
            proportion_missing = num_missing / len(df_class) * 100
            print(f'Class: {class_}, Column: {col}, Number of Missing Values: {num_missing}, Proportion: {proportion_missing}%')

def request5(df):
    # Defineste intervalele de varsta
    bins = [0, 20, 40, 60, df['Age'].max()]
    labels = ['[0-20]', '[20-40]', '[40-60]', '[61, max]']

    # Creeaza o noua coloana 'AgeCategory' care indica intervalul de varsta al fiecarui pasager
    df['AgeCategory'] = pd.cut(df['Age'], bins=bins, labels=labels)
    passengers_per_age_category = df['AgeCategory'].value_counts().sort_index()

    for category, count in passengers_per_age_category.items():
         # Afiseaza numarul de pasageri pentru fiecare categorie de varsta
        print(f'Age Category: {category}, Number of Passengers: {count}')

    # Creeaza un grafic cu numarul de pasageri pentru fiecare categorie de varsta
    plt.figure(figsize=(8, 4))
    passengers_per_age_category.plot(kind='bar')
    plt.title('Number of Passengers per Age Category')
    plt.xlabel('Age Category')
    plt.ylabel('Number of Passengers')
    plt.show()

def request6(df):
    # Defineste intervalele de varsta
    bins = [0, 20, 40, 60, df['Age'].max()]
    labels = ['[0-20]', '[20-40]', '[40-60]', '[61, max]']
    # Creeaza o noua coloana 'AgeCategory' care indica intervalul de varsta al fiecarui pasager
    df['AgeCategory'] = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)
    # Selecteaza pasagerii de sex masculin
    df_males = df[df['Sex'] == 'male']
    # Calculeaza numarul total de barbati pe categorii de varsta
    total_males_per_age_category = df_males['AgeCategory'].value_counts().sort_index()
    # Selecteaza barbatii supravietuitori
    df_survived_males = df_males[df_males['Survived'] == 1]
    # Calculeaza numarul de supravietuitori pe categorii de varsta
    survivors_per_age_category = df_survived_males['AgeCategory'].value_counts().sort_index()
    # Calculeaza rata de supravietuire pe categorii de varsta
    survival_rate_per_age_category = survivors_per_age_category / total_males_per_age_category * 100    
    # Afiseaza graficul cu rata de supravietuire pe categorii de varsta pentru barbati
    plt.figure(figsize=(10, 6))
    survival_rate_per_age_category.plot(kind='bar')
    plt.title('Survival Rate per Age Category for Males')
    plt.xlabel('Age Category')
    plt.ylabel('Survival Rate')
    plt.show()
 
def request7(df):
    # Selecteaza copiii (varsta < 18 ani)
    df_children = df[df['Age'] < 18]
    # Selecteaza adultii (varsta >= 18 ani)
    df_adults = df[df['Age'] >= 18]

    survival_rate_children = df_children['Survived'].mean() * 100
    survival_rate_adults = df_adults['Survived'].mean() * 100

    print(f'Survival Rate for Children: {survival_rate_children}%')
    print(f'Survival Rate for Adults: {survival_rate_adults}%')

    plt.figure(figsize=(10, 6))
    plt.bar(['Children', 'Adults'], [survival_rate_children, survival_rate_adults])
    plt.title('Survival Rate for Children and Adults')
    plt.xlabel('Category')
    plt.ylabel('Survival Rate (%)')
    plt.show()

def request8(df):
    # se grupeaza dataframe-ul df pe baza valorilor din cele 2 coloane si dupa selecteaza coloana age din fiecare grup
    #  si aplica o functie care inlocuieste valorile lipsa cu media varstei pentru grupul respectiv
    df['Age'] = df.groupby(['Survived', 'Pclass'])['Age'].transform(lambda x: x.fillna(x.mean()))

    # Pentru fiecare coloana categorica, inlocuieste valorile lipsa cu cea mai frecventa valoare in aceeasi clasa
    categorical_columns = df.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        # Inlocuieste valorile lipsa cu cea mai frecventa valoare din aceeasi clasa si prin groupby se grupeaza dupa clasa
        df[column] = df.groupby('Pclass')[column].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "Unknown"))

    return df
    
import re

def request9(df):
    # Creeaza o noua coloana 'Title' care extrage titlul din nume
    df['Title'] = df['Name'].apply(lambda x: re.search(' ([A-Za-z]+)\.', x).group(1))

    # Defineste o mapare a titlurilor la genuri
    title_to_gender = {
        'Mr': 'male',
        'Mrs': 'female',
        'Miss': 'female',
        'Master': 'male',
        'Don': 'male',
    }

    # Creeaza o noua coloana 'TitleMatchesSex' care indica daca titlul corespunde cu genul
    # daca titlul nu exista returneaza unknown
    # se compara valoarea obtinuta cu valoarea din coloana 'Sex' a randului obtinut
    df['TitleMatchesSex'] = df.apply(lambda row: title_to_gender.get(row['Title'], 'unknown') == row['Sex'], axis=1)
    # Afiseaza numarul de titluri care corespund si nu corespund cu genul
    print(df['TitleMatchesSex'].value_counts())
    # Afiseaza un grafic cu numarul de fiecare titlu
    plt.figure(figsize=(10, 6))
    df['Title'].value_counts().plot(kind='bar')
    plt.title('Count of Each Title')
    plt.xlabel('Title')
    plt.ylabel('Count')
    plt.show()

import seaborn as sns

def request10(df):
    # Creeaza o noua coloana 'IsAlone' care indica daca un pasager nu are membri ai familiei la bord
    df['IsAlone'] = (df['SibSp'] + df['Parch'] == 0).astype(int)

    # Calculeaza rata de supravietuire pentru pasagerii care sunt singuri si nu sunt singuri
    survival_rate_alone = df[df['IsAlone'] == 1]['Survived'].mean() * 100
    survival_rate_not_alone = df[df['IsAlone'] == 0]['Survived'].mean() * 100

    # Afiseaza rezultatele
    print(f'Survival Rate for Passengers Who Are Alone: {survival_rate_alone}%')
    print(f'Survival Rate for Passengers Who Are Not Alone: {survival_rate_not_alone}%')

    # Afiseaza graficul cu rata de supravietuire pentru pasagerii care sunt singuri si nu sunt singuri
    plt.figure(figsize=(10, 6))
    plt.bar(['Alone', 'Not Alone'], [survival_rate_alone, survival_rate_not_alone])
    plt.title('Survival Rate for Passengers Who Are Alone vs. Not Alone')
    plt.xlabel('Is Alone')
    plt.ylabel('Survival Rate (%)')
    plt.show()

    # Investigheaza relatia dintre tarif, clasa si statutul de supravietuire pentru primele 100 de inregistrari
    sns.catplot(x='Pclass', y='Fare', hue='Survived', data=df.head(100), kind='swarm')
    plt.title('Relationship Between Fare, Class, and Survival Status')
    plt.show()


def read_data(filename):
    df = pd.read_csv(filename)
    return df

def main():
    df = read_data(filename)
    ok = 0
    while ok == 0:
        req_number = input("Enter a request")
        req_number = int(req_number)
        if req_number == 1:
            request1(df)
        elif req_number == 2:
            request2(df)
        elif req_number == 3:
            request3(df)
        elif req_number == 4:
            request4(df)
        elif req_number == 5:
            request5(df)
        elif req_number == 6:
            request6(df)
        elif req_number == 7:
            request7(df)
        elif req_number == 8:
            df = request8(df)
        elif req_number == 9:
            request9(df)
        elif req_number == 10: 
            request10(df)
        elif req_number == 11:
            print(df)
        else:
            ok = 1
            

if __name__ == '__main__':
    main()
