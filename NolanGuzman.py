import pygame

"""
pygame.init()

screenName=pygame.display.set_mode((800,800))
"""

NolanQs={
1: {
"problem":["apples=3",
           "oranges=4",
           "apples=oranges+2",
           "for x in range(0,9):",
           "    if(apples<10):",
           "        apples=apples+x",
           "print apples"],
"answer":"12"
},
2:{
"problem":["word1='hello'",
           "word2='goodbye'",
           "word1=word1+' '+word2",
           "word1.replace('hello', 'hi')",
           "word1=word1+''+'end'",
           "print word1"],
"answer":"hi goodbye end"
},
3:{
"problem":["nums=set([1,1,2,3,3,3,4])",
           "print len(nums)"],
"answer": "7"
},
4:{
"problem":["x=True",
           "y=False",
           "z=False",
           "if x or y and z:",
           "    print 'yes'",
           "else:",
           "    print 'no'"],
"answer":"yes"
},
5:{
"problem":["x=True",
           "y=False",
           "z=False",
           "if not x or y:",
           "    print 1",
           "elif not x or not y and z:",
           "    print 2",
           "elif not x or y or not y and x:",
           "    print 3",
           "else:",
           "    print 4"]
,"answer": "3"
},
6:{
"problem":["counter=1",
           "def doLotsofStuff():",
           "    global counter",
           "    for i in (1,2,3):",
           "        counter+=1",
           "        counter+=1",
           "doLotsOfStuff()",
           "print counter"]
,"answer":"4"
},
7:{
"problem":["print r'#woow'"]
,"answer":"#woow"
},
8:{
"problem":["x=sum(range(5))",
           "print x"]
,"answer":"10"
},
9:{
"problem":["kvps={'1':1,'2':2}",
           "theCopy = kvps",
           "kvps['1']=5",
           "sum = kvps['1']+theCopy['1']",
           "print sum"]
,"answer":"10"
},
10:{
"problem":["name='snow storm'",
           "print '%s' % name[6:8]"]
,"answer":"to"
},
}

'''
randomlist=random.sample(range(1,10),9)
for x in randomlist:
    comeon=NolanQs.get(x)
    newthingy=comeon.get('problem')
    for y in newthingy:
        print y
        
name = pygame.font.SysFont("Monospace",36)
screenName.blit(name.render("test",1,(0,128,128)),(400,400))

while True:
    pygame.display.update()
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

            '''
