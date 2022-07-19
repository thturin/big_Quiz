import pgzrun, random
"""
Project No. Big Quiz

first question shows with four possible answers. The player has 10 secs to click on one of the answers. Game ends 
if player chosses a wrong answer or if the time runs out

HACKS AND TWEAKS
give a hint-> when the user hits the h key, they can see a hint in the python console or terminal OR two answers get 
blurred out on the screen 

add more questions to the text file 

make the colors look nicer!

"""
#Constants
WIDTH = 1280
HEIGHT = 720
#Global vars
score = 0
time_left = 10
questions = []
answers = []
hint = False

#create the box interface
main_box = Rect(0,0,820,240)
timer_box = Rect(0,0,240,240)
answer_box1 = Rect(0,0,495,165)
answer_box2 = Rect(0,0,495,165)
answer_box3 = Rect(0,0,495,165)
answer_box4 = Rect(0,0,495,165)
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

#move_ip moves the rectangular shape move_ip(x,y coords of top left corner)
main_box.move_ip(50,40)
timer_box.move_ip(990,40)
answer_box1.move_ip(50,358)
answer_box2.move_ip(735,358)
answer_box3.move_ip(50,538)
answer_box4.move_ip(735,538)


def read_data():
    global questions, answers
    data = []
    with open('data.txt') as f:
        data = f.readlines()
        #print(data)
    for i in range(0,len(data),2):
        temp = []
        temp = data[i+1].strip('\n').split(',')
        temp.insert(0,data[i].strip('\n'))
        questions.append(temp)

read_data()
question = questions.pop(0) #have to create variable here after questions list is populated in read_data() function

def draw():
    global hint
    screen.fill((6,12,233)) #JEOPARDY BLUE COLOR
    screen.draw.filled_rect(main_box,"Yellow")
    screen.draw.filled_rect(timer_box,(6,12,233))

    for box in answer_boxes:
        screen.draw.filled_rect(box,"yellow")

    screen.draw.textbox(str(time_left), timer_box, color=("yellow"))
    screen.draw.textbox(question[0],main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index],box, color=("black"))
        index+=1

#hack that blurs out two answers that are wrong
    if hint:
        #do not block out answer and one random non answer
        while True: #first find another index that will not be blurred out with the correct answer
            keep_index = random.randint(0,3)
            if keep_index != (int(question[5])-1): #you must subtract 1 because the answer assumes index 1-4
                break

        for index, box in enumerate(answer_boxes): #loop through answer boxes
            if index!=keep_index and (index+1)!=int(question[5]): #if the index is not the keep_index or the index that has the answer, temporarily make the box red
                screen.draw.filled_rect(answer_boxes[index], "red")
        hint = False

def game_over():
    global question, time_left
    message = "Game over, you got {} questions correct".format(score)
    question = [message,'x','x','x','x',5]
    time_left = 0

def correct_answer():
    global question, score, time_left
    score +=1
    if questions: #assuming the boolean is if questions is not empty then do this
        question = questions.pop(0)
        time_left = 10 #reset timer
    else: #questions list is empty, game is over
        print("End of Questions")
        game_over()

def on_key_up(key):
    global hint
    if key == keys.H:
        hint = True

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            #print("Clicked on answer " + str(index))
            #make sure you change the type of integer!!! can't compare 2 and '2'
            if index == int(question[5]): #the index value corresponds to answer box 1-4 in answer_boxes list
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index+=1

def update_time_left(): #for the countdown clock
    global time_left
    if time_left: #if time_left!=0
        time_left -= 1
    else:
        game_over()

clock.schedule_interval(update_time_left,1.0) #call this function every 1 second

pgzrun.go()