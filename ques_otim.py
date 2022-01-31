import pulp as p
import pandas as pd
import numpy as np
from collections import OrderedDict

prob = p.LpProblem("Ques_Otim", p.LpMinimize)

Xa1 = p.LpVariable("Xa1", lowBound=0, cat="Integer")
Xb1 = p.LpVariable("Xb1", lowBound=0, cat="Integer")
Xc1 = p.LpVariable("Xc1", lowBound=0, cat="Integer")
Xd1 = p.LpVariable("Xd1", lowBound=0, cat="Integer")
Xa2 = p.LpVariable("Xa2", lowBound=0, cat="Integer")
Xb2 = p.LpVariable("Xb2", lowBound=0, cat="Integer")
Xc2 = p.LpVariable("Xc2", lowBound=0, cat="Integer")
Xd2 = p.LpVariable("Xd2", lowBound=0, cat="Integer")
Xa3 = p.LpVariable("Xa3", lowBound=0, cat="Integer")
Xb3 = p.LpVariable("Xb3", lowBound=0, cat="Integer")
Xc3 = p.LpVariable("Xc3", lowBound=0, cat="Integer")
Xd3 = p.LpVariable("Xd3", lowBound=0, cat="Integer")

prob += (Xa1*65) + (Xb1*60) + (Xc1*55) + (Xd1*65) + (Xa2*65) + (Xb2*70) + (Xc2*80) + (Xd2*60) + (Xa3*70) + (Xb3*75) + (Xc3*80) + (Xd3*85)

prob += Xa1 + Xb1 + Xc1 + Xd1 == 60
prob += Xa2 + Xb2 + Xc2 + Xd2 == 90
prob += Xa3 + Xb3 + Xc3 + Xd3 == 110
prob += Xa1 + Xa2 + Xa3 == 50
prob += Xb1 + Xb2 + Xb3 == 60
prob += Xc1 + Xc2 + Xc3 == 70
prob += Xd1 + Xd2 + Xd3 == 80

print(prob)

status = prob.solve()
print(p.LpStatus[status])
print(p.value(prob.objective))

data = OrderedDict({
	'Xa1' : [p.value(Xa1)],
	'Xb1' : [p.value(Xb1)],
	'Xc1' : [p.value(Xc1)],
	'Xd1' : [p.value(Xd1)],
	'Xa2' : [p.value(Xa2)],
	'Xb2' : [p.value(Xb2)],	
	'Xc2' : [p.value(Xc2)],	
	'Xd2' : [p.value(Xd2)],	
	'Xa3' : [p.value(Xa3)],
	'Xb3' : [p.value(Xb3)],	
	'Xc3' : [p.value(Xc3)],	
	'Xd3' : [p.value(Xd3)]
})
	
df = pd.DataFrame(data)
print(df)

