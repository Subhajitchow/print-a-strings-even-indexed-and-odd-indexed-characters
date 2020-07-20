# Given a string, , of length  that is indexed from  to ,
# print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
#
# Note:  is considered to be an even index.
# Given i/p:
# 2
# Hacker
# Rank

#Expected o/p:
# Hce akr
# Rn ak
n = int(input("how many time you want to do it?\n"))
for i in range(n):
    ls = str(input())
    print((ls[0:len(ls):2]),(ls[1:len(ls):2]))
# End
