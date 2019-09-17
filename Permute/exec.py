n=int(input())
k=1
while(int(bin(k)[2:])*9%n!=0):
  k+=1
printf(int(bin(k)[2:])*9)
