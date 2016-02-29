from sympy import *
#Circumference - c
#Radius - r
#Diameter - d
#Area - a
def r_c(r):
  return 2*r*pi
def r_a(r):
  return pi*r**2
def r_d(r):
  return 2*r
def d_r(d):
  return d/2
def d_c(d):
  return d*pi
def d_a(d):
  return r_a(d/2)
def c_a(c):
  return d_a(c/pi)
def c_d(c):
  return c/pi
def c_r(c):
  return c_d(c)/2
def a_c(a):
  return r_c(sqrt(a/pi))
def a_r(a):
  return sqrt(a/pi)
def a_d(a):
  return 2*a_r(a)
