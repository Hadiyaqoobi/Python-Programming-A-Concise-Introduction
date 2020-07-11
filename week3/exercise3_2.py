def print_file(filename):
        """ Opens file and prints its contents line by line. """
        infile = open(filename)
        
        for line in infile:
            print(line, end="")
            
        infile.close()   
            
print_file("hellozahra.txt")



def copy_file(infilename, outfilename):
    """ Opens two files and copies one into the other line by line. """
    infile = open(infilename)
    outfile = open(outfilename,'w')
    
    for line in infile:
        outfile.write(line)
        
    infile.close()
    outfile.close()
