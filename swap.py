def swap():

    print('\nWelcome to the file swapper app.')
    path1 = input('Enter the path of the first file :- ')
    file1 = open(path1, "r")
    data1=file1.read()

    path2 = input('Enter the path of the second file :- ')
    file2 = open(path2, "r")
    data2=file2.read()

    //data1 = (file1)
    //data2 = (file2)

    file1 = open(path1, 'w')
    file1.write(data2)

    file2 = open(path2, 'w')
    file2.write(data1)

    print('\nThe data of the files have been swapped successfully')

swap()
