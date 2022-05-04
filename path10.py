import pygame
import csv
import wpilib
import wpilib.drive

# start pygame
pygame.init()
running = True

right_motor = wpilib.WPI_TalonFX(1) #right motor
left_motor = wpilib.WPI_TalonFX(2) #left motor

joysticks = []
encoder1 = wpilib.Encoder(0, 1, False)
count = 0
save = 0
area = None
area2 = None
pos_1 = 0
pos_2 = 0
pos_3 = 0
pos_4 = 0
pos_5 = 0
turnDirect = ""
turn = ""
turn1 = ""
turn2 = ""
turn3 = ""
turn4 = ""


def setup():
    count = 0
    encoder1.reset()
    turnDirect = ""

    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 4:
            # left bumper
            # turn 90° to the left
            turnDirect = "L"
            turn90()
            turn = ""
        if event.button == 5:
            # right bumper
            print('RB')
            turnDirect = "R"
            turn90()
            turn = ""


        if event.button == 0 and count == 0:
            # a button
            encoder1 = 0
            pos_1 = 0
            count = count + 1
        if event.button == 0 and count == 1:
            # a button
            pos_2 = encoder1
            count = count + 1
        if event.button == 0 and count == 2:
            # a button
            pos_3 = encoder1
            count = count + 1

        if event.type == pygame.JOYAXISMOTION:
            if (event.button == 3) and (count == 3):
                # y button
                return_home()

        if event.type == pygame.JOYAXISMOTION:
            #movement
            if event.axis == 4:
                # left trigger
                #have both motors go forward
                print('Lt')


            if event.axis == 5:
                # right trigger
                #have both motors go backward
                print('RT')
                right_motor.set(.01)
                left_motor.set(.01)

        pos_4 = (pos_3 + '''90°''') + side1
        pos_5 = (pos_4 + '''90°''') + side2

        side1 = pos_2 - pos_1
        side2 = pos_3 - (pos_2 + '''90°''')

    area = side1 * side2


def turn90():
    if turnDirect == "R":
        '''
        if encoder1 < (encoder1 + amount to turn):
            right_motor.set(.01) #turn right motor forewards
            left_motor.set(-.01) #turn left motor backwards
        elif encoder1 == (encoder1 + amount to turn):
            #turns motors off when complete turn
            right_motor.set(0)
            left_motor.set(0)
            turn = complete
        '''
    if turnDirect == "L":
        '''
        if encoder1 > (encoder1 - amount to turn):
            right_motor.set(-.01) #turn right motor backwards
            left_motor.set(.01) #turn left motor forewards
        elif encoder1 == (encoder1 - amount to turn):
            #turns motors off when complete turn
            right_motor.set(0) 
            left_motor.set(0)
            turn = "complete"
        '''


def return_home():
    r_turn1 = ""
    r_turn2 = ""
    turn = ""
    turn90()
    if turn == "complete":
        r_turn1 = "complete"
        turn = "reset"
    if r_turn1 == "complete":
        if (encoder1) < pos_4:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_4:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
            if turn == "complete":
                r_turn2 = "complete"
                turn = "reset"
    if r_turn2 == "complete":
        if (encoder1) < pos_5:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_5:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
            turn = "reset"

def outline():
    encoder1.reset()
    turn1 = ""
    turn2 = ""
    turn3 = ""
    turn4 = ""

    if (encoder1) == 0:
        if (encoder1) < pos_2:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_2:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
        if turn == "complete":
            turn1 = "complete"
            turn = "reset"

    if turn1 == "complete":
        if (encoder1) < pos_3:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_3:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
        if turn == "complete":
            turn2 = "complete"
            turn = "reset"

    if turn2 == "complete":
        if (encoder1) < pos_4:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_4:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
        if turn == "complete":
            turn3 = "complete"
            turn = "reset"

    if turn3 == "complete":
        if (encoder1) < pos_5:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_5:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
        if turn == "complete":
            turn4 = "complete"
            turn = "reset"
            area = (pos_2 - pos_1) * (pos_3 - (pos_2 +''''90°'''))



