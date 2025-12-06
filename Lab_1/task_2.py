# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44 #Мб
Stranis = 100
Strok = 50
Simvol_in_strok = 25
Hranenie_simvol = 4 #б
obem_disk = disk * 1024 * 1024 #Общий обьем на диске в б
odna_kniga = Stranis * Strok * Simvol_in_strok * Hranenie_simvol #Обьем 1 книги в б
resylt = int (obem_disk // odna_kniga)
print("Количество книг, помещающихся на дискету:", resylt)
