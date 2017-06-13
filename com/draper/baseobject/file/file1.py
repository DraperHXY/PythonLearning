input = open(r"test.txt","w")
input.write("Hello Py")
input.close()

output = open(r"test.txt")
str = output.readline()
print(str)

input= open("/test.txt","w")
input.write("Haha I'm herere")
input.close()

output = open("/test.txt","rb")
print(output.read())

input = open("/bin.bin","w")
input.write("打发士大夫AHHAHadfsA")
input.close()

output = open('/bin.bin','w+')
str = output.readline()
print(str)