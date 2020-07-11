def write_to_file(filename,myname,myage,major):
    outfile = open(filename, 'w')
    outfile.write("My name is "+ myname +"\n")
    outfile.write("My age is" + str(myage) + "\n")
    outfile.write("I am majoring" + major + "\n")
    
    outfile.close()
    