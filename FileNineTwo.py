#Do we have sympy?
try:
  from sympy import *
except ImportError:
  from math import pi,sin,cos,tan
#Some py scripts I used for 9-2, area and perimeter of regular polygons
#a - Apothem
#p - perimeter
#n - number of sides
#r - polygonal radius
#s - side length
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