def fill():
    encoder1.reset()
    encoder1 = 0
    turn1 = ""
    turn2 = ""
    turn3 = ""
    turn4 = ""
    turn1_2 = 0

    t = 1
    if (encoder1) == 0:
        if (encoder1) < pos_2:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_2:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
            if turn == "complete":
                turn1 = "complete"
                turn = ""

    if turn1 == "complete":
        if (encoder1) < pos_3:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_3:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
            if turn == "complete":
                turn2 = "complete"
                turn = ""


    if turn2 == "complete":
        if (encoder1) < pos_4:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_4:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
            if turn == "complete":
                turn3 = "complete"
                turn = ""

    if turn3 == "complete":
        if (encoder1) < pos_5:
            right_motor.set(.01)
            left_motor.set(.01)
        elif (encoder1) == pos_5:
            right_motor.set(0)
            left_motor.set(0)
            turn90()
            if turn == "complete":
                turn4 = "complete"
                turn = "reset"
                area = (pos_2 - pos_1) * (pos_3 - (pos_2 + '''90°'''))


    while (area2 > 0) and (turn4 == complete):
        turn1_2 = 0
        turn2_2 = 0
        turn3_2 = 0
        turn4_2 = 0
        
        if encoder1 < (pos_2 - (x*t)):
            right_motor.set(.01)
            left_motor.set(.01)

        elif encoder1 == (pos_2 - (x*t)):
            right_motor.set(0)
            left_motor.set(0)
            turn90()

            if turn == "complete":
                turn = "reset"
                turn1_2 = 1
                
        if turn1_2 == 1:
            if encoder1 < (pos_3 - (x*t)):
                right_motor.set(.01)
                left_motor.set(.01)

            elif encoder1 == (pos_3 - (x*t)):
                right_motor.set(0)
                left_motor.set(0)
                turn90()

                if turn == "complete":
                    turn = "reset"
                    turn2_2 = 1
                    
        if turn3_2 == 1:
            if encoder1 < (pos_4 - (x*t)):
                right_motor.set(.01)
                left_motor.set(.01)
    
            elif encoder1 == (pos_4 - (x*t)):
                right_motor.set(0)
                left_motor.set(0)
                turn90()
    
                if turn == "complete":
                    turn = "reset"
                    turn3_2 = 1
        
        if turn4_2 == 1:
            if encoder1 < (pos_5 - (x*t)):
                right_motor.set(.01)
                left_motor.set(.01)
            elif encoder1 == (pos_5 - (x*t)):
                area2 = (pos2 - (x*t)) * (pos3 - (x*t))
                right_motor.set(0)
                left_motor.set(0)
                turn90()
                turn += 1
                collection.setIntegratedSensorPosition(0)
    
    else:
        right_motor.set(0)
        left_motor.set(0)


# find and connect the xbox controller
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Detected joystick '" + joysticks[-1].get_name() + "'")

while True:
    for event in pygame.event.get():
        # buttons, bumpers, and menu/view buttons
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:
                # b button
                # zero/reset
                print('b')
                encoder1.reset()
                count = 0
                pos_1 = 0
                pos_2 = 0
                pos_3 = 0
                pos_4 = 0


            if event.button == 2:
                # x button
                # load
                print('x')
                with open('positions.csv') as file:  # opens and reads file
                    reader = csv.reader(file)
                    list = next(reader)

                    # sets pos values to pos values in the csv file
                    pos_1 = list[0]
                    pos_2 = list[1]
                    pos_3 = list[2]
                    pos_4 = list[3]
                    pos_5 = list[4]

            if event.button == 3:
                # y button
                print('y')

            if event.button == 4:
                # left bumper
                #turn 90° to the left
                print('LB')
                turn = "L"
                turn90()

            if event.button == 5:
                # right bumper
                #turn 90° the the right
                print('RB')
                turn = "R"
                turn90()

            if event.button == 6:
                # view button
                #save
                print('View')
                values = [pos_1, pos_2, pos_3, pos_4, pos_5, turn]
                with open('positions.csv', 'w') as data:
                    data_writer = csv.writer(data, delimiter=',')

                    data_writer.writerow(positions)

            if event.button == 7:
                # menu button
                #run program
                print('Menu')


        if event.type == pygame.JOYAXISMOTION:
            #movement
            if event.axis == 4:
                # left trigger
                #have both motors go forward
                print('Lt')
                right_motor.set(-.01)
                left_motor.set(-.01)

            if event.axis == 5:
                # right trigger
                #have both motors go backward
                print('RT')
                right_motor.set(.01)
                left_motor.set(.01)



            if event.value[1] == 1:
                # up d-pad
                count += 1
                if count > 1:
                    count = 0

        if count == 1:
            setup()
            if event.button == 3:
                # y button
                return_home()

            if event.button == 7:
                # menu button
                #start fill
                fill()





pygame.quit()
