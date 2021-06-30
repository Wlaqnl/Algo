bts={}
bts['rm']=94
print(bts)
bts['rm']='leader'
print(bts)
bts['jimin']='긔요밍'
bts['jk']='근육돼지'
bts['jin']='요리사'
bts['j-hope']='희망'
bts['suga']='daegu'
bts['V']='cgv'
print(bts)
print(bts.keys())
print(bts.values())
print(bts.items())

for a, b in bts.items():
    print(a,b)

print(bts.get('jimin'))