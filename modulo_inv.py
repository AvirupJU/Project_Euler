def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)
  
def diophantine(a,b,c):
  q,r= divmod(a,b)
  if r==0:
    return([0,c/b])
  else:
    sol=diophantine(b,r,c)
    u=sol[0]
    v=sol[1]
    return([v,u-q*v])
  
def divide(a, b, n):
  assert n > 1 and a > 0 and gcd(a, n) == 1
  t,s= diophantine(n,a,1)
  if s<0:
    s=n+s
  # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
  return (s*b)%n