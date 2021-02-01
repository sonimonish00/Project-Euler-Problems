# ============================================================
# Sieve of Erastothenes (Prime Numbers Ultimate Program) - by monish
# Will do Primality test,prime factors,generating primes upto root n etc. etc. all in one program 
# ============================================================
#1. Multiples of 3 and 5
counter = 0
for i in range (1000):
    if (i%3 == 0) | (i%5 == 0):
        counter = counter + i
print(counter)
# ============================================================
#2. Even Fibonacci numbers
fiblis = [1,2]
counter = 0
while(fiblis[-1]<4000000):
    fiblis.append(fiblis[-1]+fiblis[-2])
for i in range(len(fiblis)):
    if fiblis[i] % 2 == 0:
        counter = counter + fiblis[i]
print(counter)
# ============================================================
#3. Largest prime factor - using Trial Division Method [2 to root(n)]
n = 17
prime_list = []
first = 2
while n>1:
    if n% first == 0:
        prime_list.append(first)
        n/= first
    else:
        first+=1
if not prime_list:
	prime_list.append(n)
	print(prime_list)
else:
	print(prime_list)

# More Efficient Code
prime_list = []
while n % 2 == 0:
    prime_list.append(2)
    n /= 2
first = 3
# 3 to root(n) can be written as 3*3 <=n
while first * first <= n:
    if n % first == 0:
        prime_list.append(first)
        n /= first
    else:
        first += 2
# Only odd number is possible - the number which comes here will surely be a odd & not prime (dont get confused with the name prime_list its just name)
if n != 1: a.append(n)
print(prime_list)
# ============================================================
#4. Largest Palindrom Product (Unoptimized Solution)
def check_palindrome (num):
    num_rev = int(str(num)[::-1])
    if (num == num_rev):
        return True
    else:
        return False

f = 0
s = 0
temp = 0
for i in range(100,1000):
    if (check_palindrome(i*i) == True) & ((i*i) >temp):
        temp = i*i
        f = i
        s = i
    else:
        j = i+1
        while (j<=999):
            if (check_palindrome(i*j) == True) & ((i*j) > temp) :
                temp = i*j
                f = i
                s = j
            j+=1

print(f)
print(s)
print(temp)
# ============================================================
#5. Smallest Multiple (LCM)
from math import gcd
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lcm = 1
for i in num_list[1:]:
  lcm = lcm*i//gcd(lcm, i)
print(lcm)
# ============================================================
#6. Sum of Squares - Square of sum 
sum_of_square = 0
square_of_sum = 0

for i in range(1,101):
    sum_of_square += i*i
    square_of_sum+=i

print((square_of_sum*square_of_sum)-sum_of_square)
# ============================================================
#7. 10001st prime
prime_counter = 1
primes = 2

prime_list = []
while(prime_counter<=10001):
    for i in range(2,primes):
        if(primes%i) == 0:
            break
    else:
        prime_counter +=1
        prime_list.append(primes)
    primes+=1
print("The 10001th prime Number is : "+str(prime_list[-1]))    
# ============================================================
#8. Largest Product in a series - 13 digit
t = [int(x) for x in str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)]

greatest_product = 0
new_str = ""
adj_elem = 0

for i,c in enumerate(t):
    while(i<=len(t)-13):
        adj_elem = t[i]*t[i+1]*t[i+2]*t[i+3]*t[i+4]*t[i+5]*t[i+6]*t[i+7]*t[i+8]*t[i+9]*t[i+10]*t[i+11]*t[i+12]
        if (adj_elem)>greatest_product:
            greatest_product = adj_elem
            new_str = str(t[i])+str(t[i+1])+str(t[i+2])+str(t[i+3])+str(t[i+4])+str(t[i+5])+str(t[i+6])+str(t[i+7])+str(t[i+8])+str(t[i+9])+str(t[i+10])+str(t[i+11])+str(t[i+12])
        i+=1
print("The 13 Adjacent No. is :"+new_str)
print("And their Product is (Answer) : "+str(greatest_product))
# ============================================================
#9. Special Pythagorean triplet
# Unoptimized and Very Heavy computing Solution
m,n = 2,1
a,b,c = 0,0,0
while((a+b+c)!=56):
    a = (m*m) - (n*n)
    b = 2*m*n
    c = (m*m) + (n*n)
    if (a+b+c) == 56:
        print(a,b,c)
        print("The Product is")
        print(a*b*c)
    m+=1
    n+=1
# Optimized and Quick Solution (Copy-paste)
for a in range(1, 1000):
     for b in range(a, 1000):
         c = 1000 - a - b
         if c > 0:
             if c*c == a*a + b*b:
                 print (a*b*c)
                 break
# ============================================================
#10. Summation of primes

