import numpy as np
from scipy.optimize import minimize

def Loss(Location, Bases, Distances):

  Location = np.atleast_2d(Location)
  Bases = np.atleast_2d(Bases)
  Distances = np.atleast_2d(Distances)

  squared_distance_actual = np.sum((Bases - Location)**2, axis=1, keepdims=True)
  
  epsilon_squared = (squared_distance_actual - Distances**2)
  
  return np.sum(epsilon_squared**2)

def argmin_loss(Bases, Distances):
 
  initial_guess = np.mean(Bases, axis=0)

  loss_func = lambda loc: Loss(loc, Bases, Distances)

  result = minimize(loss_func, initial_guess, method='Powell')
  
  return result.x

if __name__ == '__main__':
  BRef = np.array([[100, 0], [100, 100], [0, 100],
                   [0, 0], [-20, 50]])

  gt = np.array((30, 70)).reshape((1, 2))
  D = np.sqrt(np.sum((BRef - gt)**2, axis=1)).reshape(-1, 1)
  P = np.array([30, 70])
  print(Loss(P, BRef, D))
  P = np.array([31, 71])
  print(Loss(P, BRef, D))
  P = np.array([29, 70])
  print(Loss(P, BRef, D))
  print(f"Location = {argmin_loss(BRef, D)}")
  
  gt = np.array((15, 40)).reshape((1, 2))
  D = np.sqrt(np.sum((BRef - gt)**2, axis=1)).reshape(-1, 1)
  print(f"Location = {argmin_loss(BRef, D)}")