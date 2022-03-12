import random

break1 = ["!","@","#","$","%","^","&","*"]
break2 = ["1","2","3","4","5","6","7","8","9","0"]
for i in range(65,91):
	break2.append(chr(i))
for i in range(97,123):
	break2.append(chr(i))




def encrypt(s):
	pre = random.randint(3,9)
	shift = random.randint(1,pre-1)
	output = ""
	for i in range(pre):
		output += random.choice(break2)
	shift2 = output[shift]
	for i in range(len(s)):
		temp = 0
		temp += (len(s)-i) * shift * ord(s[i]) + shift * ord(shift2)
		output += str(temp) + random.choice(break1) + random.choice(break2)
	if shift < 4:
		output += "0"
	output += str(shift**2) + random.choice(break2) + random.choice(break2) + str(pre) + "\n"
	with open("passwords.txt", "a") as file_object:
		file_object.write(output)





def decrypt(h):
	if not h:
		return
	pre = int(h[-1])
	shift = int(int(h[-5]+h[-4])**0.5)
	shift2 = h[shift]
	output = ""
	length = 0
	temp = ""
	chars = []
	for i in h:
		if i in break1:
			length += 1
	pointer = pre
	while pointer < len(h):
		if h[pointer] in break1:
			chars.append(int(temp))
			pointer += 2
			temp = ""
		else:
			temp += h[pointer]
			pointer += 1
	
	for i,num in enumerate(chars):
		char = chr(int((num-shift*ord(shift2)) / shift / (length-i))) 
		output += char
	return output


def reveal():
	with open("passwords.txt") as file:
		lines = file.readlines()
		for line in lines:
			print(decrypt(line.rstrip()))








