"""


"""

logical_false = 0
logical_true = 1


delimiter  = "*"
space_symbol = " "
# ord() или chr()
header = "* A *" + "* B *" + "* "+" A and B "+ "*"

table_width = len(header)
# print (logical_A and logical_B)
print(delimiter * table_width)
print(header)
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_true) and bool(logical_true)))) + "   *"
print(inp_str+res1)
print(delimiter * table_width)

inp_str = "* A ** B *"

res1 = "*  "+str(logical_true and logical_false) + "   *"
print(inp_str+res1)