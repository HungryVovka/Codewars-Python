# -----------------------------------------------------------
# Skip Situation and go straight to Task if you care not about the story (all you need to solve the kata will be contained under "Task").
# 
# The answers are hidden to prevent users from figuring out the solution from the results of the tests.
# 
# Situation
# Every year, in an ancient civilization, all the villagers would gather for the ritual that would ensure their survival.
# 
# All of the sheep in the village would be arranged in a square grid. Then, a sacrifice to the gods would be performed, granting the people food and 
# riches.
# 
# However, their rewards for the sacrifice weren't always the same, largely depending on the layout of the sheep.
# 
# Unbeknownst to the villagers, the gods had a very systematic method for rewarding them.
# 
# Our generosity towards you humans shall be proportional to the determinant of the matrix formed by the sheep you provide us.
# 
# One day, a new emperor, "Yushi.py the II", decides on a new formation for the sheep, believing it would bring great riches to his reign.
# 
# The sheep would be placed in the following manner:
# 
# Consider a matrix with rows and columns with indices beginning at 1 and the first square in the upper left corner.
# The number of sheep in a given square shall be the product of the indices of the rows and the columns.
# In more programmer friendly words: The elements of a matrix m are such that m[i][j] = (i + 1) * (j + 1).
# 
# Here are the formations used in the first three rituals:
# 
# [1]     [1, 2]      [1, 2, 3]
#         [2, 4]      [2, 4, 6]
#                     [3, 6, 9]
# 
# As a historian, you stumble across this civilization and wish to try to explain their sudden decay after the rule of their new emperor.
# 
# To do so, you decide to determine the riches received by the villagers, according to the new disposition of sheep decided by Yushi.py the II.
# 
# 
# Task
# Let's say a matrix m exists such that the value of each square is the product of the indices of the rows and columns, considering that the indices start 
# at 1 and the first square is in the upper left corner.
# 
# Examples of the matrix:
# 
# n = 1 -> [1] n = 2 -> [1, 2] n = 3 -> [1, 2, 3]
#                       [2, 4]          [2, 4, 6]
#                                       [3, 6, 9]
# 
# Given n, the size of the square matrix, your task is to create a function, ritual, that returns the determinant of the matrix.
# 
# Do not return the matrix; return its determinant
# 
# Input
# You will be given a positive integer n, meaning, don`t worry about input validation.
# 
# Maximum Length
# The length of your code must not exceed 19 characters.
# 
# Random Tests
# There will be a total of 100 random tests. They will be separated into 4 categories: small, medium, big, and huge tests, with 25 tests each; their range 
# is:
# 
# Small: 1 <= n <= 9
# Medium: 10 <= n <= 1_000
# Big: 100_000 <= n <= 1_000_000
# Huge: 2 ** 32 <= n <= 2 ** 64
# -----------------------------------------------------------

ritual=lambda m:m<2