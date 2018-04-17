import Dice as die


#general tests to check the 'Dice' library

sides = 4
rps = ('rps',['rock','paper','scissors'])

runCount = 2000000
a,b = [],[]

#fill list 'a' with 'runcount' of results from a 'sides' sided die
for x in range(runCount):
    a.append(die.die(sides))

#calculate and display varience from expected results.
#some variance is expected as this is experimental vs theoretical 
for x in range(1,sides+1):
    print(str(x) + ": " + str(a.count(x)*100/runCount - 100/sides))

#test that die starts at 1 and stops at 'sides'
print('max: ' + str(max(a)) + ' min: ' + str(min(a)))

#fill list 'b' with 'runcount' of results from playing rock paper scissors
for x in range(runCount):
    b.append(die.die(rps))

#calculate and display varience
for x in range(len(rps[1])):
    print(rps[1][x] + ': ' + str(b.count(rps[1][x])*100/runCount - 100/len(rps[1])))

#count results for rock paper scissors
j=[]
for x in range(len(rps[1])):
    j.append((rps[1][x],b.count(rps[1][x])))
print(j)

#dice name check
print('rps is ' + die.dieName(rps))

#isIntList behavior validation
tests = [[1],         #True
         [1,2],       #True
         ['a'],       #False
         ('a', [1,2]),#False
         1,           #False
         1.0]         #False

for example in tests:
    print(example, " | ", die.isIntList(example))


