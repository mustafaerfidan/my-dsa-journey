def Merge_Sort(liste):
    if len(liste)<=1:
        return liste
    
    orta=len(liste)//2
    sol=liste[:orta]
    sag=liste[orta:]
    sirali_sol=Merge_Sort(sol)
    sirali_sag=Merge_Sort(sag)
    return birleştir(sirali_sol,sirali_sag)
    
def birleştir(list1,list2):
    result=[]
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i]<list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1
    if i==len(list1):
       result= result + list2[j:]
    elif j==len(list2):
        result = result + list1[i:]
    return result

a=[38, 27, 43, 3, 9, 82, 10]
print(Merge_Sort(a))