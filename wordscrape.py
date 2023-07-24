letters=[['h','o','l','i','d','a','y'],
         ['p','r','o','g','r','a','m','m','i','n','g'],
         ['b','o','o','t','c','a','m','p'],
         ['f','l','o','w','e','c','h','a','r','t'],
         ['w','o','r','d','s','c','r','a','p','e','s']]

words=[{'hi','hay','day','had','lay','dal','lad','lid','hold','lady','hail','load','holy','oil'},
       {'go','an','in','no','on','map','mom','gap','gag','pig','man','ping','pong','pram','pram','prom','ramp'},
       {'am','at','to','cab','cop','map','map','mop','act','bat','camp','comb','boom','pact','atom','boot','tap'},
       {'of','at','or','to','caw','cow','how','who','calf','claw','flaw','flow','fowl','wolf','crow','half'},
       {'we','do','as','cap','caw','cop','cow','paw','cod','dew','pad','cape','cope','crap','crew','crop','pace'}]

lives=5
level=0
score=0

print('***** WELCOME TO WORDSCAPE *****')
name= input("What's your good Name : ")
print('Game begins....\nBest of Luck', name, '!')
print()
while True:
    print('Level :', level+1)
    print('Create 3 words using given letters: ' )
    print(letters[level])
    print()
    word=''
    oldword=''
    wordcount=0
    match=False
    while wordcount == 0 or wordcount < 3:
        match = False
        word= input('Word:')
        word.lower()
        if  word != oldword:
            for w in words[level]:
                if word == w :
                    wordcount += 1
                    score += 1
                    oldword = word
                    match = True
                    #ptint (wordcount, score ,  oldword )
                    break
        elif word == '':
            continue

        if not match:
            print('Oops !! Take another guess...')
            lives -= 1
            print('lives:',lives)

        if (lives <= 0):
            print('Game over!! Better Luck Next Time !!!')
            print('Your score is ', score)
            break

    wordcount = 0
    match = False
    word = ''

    if lives == 0:
        break

    if level == 4:
        print('Thanks for playing the game!!')
        print('Your score is :' , score)
        break


    else:
        choice = input('Do you want to continue to next level? (y/n)' )
        if choice in 'y,Y':
            level+=1
        else:
            print('Thanks for playing the game!!')
            print('Your score is : ', score)
            break
        

            
