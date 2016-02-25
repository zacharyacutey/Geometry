from math import pi,sin,cos,tan
def nas(n,a,s):
  return n*a*s/2
def pa(p,a):
  return p*a/2
#Little nicities that Harness failed to teach us
def na(n,a):
  return n*a**2*tan(pi/n)
def ns(n,s):
  return n*s**2/4/tan(pi/n)
def nr(n,r):
  return n*r**2/2*sin(2*pi/n)
