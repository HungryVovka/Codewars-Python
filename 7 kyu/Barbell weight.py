# -----------------------------------------------------------
# Barbell weight
# 
# Kata overview
# Olympic weightlifting is a sport in which athletes compete in lifting a barbell from the ground to overhead, with the aim of successfully lifting the 
# heaviest weights.
# 
# The purpose of this kata is to compute the weight of an Olympic barbell.
# 
# Task
# Write a function that computes the barbell weight.
# 
# Input
# A string representation of a barbell, in the form ---gcBRRRR--------------------RRRRBcg---.
# 
# Weights are always between 25 - 274 kg (both included).
# 
# Output
# The weight of the barbell in kg (integer).
# 
# Barbell details
# A barbell consists of three parts:
# 
# Bar
# Discs
# Collars
# 
# The bar weighs 20 kg and uses character -. The bar is 40 characters long.
# 
# Discs are loaded and secured by collars on the sleeve of the bar. The bar is loaded with the heaviest discs first and then the lighter discs loaded in 
# descending order of weight toward the outer edge of the bar. The following discs are used. Discs are loaded from the 10th character from the outer 
# edge of the bar.
# 
# WEIGHT  COLOR   CHAR
# 25 kg   red     R
# 20 kg   blue    B
# 15 kg   yellow  Y
# 10 kg   green   G
# 5 kg    white   W
# 2.5 kg  red     r
# 2 kg    blue    b
# 1.5 kg  yellow  y
# 1 kg    green   g
# 0.5 kg  white   w
# 
# In order to secure the discs to the bar, each bar must be equipped with two (2) collars. Collars weigh 2.5 kg each. Collars use character c, and are 
# positioned outward of discs of 2.5 kg or more, and inward of discs of 2 kg or less.
# 
# Some examples of loaded barbells and their total weight.
# 
# WEIGHT  BARBELL
# 25 kg   ---------c--------------------c---------
# 26 kg   --------wc--------------------cw--------
# 34 kg   -------bcr--------------------rcb-------
# 35 kg   --------cW--------------------Wc--------
# 47 kg   -------gcG--------------------Gcg-------
# 58 kg   -------ycY--------------------Ycy-------
# 124 kg  -----bcrBR--------------------RBrcb-----
# 225 kg  -----cRRRR--------------------RRRRc-----
# 267 kg  ---gcBRRRR--------------------RRRRBcg---
# -----------------------------------------------------------

discs_and_collar = {
    "b" : 2.0,
    "c" : 2.5,
    "g" : 1.0,
    "r" : 2.5,
    "w" : 0.5,
    "y" : 1.5,
    "B" : 20.0,
    "G" : 10.0,
    "R" : 25.0,
    "W" : 5.0,
    "Y" : 15.0,
    "-" : 0.0,
}

def barbell_weight(barbell):
    return sum(discs_and_collar[i] for i in barbell) + 20.0
