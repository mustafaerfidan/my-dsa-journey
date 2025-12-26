def Insertion_Sort(list1):
    for i in range(1,len(list1)):
        value=list1[i]
        j=i-1
        while j>=0 and list1[j]>value :
            list1[j+1]=list1[j]
            j=j-1
        list1[j+1]=value

             
kartlar = [12, 11, 13, 5, 6]
Insertion_Sort(kartlar)
print("Sıralı Kartlar:", kartlar)