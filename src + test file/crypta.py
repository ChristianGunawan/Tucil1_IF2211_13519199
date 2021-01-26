#Nama       :   Christian Gunawan
#NIM        :   13519199
#Kelas      :   04
#Nama file  :   crypta.py
#Deskripsi  :   Tugas Kecil 1 Strategi Algortima IF2211 - Cryptarithmetic Solver dengan Algoritma Brute Force

import timeit

# membaca file
def read_input():
    listkata = []
    f = open("sample8.txt", "r") #file yang akan dibaca
    f1 = f.readlines()
    for word in f1:
        listkata.append(word.replace("\n", "").replace("+","").replace(" ",""))
    listkata.pop(-2) #membuang "----"
    return listkata, f1 

#convert to string
def conv(w, camp):
    result = 0
    k = 1
    balikkan = w[::-1]
    for x in range(len(balikkan)):
        result += camp[balikkan[x]] * k
        k *= 10
    return result
    
# membuat fungsi permutasi
def permutations(ez, r=None):
    p = tuple(ez) #mengubah menjadi tuple
    n = len(p) #menghitung banyak pada ez
    r = n if r is None else r
    if r > n:
        return
    sin = list(range(n)) 
    c = list(range(n, n-r, -1))
    yield tuple(p[i] for i in sin[:r])
    while n:  #
        for i in reversed(range(r)):
            c[i] -= 1
            if c[i] == 0:
                sin[i:] = sin[i+1:] + sin[i:i+1]
                c[i] = n - i
            else:
                j = c[i]
                sin[i], sin[-j] = sin[-j], sin[i]
                yield tuple(p[i] for i in sin[:r])
                break
        else:
            return

def solve2(equation):
    join = ''.join(equation) #Semua list jadi satu
    sets = set(join) #Semua join jadi hanya satu huruf
    List = tuple(sets)
    angka = list(range(10)) # Range angka hanya boleh 0-9
    trying = 0 # Menghitung jumlah percobaan
    n = len(List) 
    for poss in permutations(angka,n):
        word_dict = dict(zip(List,poss)) # Membentuk <key:value> dengan key adalah huruf dan value adalah angka
        count = 0
        for i in range(len(equation)):
            if(word_dict[equation[i][0]] == 0) :
                count += 1
        if count != 0:
            continue
        else: #mencari operand 
            result = 0
            sols = []
            for i in range(len(equation)-1):
                result += conv(equation[i],word_dict)
                sols.append(conv(equation[i],word_dict))
            
            if (result == conv(equation[-1], word_dict)):
                sols.append(conv(equation[-1], word_dict))
                return sols, trying
        trying += 1 #
    

if __name__ == '__main__':
    baca = read_input() 
    for word in baca[1]:  
        print(word, end = '')
    print('\n')
    #Start Menghitung
    start = timeit.default_timer() #start timer
    result = solve2(baca[0]) #Output fungsi read_input pertama menjadi parameter fungsi cryparithms solver
    end = timeit.default_timer() #end timer
    sols = result[0] 
    for i in range(len(sols)):
        if(i != len(sols) - 2):
            print(str(sols[i]))
        else:
            print(str(sols[i]) + "+")
            print("-----")
    print("\n{} second(s) in {} experiment(s)".format(end - start, result[1])) #hasil timer dan result pada try
else:
    print("") #jika gagal maka output kosong
    
