S="MADAM"
R=""
for i in S:
    R = i+R
l=len(S)
for i in range(0,l):
    if(S[i] !=R[i]):
       break
if (i==l-1):
      print("PALINDROME")
else:
      print("NOT PALINDROME")
