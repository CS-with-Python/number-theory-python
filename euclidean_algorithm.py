"""
The Euclidean Algorithm using Python
Solution to ex.5.2 from "A Friendly Introduction to Number Theory" 
Author: Winterflower (2014)
contact: info[at]winterflower.net
"""

def gcd(a,b):
	"""
	Returns the greatest common divisor of two greatest
	integers.
	"""
	if a==0 or b==0:
		return 0
	else:
		#first calculation
		remainders=[]
		quotient=a/b
		remainder=a%b
		if remainder==0:
			return quotient
		else:
			remainders.append(remainder)		
			a=b
			b=remainder
			while remainders[len(remainders)-1]>0:
				quotient=a/b
				remainder=a%b
				remainders.append(remainder)
				a=b
				b=remainder
			return remainders[len(remainders)-2]

def main():
	"""
	Main for calculating the gcd of two user supplied numbers
	"""
	print "Please enter the first integer"
	a=raw_input()
	print "The integer you entered is "+ a
	
	print "Please enter the second integer"
	b=raw_input()
	print "The integer you entered is "+ b

	print "Now computing the greatest common divisor of "+ a + " and "+ b 
	
	divisor=gcd(int(a),int(b))
	print divisor
	
if __name__: main()





