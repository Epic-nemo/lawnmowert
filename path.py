import pygame

# start pygame
pygame.init()
running = True

joysticks = []
encoder1 = value1
encoder2 = value2
count = 0
area = 0
area2 = none
pos_1 = (0, 0)
pos_2 = (0, 0)
pos_3 = (0, 0)
pos_4 = (0, 0)
turn = ""
turn1 = ""
turn2 = ""
turn3 = ""
turn4 = ""

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
            encoder2 = 0
            pos_1 = (0, 0)
            pos_2 = (0, 0)
            pos_3 = (0, 0)
            pos_4 = (0, 0)

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
            print('UDP')
        if event.value[1] == -1:
            # down d-pad
            print('DDP')

    # triggers and joystick
    if event.type == pygame.JOYAXISMOTION:
        if event.axis == 4:
            # left trigger
            #have both motors go forward
            print('Lt')
        if event.axis == 5:
            # right trigger
            #have both motors go backward
            print('RT')

    def outline():
      '''
      if (encoder1, encoder2) == (0,0):
            if (encoder1, encoder2) < pos_1:
                motorforward
            if (encoder1, encoder2) == pos_1:
                motorstop
                if turn == "right":
                    turn 90° right
                    turn1 = "complete"
                if turn == "left":
                    turn 90° left
                    turn1 = "complete"
        if turn1 == "complete":
            if (encoder1, encoder2) != pos_2:
                motorforward
            else if (encoder1, encoder2) == pos_2:
                motorstop
                if turn == "right":
                    turn 90° right
                    turn2 = "complete"
                if turn == "left":
                    turn 90° left
                    turn2 = "complete"
        if turn2 == "complete":
            if (encoder1, encoder2) != pos_3:
                motorforward
            else if (encoder1, encoder2) == pos_3:
                motorstop
                if turn == "right":
                    turn 90° right
                    turn3 = "complete"
                if turn == "left":
                    turn 90° left
                    turn3 = "complete"
        if turn2 == "complete":
            if (encoder1, encoder2) != pos_4:
                motorforward
            else if (encoder1, encoder2) == pos_4:
                motorstop
                if turn == "right":
                    turn 90° right
                    turn4 = "complete"
                if turn == "left":
                    turn 90° left
                    turn4 = "complete"
      '''

    def fill():
        '''
        if (encoder1, encoder2) == (0,0):
            if (encoder1, encoder2) < pos_1:
                motorforward
            if (encoder1, encoder2) == pos_1:
                motorstop
                if turn == "right":
                    turn 90° right
                    turn1 = "complete"
                if turn == "left":
                    turn 90° left
                    turn1 = "complete"
        if turn1 == "complete":
            if (encoder1, encoder2) != pos_2:
                motorforward
            else if (encoder1, encoder2) == pos_2:
                motorstop
                if turn == "right":
                    turn 90° right
                    turn2 = "complete"
                if turn == "left":
                    turn 90° left
                    turn2 = "complete"
        if turn2 == "complete":
            if (encoder1, encoder2) != pos_3:
                motorforward
            else if (encoder1, encoder2) == pos_3:
                motorstop
                if turn == "right":
                    turn 90° right
                    turn3 = "complete"
                if turn == "left":
                    turn 90° left
                    turn3 = "complete"
        if turn3 == "complete":
            if (encoder1, encoder2) != pos_4:
                motorforward
            else if (encoder1, encoder2) == pos_4:
                motorstop
                if turn == "right":
                    turn 90° right
                    turn4 = "complete"
                if turn == "left":
                    turn 90° left
                    turn4 = "complete"

        repeat until area = 0
            motor forward until (encoder1, encoder2) is x amount less of pos1
            turn 90
            motor forward until (encoder1, encoder2) is x amount less of pos2
            turn 90
            motor forward until (encoder1, encoder2) is x amount less of pos3
            turn 90
            motor forward until (encoder1, encoder2) is x amount less of pos4
            area2 = (pos_2-pos_1) * (pos_3-pos_2)
                    '''





    if event.button == 0 and count == 0:
        # a button
        pos_1 = (0, 0)
        if event.button == 3:
            # y button
            turn = "right"
        if event.button == 4:
            # left bumper
            #turn 90° to the left
            turn = "left"
        count = count + 1
        if event.button == 0 and count == 1:
            # a button
            pos_2 = (encoder1, encoder2)
            count = count + 1
        if event.button == 0 and count == 2:
            # a button
            pos_3 = (encoder1, encoder2)
            count = count + 1
        if event.button == 0 and count == 3:
            # a button
            pos_4 = (encoder1, encoder2)
            count = count + 1

        #area = (pos_2-pos_1) * (pos_3-pos_2)

    if event.button == 7:
        # menu button
        # run program
        outline()





pygame.quit()
