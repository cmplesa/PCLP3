### Plesa Marian Cosmin 311CA
# TASK 1

## Cerinta 1

    Functia calculeaza si afiseaza numarul de coloane folosind proprietatea shape, afiseaza tipurile de date ale coloanelor folosind metoda dtypes. Dupa aceea, calculeaza si afiseaza numarul de valori lipsa pentru fiecare coloana folosind metoda isnull().sum(). In continuare, afiseaza numarul de randuri si verifica daca exista randuri duplicate folosind metoda duplicated().sum().

## Cerinta 2

    Functia calculeaza procentele de supravietuitori, distributia pe clase si distributia pe sexe, apoi afiseaza aceste statistici si creeaza grafice corespunzatoare. Foloseste Pandas pentru a calcula distributiile procentuale utilizand value_counts(normalize=True), iar Matplotlib pentru a crea trei grafice cu bare intr-o singura figura, reprezentand procentele calculate.

## Cerinta 3

    Functia request3 genereaza histograme pentru toate coloanele numerice. Foloseste select_dtypes pentru a selecta coloanele numerice, apoi creeaza subgrafice pentru fiecare coloana numerica intr-o figura verticala. Pentru fiecare coloana, creeaza o histograma folosind hist cu 40 de bin-uri si margini negre. Titlul fiecarei histograme indica numele coloanei. Layout-ul este ajustat cu plt.tight_layout pentru a preveni suprapunerea elementelor si afiseaza graficele.

## Cerinta 4

    Functia request4 analizeaza valorile lipsa. Identifica coloanele cu valori lipsa folosind isnull().any(), apoi calculeaza si afiseaza numarul si procentajul de valori lipsa pentru fiecare coloana. In continuare, pentru fiecare valoare unica din coloana 'Survived', selecteaza randurile corespunzatoare si calculeaza numarul si procentajul de valori lipsa pentru fiecare coloana in functie de clasa de supravietuire.

## Cerinta 5

    Functia request5 analizeaza distributia pasagerilor pe categorii de varsta. Defineste intervalele de varsta si creeaza o coloana noua, AgeCategory, folosind pd.cut pentru a indica intervalul de varsta al fiecarui pasager. Calculeaza numarul de pasageri pentru fiecare categorie de varsta si afiseaza aceste informatii. Creeaza un grafic cu bare care ilustreaza numarul de pasageri pentru fiecare categorie de varsta, adaugand titlu si etichete pentru axe, si afiseaza graficul.

## Cerinta 6

    Functia request6 analizeaza rata de supravietuire pe categorii de varsta pentru barbati. Defineste intervalele de varsta si creeaza coloana AgeCategory folosind pd.cut. Selecteaza pasagerii de sex masculin si calculeaza numarul total de barbati pe categorii de varsta. Selecteaza barbatii supravietuitori si calculeaza numarul de supravietuitori pe categorii de varsta. Calculeaza rata de supravietuire pentru fiecare categorie de varsta si creeaza un grafic cu bare pentru a ilustra aceste rate, adaugand titlu si etichete pentru axe, si afiseaza graficul.

## Cerinta 7

    Functia request7 analizeaza rata de supravietuire pentru copii si adulti. Selecteaza copiii (varsta < 18 ani) si adultii (varsta >= 18 ani) din DataFrame. Calculeaza rata de supravietuire pentru fiecare grup, apoi afiseaza aceste rate. Creeaza un grafic cu bare pentru a ilustra ratele de supravietuire ale copiilor si adultilor, adaugand titlu si etichete pentru axe, si afiseaza graficul.
    
## Cerinta 8

    Functia request8 completeaza valorile lipsa. Pentru coloana Age, valorile lipsa sunt completate cu media varstei pentru fiecare combinatie de Survived si Pclass folosind groupby si transform. Pentru coloanele categorice, valorile lipsa sunt inlocuite cu cea mai frecventa valoare din aceeasi clasa (Pclass) folosind mode si fillna. Functia returneaza DataFrame-ul completat.

## Cerinta 9

    Functia request9 analizeaza corespondenta dintre titlu si gen. Extrage titlul din coloana Name si creeaza o coloana noua, Title. Defineste o mapare a titlurilor la genuri si creeaza coloana TitleMatchesSex, care indica daca titlul corespunde cu genul pentru fiecare rand. Afiseaza numarul de titluri care corespund si nu corespund cu genul. Creeaza un grafic cu bare pentru a ilustra numarul de aparitii ale fiecarui titlu, adaugand titlu si etichete pentru axe, si afiseaza graficul.

## Cerinta 10

    Functia request10 analizeaza rata de supravietuire in functie de statutul de a fi singur sau nu. Creeaza coloana IsAlone pentru a indica daca un pasager nu are membri ai familiei la bord. Calculeaza si afiseaza rata de supravietuire pentru pasagerii singuri si cei care nu sunt singuri. Creeaza un grafic cu bare pentru a ilustra aceste rate de supravietuire. Folosind Seaborn, creeaza un grafic catplot pentru a investiga relatia dintre tarif, clasa si statutul de supravietuire pentru primele 100 de inregistrari, si afiseaza graficul.