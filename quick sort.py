def quick_sort(liste):
    left=[]
    right=[]
    if len(liste)<=1:
        return liste
    
    pivot=liste[len(liste)-1]
    for i in liste[:len(liste)-1]:
        if i<pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left)+ [pivot]+quick_sort(right)



# --- TEST KODU ---
karisik_sayilar = [33, 10, 55, 71, 29, 5, 10, 100]
sirali_sayilar = quick_sort(karisik_sayilar)

print("Karışık:", karisik_sayilar)
print("Sıralı :", sirali_sayilar)