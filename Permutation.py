def toString(List): 
	return ''.join(List) 


def permute(a, l, r): 
	if l == r: 
		print(toString(a)) 
	else: 
		for i in range(l, r): 
			a[l], a[i] = a[i], a[l]   #exchange
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l]
			
string =input("Enter the string:")
n = len(string) 
a = list(string) 
print(a)
permute(a, 0, n) 