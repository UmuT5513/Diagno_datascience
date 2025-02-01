import numpy as np

np.arange(1, 10, 0.1) #1-10 arasında 0.1 aralıklarla sayılar üretir.

np.linspace(1,10, 8) #1-10 arasını 8 eşit parçaya böler.

np.zeros(5)
np.ones([4,3], dtype=int) # 4x3 boyutunda 1'lerden oluşan bir matris oluşturur.

np.random.rand(10) #0-1 arasında sırasız bir şekilde rastgele 10 sayı üretir.
np.random.randint(100) #0-100 aralığında rastgele bir sayı üretir.

np.eye(5) #5x5 birim(Identity) matris oluşturur.
arr = np.full([3,3], 67, dtype=int) #2x2 boyutunda 67 sayılarından oluşan bir matris oluşturur.

arr.size #eleman sayısını verir.
arr.shape #boyut bilgisini verir.
arr.ndim #boyut sayısını verir.

arr
len(arr) #ilk boyutun eleman sayısını verir.


arr.astype('float') #tip dönüşümü yapar.

arr.tolist() #numpy array'ini listeye dönüştürür.


arr1 = np.random.rand(10)
arr1.sort() # sorting array
print(arr1)


np.empty([2,2]) #2x2 boyutunda boş bir matris oluşturur.

arr2 = np.array([[4,1,6],
                 [2,3,5],
                 [7,8,9]]) #3 boyutlu bir array oluşturur.
arr2.sort(axis=1) #sütuna göre(soldan sağa) sıralama işlemi yapar.
arr2.sort(axis=0) #satıra göre(yukarıdan aşağıya) sıralama işlemi yapar.
print("Original Array:", arr2)

arr2 = np.append(arr2, [[10,11,12]], axis=0) #array'e yeni bir satır ekler.
print("Array after appending:", arr2)



arr3 = np.arange(1, 13).reshape(2,6) #1-12 arasındaki sayıları 2x6 boyutunda bir matris oluşturur.
print("Original Array")
print(arr3, "\n")
# append column wise
col = np.arange(5, 11).reshape(1, 6)
arr3_col = np.append(arr3, col, axis=0) #array'e yeni bir satır ekler.
print("Array after appending the values column wise")
print(arr3_col, "\n")
# append row wise
row = np.array([1, 2]).reshape(2,1)
arr3_row = np.append(arr3, row, axis=1) #array'e yeni bir sütun ekler.
print("Array after appending the values row wise")
print(arr3_row)


# inserting
arr4 = np.array([1,2,3])
arr4 = np.insert(arr4, 1, 5) #array'in 1. index'ine 5 sayısını ekler.
arr4


# reshaping array
arr5 = np.arange(1,17)
print("Original Array: " + str(arr5))
reshaped1 = arr5.reshape(8,2) #1-16 arasındaki sayıları 8x2 boyutunda bir matris oluşturur.
reshaped1.shape

reshaped2 = arr5.reshape(4, arr5.size//4) #1-16 arasındaki sayıları 4x4 boyutunda bir matris oluşturur.
reshaped2.shape


# resizing
arr6 = np.arange(1, 10)
print("Original Array: " + str(arr6))
arr6.resize(3,3) #array'i 3x3 boyutuna dönüştürür.
arr6
#arr6.resize(4,4) #bu işlemi yapamaz çünkü eleman sayısı değişir.
#Numpy arrays can be resized using the resize() function. It returns nothing but changes the original array.


# flatten a two dimensional array
list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 = [9,10,11,12]
arr7 = np.array([list_1, list_2, list_3])
print(arr7)
print("Flattened Array: " + str(arr7.flatten())) # çok boyutlu bir array'i 1 boyutlu hale getirir.


# transpose
arr8 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print("Original Array: ")
print(arr8)
print("Transposed Array: " + str(arr8.T)) #array'in transpozunu alır.


# combining and splitting arrays
np.concatenate((arr8, arr8), axis=0) #array'leri birleştirir.
np.split(arr8, 3, axis=0) #array'i 3 parçaya böler. Bir listenin içinde 3 adet array döner.
np.hsplit(arr8, 3) #array'i sütunlara göre 3 parçaya böler. Bir listenin içinde 3 adet array döner.
np.vsplit(arr8, 3) #array'i satırlara göre 3 parçaya böler. Bir listenin içinde 3 adet array döner.


# indexing, slicing and subsetting
#subsetting
print(arr8)
print("Elements are:", arr8[np.array([1, 2, -3])]) #array'in 1., 2. ve sondan 3. elemanlarını getirir.
#slicing  a[start:stop:step]
print(arr8[0:2, 0:2]) #array'in 0. ve 1. satırlarını ve 0. ve 1. sütunlarını getirir.
# indexing 1)integer indexing 2)boolean indexing
arr9 = np.array([[1,2],[3,4], [5,6]])
print(arr9[[0,1,2], [0,1,0]]) #array'in 0,0; 1,1 ve 2,0 elemanlarını getirir.

arr10 = np.arange(10,101,10)
arr10[arr10>50] #50'den büyük elemanları getirir.



arr9.view() #array'in bellekteki adresini verir.
arr9.copy() #array'i kopyalar.






