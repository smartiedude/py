import re
with open("show_int_output.txt") as f:
    output = f.read()

print(type(output))

def Interface_Desc_Getter(ooga):    
   printa = re.search(r"  Description: (\S.+)", ooga).group(1)
   print(printa)
   return

def Interface_ID_Getter(booga):    
   mach = re.search(r"^(\S+/\d+) ", booga).group(1)
   print(mach)
   return

for i,line in enumerate(output.splitlines()):
    try:
        Interface_Desc_Getter(line)  
    except:
        continue
    
    try:
        Interface_ID_Getter(line)
    except:
        continue
    
# why will this not work with calling both functions?
# it only outputs from the one, never both. 
