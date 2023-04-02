from pulp import *

import numpy as np, pandas as pd

import warnings

warnings.filterwarnings('always')

warnings.filterwarnings('ignore')
prob = LpProblem('Diet_Problem', LpMinimize)
df = pd.read_excel('diet.xls',nrows=17)
df.head() #Here we see the data
food = list(df.Foods)
#The list of items
count=pd.Series(range(1,len(food)+1))
print('List of different food items is here follows: -')
food_s = pd.Series(food)
#Convert to data frame
f_frame = pd.concat([count,food_s],axis=1,keys=['S.No','Food Items'])
f_frame
# Create a dictinary of costs for all food items
costs = dict(zip(food,df['Price/Serving']))
#Create a dictionary of calories for all items of food
calories = dict(zip(food,df['Calories']))
#Create a dictionary of cholesterol for all items of food
chol = dict(zip(food,df['Cholesterol (mg)']))
#Create a dictionary of total fat for all items of food
fat = dict(zip(food,df['Total_Fat (g)']))
#Create a dictionary of sodium for all items of food
sodium = dict(zip(food,df['Sodium (mg)']))
#Create a dictionary of carbohydrates for all items of food
carbs = dict(zip(food,df['Carbohydrates (g)']))
#Create a dictionary of dietary fiber for all items of food
fiber = dict(zip(food,df['Dietary_Fiber (g)']))
#Create a dictionary of protein for all food items
protein = dict(zip(food,df['Protein (g)']))
#Create a dictionary of vitamin A for all food items
vit_A = dict(zip(food,df['Vit_A (IU)']))
#Create a dictionary of vitamin C for all food items
vit_C = dict(zip(food,df['Vit_C (IU)']))
#Create a dictionary of calcium for all food items
calcium = dict(zip(food,df['Calcium (mg)']))
#Create a dictionary of iron for all food items
iron = dict(zip(food,df['Iron (mg)']))
# A dictionary called 'food_vars' is created to contain the referenced Variables
food_vars = LpVariable.dicts("Food",food,lowBound=0,cat='Continuous')
prob += lpSum([costs[i]*food_vars[i] for i in food])
prob
lpSum([food_vars[i]*calories[i] for i in food])
prob += lpSum([food_vars[x]*calories[x] for x in food]) >= 800, "CaloriesMinimum"
prob += lpSum([food_vars[x]*calories[x] for x in food]) <= 1300, "CaloriesMaximum"
prob
#Carbohydrates' constraint
prob += lpSum([food_vars[x]*carbs[x] for x in food]) >= 130, "CarbsMinimum"
prob += lpSum([food_vars[x]*carbs[x] for x in food]) <= 200, "CarbsMaximum"
#Fat's constraint
prob += lpSum([food_vars[x]*fat[x] for x in food]) >= 20, "FatsMinimum"
prob += lpSum([food_vars[x]*fat[x] for x in food]) <= 50, "FatsMaximum"
#Protein's constraint
prob += lpSum([food_vars[x]*protein[x] for x in food]) >= 100, "ProteinsMinimum"
prob += lpSum([food_vars[x]*protein[x] for x in food]) <= 150, "ProteinsMaximum"
#Vit_A constraint
prob += lpSum([food_vars[x]*vit_A[x] for x in food]) >= 1000, "Vit_A_Minimum"
prob += lpSum([food_vars[x]*vit_A[x] for x in food]) <= 10000, "Vit_A_Maximum"
prob.solve()
prob. solver
LpStatus[prob.status]
for var in prob.variables():
    print(f'Variable name: {var.name} , Variable value : {var.value()}n')
print('n')
print('*'*100)
print('n')
#We can also see the slack variables of the constraints
for name, con in prob.constraints.items():
    print(f'constraint name:{name}, constraint value:{con.value()}n')
print('*'*100)
print('n')
## OBJECTIVE VALUE
print(f'OBJECTIVE VALUE IS: {prob.objective.value()}')
