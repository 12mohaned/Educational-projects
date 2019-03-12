# a program for counting number of items in file can track  progress how many projects you do for example
import os
counter = 0
i = input("if you want to continue click any button else click q : ")
while ( i != "q"):
    #location of file
    file_path = input("where it's located ?")
    file_attribute = input("what is the attribute ? ex : pdf ,jpg , png ")
    #file type
    x = os.listdir("/Users/mohanedmashaly/" +file_path)
    for y in x :
        #counting every project or file you created
         if(y[y.find('.'):len(y)] == file_attribute or y[y.find('.'):len(y)] == file_attribute.upper() ):
             counter+=1
    i = input("if want to quit click q else click any other word")
    print("number of " + file_attribute[1:len(file_attribute)]+ " programs is " + str(counter))
 
