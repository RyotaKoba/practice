planetList = [{"name":"Mercury","radius":2439.64,"au":0.3871,"period":88.0},
              {"name":"Venus","radius":6051.59,"au":0.7233,"period":224.7},
              {"name":"Earth","radius":6387.1,"au":1.0000,"period":365.25},
              {"name":"Mars","radius":3397.0,"au":1.5237,"period":687.0},
              {"name":"jupiter","radius":69911.0,"au":5.2026,"period":4328.9}
              ]
print len(planetList)
print planeList[2]
print planetList[2]['radius']
radiusSum=0
for i in range(len(planetList)):
    radiusSum += planetList[i]['radius']
    
print "ave:",radiusSum 
    
radiusSum=0

for p in range planetList:
    radiusSum += p['radius']
print "ave:",radiusSum
