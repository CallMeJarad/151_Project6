#Jarad Aker
#the bad guys stop before the edge of the left side for reasons I couldn't figure out
import graphics
import time
#comment each function to troubleshoot
def main():
    window = graphics.GraphWin("Project 6", 1100, 900)
    hero = GoodGuy(window)
    bad_guys = BadGuys(window)
    Move_Stuff(window,hero,bad_guys)
    window.getMouse()
def GoodGuy(window):
    hero = graphics.Image(graphics.Point(550, 700), "horseman-ne-attack6.gif")
    hero.draw(window)
    return hero
# hero image dimensions 90x72
def BadGuys(window):
    #create list for bad guys instead of variable for each bad guy
    bad_guy_list = []
    for i in range(10):
        bad_guy = graphics.Image(graphics.Point(32 + i * 75, 150), "burner-fly-2.gif")
        bad_guy_list.append(bad_guy) #append adds to list
        bad_guy.draw(window)
    return bad_guy_list
# bad guy image dimensions 72x102
def Move_Stuff(window, hero, bad_guy_list,):
    #use first and last bad guy when touching edge of window to change direction
    dx = 0
    dy = 0
    while True:
# 1064 pixels for right of window\
        for bad_guy in bad_guy_list:
            center = bad_guy.getAnchor()
            xLoc = center.getX()
            if xLoc > 1064:


                for bad_guy in bad_guy_list:
                    bad_guy.move(-35, 0)
                    time.sleep(.0001)
                    if xLoc < 0:
                        for bad_guy in bad_guy_list:
                            bad_guy.move(30, 0)
                            time.sleep(.0001)

        for bad_guy in bad_guy_list:#origional bad guy movement
            bad_guy.move(30, 0)
            time.sleep(.0001)

#image moves slightly off of screen on left
            key = window.checkKey()
            hero.move(dx, dy)
            if key == "a":
                hero.move(-20, 0)
            if key == "d":
                hero.move(20, 0)


main()