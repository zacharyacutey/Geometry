from sympy import *
from __future__ import division
from FileNineThree import 
#p1 in circles is the center, p2 is the point
def slope(p1,p2):
  return Number(p2[1]-p1[1])/Number(p2[0]-p1[0])
def distance(p1,p2):
  return sqrt((Number(p2[1]-p1[1]))**2+(Number(p2[0]-p2[0]))**2)
def circle_area(p1,p2):
  return r_a(distance(p1,p2))
def circle_circumfrence(p1,p2):
  return r_c(distance(p1,p2))
