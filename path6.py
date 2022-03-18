import pygame
import csv

# start pygame
pygame.init()
running = True

joysticks = []
encoder1 = value1
encoder2 = value2
count = 0
save = 0
area = 0
area2 = none
pos_1 = (0, 0)
pos_2 = (0, 0)
pos_3 = (0,0)
turnDirect = ""
turn = ""
turn1 = ""
turn2 = ""
turn3 = ""
turn4 = ""


def setup():
    count = 0
    turnDirect = ""

    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 4:
            # left bumper
            # turn 90° to the left
            print('LB')
            turnDirect = '''L'''
        if event.button == 5:
            # right bumper
            # turn 90° the the right
            print('RB')
            turnDirect = '''R'''

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

        pos_4 = (pos_3 + '''90°''') + side1
        pos_5 = (pos_4 + '''90°''') + side2

        side1 = pos_2 - pos_1
        side2 = pos_3 - (pos_2 + '''90°''')

    area = side1 * side2


def turn90():
    turn = ""
    if turnDirect == "L":
        '''
        if encoder1 < (encoder1 + amount to turn):
            right motor +
            left motor -
        elif encoder1 == (encoder1 + amount to turn):
            stop motors
            turn = complete
        '''
    if turnDirect == "R":
        '''
        if encoder1 > (encoder1 - amount to turn):
            right motor +
            left motor -
        elif encoder1 == (encoder1 - amount to turn):
            motors stop
            turn = "complete"
        '''


def return_home():
    turn90()
    if (encoder1) < pos_4:
        #moveforward
    elif (encoder1) == pos_4:
        motorstop
        turn90()
        if (encoder1) < pos_5:
        # moveforward
        elif (encoder1) == pos_5:
            motorstop
            turn90()


def outline():
    '''
      if (encoder1) == 0:
          if (encoder1) < pos_2:
              motorforward
          elif (encoder1) == pos_2:
              motorstop
              turn90()
              if turn == "complete":
                  turn1 = "complete"
  
      if turn1 == "complete":
          if (encoder1) < pos_3:
              motorforward
          elif (encoder1) == pos_3:
              motorstop
              turn90()
              if turn == "complete":
                  turn2 = "complete"
  
  
      if turn2 == "complete":
          if (encoder1) < pos_4:
              motorforward
          elif (encoder1) == pos_4:
              motorstop
              turn90()
              if turn == "complete":
                  turn3 = "complete"
  
      if turn3 == "complete":
          if (encoder1) < pos_5:
              motorforward
          elif (encoder1) == pos_5:
              motorstop
              turn90()
              if turn == "complete":
                  turn4 = "complete"
                  area = (pos_2 - pos_1) * (pos_3 - (pos_2 + 90°))
    '''


def fill():
    '''
    t = 1
    if (encoder1) == 0:
        if (encoder1) < pos_2:
            motorforward
        elif (encoder1) == pos_2:
            motorstop
            turn90()
            if turn == "complete":
                turn1 = "complete"

    if turn1 == "complete":
        if (encoder1) < pos_3:
            motorforward
        elif (encoder1) == pos_3:
            motorstop
            turn90()
            if turn == "complete":
                turn2 = "complete"


    if turn2 == "complete":
        if (encoder1) < pos_4:
            motorforward
        elif (encoder1) == pos_4:
            motorstop
            turn90()
            if turn == "complete":
                turn3 = "complete"

    if turn3 == "complete":
        if (encoder1) < pos_5:
            motorforward
        elif (encoder1) == pos_5:
            motorstop
            turn90()
            if turn == "complete":
                turn4 = "complete"
                encoder1 = 0


    while (turn4 == "complete") and (area > 0):
        if encoder1 < (pos_2 - (x*t):
            motorforward
        elif encoder1 == (pos_2 - (x*t):
            motorstop
            turn90()
            if turn == "complete":
                if encoder1 < (pos_3 - (x*t)):
                    motorforward
                elif encoder1 == (pos_3 - (x*t):
                    motorstop
                    turn90()
                    if turn == "complete":
                        if encoder1 < (pos_4 - (x*t)):
                        motorforward
                    elif encoder1 == (pos_4 - (x*t):
                        motorstop
                        turn90()
                        if turn == "complete"

                            area2 = (pos2 - (x*t)) * (pos3 - (x*t))

                            if encoder1 < (pos_5 - (x*t)):
                                motorforward
                            elif encoder1 == (pos_5 - (x*t):
                                motorstop
                                turn90()
                                turn += 1
                                encoder1 = 0
                '''

# find and connect the xbox controller
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Detected joystick '" + joysticks[-1].get_name() + "'")

while True:
    # buttons, bumpers, and menu/view buttons
    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 0:
            # a button
            print('a')
        if event.button == 1:
            # b button
            # zero/reset
            print('b')
            count = 0
            encoder1 = 0
            pos_1 = 0
            pos_2 = 0
            pos_3 = 0
            pos_4 = 0


        if event.button == 2:
            # x button
            # load
            print('x')
        if event.button == 3:
            # y button
            print('y')
        if event.button == 4:
            # left bumper
            #turn 90° to the left
            print('LB')
        if event.button == 5:
            # right bumper
            #turn 90° the the right
            print('RB')
        if event.button == 6:
            # view button
            #save
            print('View')
        if event.button == 7:
            # menu button
            #run program
            print('Menu')

    # D-pad
    if event.type == pygame.JOYHATMOTION:
        if event.value[0] == 1:
            # right d-pad
            print('RDP')
        if event.value[0] == -1:
            # left d-pad
            print('LDP')
        if event.value[1] == 1:
            # up d-pad
            #set up mode
            print('UDP')
        if event.value[1] == -1:
            # down d-pad
            print('DDP')


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

    if event.type == pygame.JOYAXISMOTION: 
        if event.button == 6: # save pos values
            # view button
            positions = [pos_1, pos_2, pos_3, pos_4, pos_5]
            with open('positions.csv', 'w') as data:
                data_writer = csv.writer(data, delimiter=',')

                data_writer.writerow(positions)
        
        if event.button == 2: #load saved pos values
            # x button
            with open('positions.csv') as file: #opens and reads file
                reader = csv.reader(file)
                list = next(reader)

            #sets pos values to pos values in the csv file
            pos_1 = list[0]
            pos_2 = list[1]
            pos_3 = list[2]
            pos_4 = list[3]
            pos_5 = list[4]


    while True: #toggle set
        if start == 1:
            setup()
            if count == 2:
                if event.type == pygame.JOYAXISMOTION:
                    if event.button == 3:
                        # y button
                        return_home()
                        break

        if event.type == pygame.JOYHATMOTION:
            if event.value[1] == 1:
                if start == 0:
                    start = 1
                elif start == 1:
                    start = 0

    '''if event.value[1] == 1:
        # up d-pad
        setup()
        if count == 2:
            if event.button == 3:
                # y button
                return_home()'''

    if event.button == 7:
        # menu button
        #start fill
        encoder1 = 0
        turn = ""
        turn1 = ""
        turn2 = ""
        turn3 = ""
        turn4 = ""
        fill()





pygame.quit()
