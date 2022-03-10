import random
#pwd = input("what is your password")
break1 = ["!","@","#","$","%","^","&","*"]
break2 = ["1","2","3","4","5","6","7","8","9","0"]
for i in range(65,91):
	break2.append(chr(i))
for i in range(97,123):
	break2.append(chr(i))




def encrypt(s):
	shift = random.randint(1,9)
	output = ""
	for i in range(len(s)):
		temp = 0
		temp += (len(s)-i) * shift * ord(s[i]) + shift
		output += str(temp) + random.choice(break1) + random.choice(break2)
	output += str(shift) + "\n"
	with open("passwords.txt", "a") as file_object:
		file_object.write(output)





def decrypt(h):
	shift = int(h[-1])
	output = ""
	length = 0
	temp = ""
	chars = []
	for i in h:
		if i in break1:
			length += 1
	pointer = 0
	while pointer < len(h):
		if h[pointer] in break1:
			chars.append(int(temp))
			pointer += 2
			temp = ""
		else:
			temp += h[pointer]
			pointer += 1
	
	for i,num in enumerate(chars):
		char = chr(int((num-shift) / shift / (length-i))) 
		output += char
	return output


def reveal():
	with open("passwords.txt") as file:
		lines = file.readlines()
		for line in lines:
			print(decrypt(line.rstrip()))










