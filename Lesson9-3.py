from sympy import *
#Circumference - c
#Radius - r
#Diameter - d
#Area - a
def r_c(r):
  return 2*r*pi
def d_c(d):
  return d*pi
def r_a(r):
  return pi*r**2
def d_a(d):
  return r_a(d/2)
def c_a(c):
  return d_a(c/pi)
def a_c(a):
  return r_c(sqrt(a/pi))
