def problem3_6(fileName):

    file_n = open(fileName, "r")
    emp = []
    for line in file_n:
        line = line.strip('\n')
        emp.append(line)
        print(len(line))
    f = open('guru.txt',"w+")
    for line in emp:
        f.write(str(len(line))+'\n')


#print(problem3_6('HumptyDumpty.txt'))

# Second attempt:

import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

infile = open(inputfile)
outfile = open(outputfile, 'w')

for line in inputfile:
    line = line.strip("\n")
    outputfile.write(str(len(line)) + "\n")

inputfile.close()
outputfile.close()