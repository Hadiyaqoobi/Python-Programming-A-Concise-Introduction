ascars = {"Ford" : "Mustang","Mazda" : "Miata", "Scion" : "FR-S", 
"Subaru" : "BRZ","Dodge" : "Challenger", "Nissan" : "370Z", "Chevy" : "Camaro", 
"Hyundai" : "Genesis Coupe" , "MINI Cooper" : "Roadster"}

ascars["MINI Cooper"]="Coupe"

#print(ascars)
#print(ascars["Nissan"])
#print(["Chevy"])

for value in ascars.values():
    print(value)
    

print("-------------------------")

for key in ascars.keys():
    print(key)
    
    
    
