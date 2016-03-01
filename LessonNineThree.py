from sympy import *
#Circumference - c
#Radius - r
#Diameter - d
#Area - a
def r_c(r):
  return r_d(r)*pi
def r_a(r):
  return pi*r**2
def r_d(r):
  return 2*r
def d_r(d):
  return d/2
def d_c(d):
  return d*pi
def d_a(d):
  return r_a(r_d(r))
def c_a(c):
  return d_a(c_d(c))
def c_d(c):
  return c/pi
def c_r(c):
  return d_r(c_d(c))
def a_c(a):
  return r_c(a_r(a))
def a_r(a):
  return sqrt(a/pi)
def a_d(a):
  return r_d(a_r(a))
