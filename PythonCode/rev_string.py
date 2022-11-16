def reverse_string(s):
	s1 = ""
	length = len(s)-1
	while length >= 0:
		s1 = s1+s[length]
		length = length - 1
	return s1
	
str = "sainath"

print("Reverse of a string using while = " ,reverse_string(str))