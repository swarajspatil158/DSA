n = 5
print("1")
for i in range(n):
	for j in range(n):
		print("*", end = " ")
	print("")

# Output:
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *
print("\n")

print("2")
for i in range(n):
	for j in range(i+1):
		print("*", end = " ")
	print("")

# Output:
#  * 
#  * * 
#  * * * 
#  * * * * 
#  * * * * *
print("\n")


print("3")
for i in range(n,0,-1):
	for j in range(i):
		print("*",end = " ")
	print("")

# Output: method1 = i:n to 0 and j: start to i
#  * * * * * 
#  * * * * 
#  * * * 
#  * * 
#  * 
print("\n")

print("4")
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


print("5")
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

print("6")
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

print("7")
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

print("8")
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

print("9")
for i in range(n-1):
	for j in range(i,n):
		print(" ", end = " ")
	for j in range(i+1):
		print("*",end = " ")
	for j in range(i):
		print("*",end = " ")
	print("")
for i in range(n):
	for j in range(i+1):
		print(" ",end = " ")
	for j in range(i,n):
		print("*", end = " ")
	for j in range(i,n-1):
		print("*", end = " ")
	print("")
# Output:
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 