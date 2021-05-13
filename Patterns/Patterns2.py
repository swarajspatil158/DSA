n = 5
print("First Pattern")
for i in range(n):
	for j in range(n):
		print("1", end = " ")
	print("")

# Output:First Pattern
# 1 1 1 1 1 
# 1 1 1 1 1 
# 1 1 1 1 1 
# 1 1 1 1 1 
# 1 1 1 1 1
print("\n")

print("Second Pattern")
for i in range(1,n+1):
	for j in range(1,i+1):
		print(i, end = " ")
	print("")
print("\n")

p=5
for i in range(1,n+1):
	for j in range(1,i+1):
		print(p, end = " ")
	p-=1
	print("")

print("\n")
for i in range(1,n+1):
	for j in range(1,i+1):
		if i%2 ==0:
			print("2",end = " ")
		else:
			print("1", end = " ")
	print("")

# Output: Second Pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 


# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1
print("\n")

p=1
print("3rd Pattern")
for i in range(n,0,-1):
	for j in range(i):
		print(p,end = " ")
	p+=1
	print("")
print("\n")

# Output: method1 = i:n to 0 and j: start to i
# 3rd Pattern
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1  
print("\n")

print("4th Pattern")
for i in range(n):
	for j in range(i,n):
		print("*",end = " ")
	print("")

# Output: method2 = i:start to n and j:i to n
#  * * * * * 
#  * * * * 
#  * * * 
#  * * 
#  * 
print("\n")


print("5th Pattern")
for i in range(n):
	for j in range(i,n):
		print(" ",end = " ")
	for j in range(i+1):
		print("*",end = " ")
	print("")

# Output:
#           * 
#         * * 
#       * * * 
#     * * * * 
#   * * * * *
print("\n")

print("6th Pattern")
for i in range(n):
	for j in range(i+1):
		print(" ", end = " ")
	for j in range(i,n):
		print("*",end = " ")
	print("")
# output:
#   * * * * * 
#     * * * * 
#       * * * 
#         * * 
#           *

print("7th Pattern")
for i in range(n):
	for j in range(i+1):
		print(" ",end = " ")
	for j in range(i,n):
		print("*", end = " ")
	for j in range(i,n-1):
		print("*", end = " ")
	print("")
# Output:
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 

print("8th Pattern")
for i in range(n):
	for j in range(i,n):
		print(" ", end = " ")
	for j in range(i+1):
		print("*",end = " ")
	for j in range(i):
		print("*",end = " ")
	print("")

# Output:
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * *
p =1
print("9th Pattern")
for i in range(n-1):
	for j in range(i,n):
		print(" ", end = " ")
	for j in range(i+1):
		print(p,end = " ")
	for j in range(i):
		print(p,end = " ")
	p+=1
	print("")
for i in range(n):
	for j in range(i+1):
		print(" ",end = " ")
	for j in range(i,n):
		print(p, end = " ")
	for j in range(i,n-1):
		print(p, end = " ")
	p+=1
	print("")

print("\n")
p =1
for i in range(n-1):
	for j in range(i,n):
		print(" ", end = " ")
	for j in range(i+1):
		print(p,end = " ")
	for j in range(i):
		print(p,end = " ")
	p+=1
	print("")
for i in range(n):
	for j in range(i+1):
		print(" ",end = " ")
	for j in range(i,n):
		print(p, end = " ")
	for j in range(i,n-1):
		print(p, end = " ")
	p-=1
	print("")
# Output:
  #         1 
  #       2 2 2 
  #     3 3 3 3 3 
  #   4 4 4 4 4 4 4 
  # 5 5 5 5 5 5 5 5 5 
  #   6 6 6 6 6 6 6 
  #     7 7 7 7 7 
  #       8 8 8 
  #         9 


  #         1 
  #       2 2 2 
  #     3 3 3 3 3 
  #   4 4 4 4 4 4 4 
  # 5 5 5 5 5 5 5 5 5 
  #   4 4 4 4 4 4 4 
  #     3 3 3 3 3 
  #       2 2 2 
  #         1   