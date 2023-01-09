# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from math import *
from matrix import *
angle = 0
points =[]

def setup():
  size(600, 400)

  points.append(Vector(-0.5, -0.5, -0.5))
  points.append(Vector(0.5, -0.5, -0.5))
  points.append(Vector(0.5, 0.5, -0.5))
  points.append(Vector(-0.5, 0.5, -0.5))
  points.append(Vector(-0.5, -0.5, 0.5))
  points.append(Vector(0.5, -0.5, 0.5))
  points.append(Vector(0.5, 0.5, 0.5))
  points.append(Vector(-0.5, 0.5, 0.5))

def draw():
  background(0)
  translate(width/2, height/2)


  rotationZ = [
    [ cos(angle), -sin(angle), 0],
    [ sin(angle), cos(angle), 0],
    [ 0, 0, 1]
  ]

  rotationX = [
    [ 1, 0, 0],
    [ 0, cos(angle), -sin(angle)],
    [ 0, sin(angle), cos(angle)]
  ]

  rotationY = [
    [ cos(angle), 0, sin(angle)],
    [ 0, 1, 0],
    [ -sin(angle), 0, cos(angle)]
  ]

  projected = []

  index = 0
  for v in points:
      rotated = matmul(rotationY, v)
      rotated = matmul(rotationX, rotated)
      rotated = matmul(rotationZ, rotated)

      distance = 2
      z = 1 / (distance - rotated.z)
      projection = [[z, 0, 0], [0, z, 0]]

      projected2d = matmul(projection, rotated)
      projected2d.mult(200)
      projected[index] = projected2d
      index += 1

  for v in projected:
      stroke(255)
      strokeWeight(16)
      noFill()
      point(v.x, v.y)

  for i in range(4):
      connect(i, (i + 1) % 4, projected)
      connect(i + 4, ((i + 1) % 4) + 4, projected)
      connect(i, i + 4, projected)

  angle += 0.03

  def connect(i, j, points):
      a = points[i]
      b = points[j]
      strokeWeight(1)
      stroke(255)
      line(a.x, a.y, b.x, b.y)