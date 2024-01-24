#version = open('version/version-label.txt', 'r')
#print(version.read())

#create funtion
def print_version(pathtoversion):
    version = open(pathtoversion, 'r')
    return(version.read())

#print(print_version('src/version/version-label.txt'))