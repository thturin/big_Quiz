import pgzrun
"""
Project No. Big Quiz

first question shows with four possible answers. The player has 10 secs to click on one of the answers. Game ends 
if player chosses a wrong answer or if the time runs out
"""
#Constants
WIDTH = 1280
HEIGHT = 720
#Global vars
score = 0
time_left = 10
questions = []
answers = []


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
    counter = 1
    with open('data.txt') as f:
        line = f.readlines()
        if (counter+1)%2 == 0: # if counter is an odd number
            print(counter)
            questions.append(line)
            #print(questions)
        counter+=1

read_data()

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box,"sky blue")
    screen.draw.filled_rect(timer_box,"green")

    for box in answer_boxes:
        screen.draw.filled_rect(box,"yellow")


def game_over():
    pass

def correct_answer():
    pass

def on_mouse_down(pos):
    pass

def update_time_left():
    pass




pgzrun.go()