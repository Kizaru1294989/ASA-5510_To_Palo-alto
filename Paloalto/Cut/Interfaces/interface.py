from Read.read import read


def identify_interface(output_file):
    file = read(output_file)
    capturing = False
    captured_data = []
    for line in file:
        line = line.strip()
        if line.startswith('interface'):
            capturing = True
        if capturing:
            captured_data.append(line)

        if line.startswith('!'):
            
            capturing = False
            
            
    for line in captured_data:
        palo_interface(line)
        
        
        
        
def palo_interface(line):
        print(line)
           