import pyautogui
import random

pyautogui.FAILSAFE = False


def Main():
    print("Main start")
    while (1):
        cutWood()
        pyautogui.sleep(4)
        createFire()
        pyautogui.sleep(4)
        returnToReset()
        pyautogui.sleep(4)
    return


def cutWood():
    for i in range(1, 7):
        print("Should we cut tree number " + str(i) + " ?")

        inventoryFull = pyautogui.locateCenterOnScreen(
            "./assets/actions/inventory full.png", confidence=0.8)

        if inventoryFull is not None:
            print("Inventory is full, let's create a fire to get rid of some wood")
            createFire()
        else:
            print("No not necessary")

        # Get the tree coordinates first
        treeCoords = pyautogui.locateCenterOnScreen(
            "./assets/trees/tree"+str(i)+".png", confidence=0.3)

        if treeCoords is not None:
            # Get Tree X and Tree Y
            # Also, let's slightly randomize the number
            treeX = treeCoords[0] + random.randrange(-5, 5)
            treeY = treeCoords[1] + random.randrange(-5, 5)

            # Move mouse to tree and click on the screeen
            pyautogui.moveTo(treeX, treeY)
            # sleep to give the UI time to show up
            pyautogui.sleep(0.5)
            pyautogui.rightClick(treeX, treeY)

            # Let's grab the chop down action
            chopDownCoords = pyautogui.locateCenterOnScreen(
                "./assets/actions/chop down tree.png", confidence=0.8)

            pyautogui.sleep(1)

            if chopDownCoords is not None:
                chopX = chopDownCoords[0] + random.randrange(-5, 5)
                chopY = chopDownCoords[1] + random.randrange(-5, 5)

                pyautogui.moveTo(chopX, chopY)
                pyautogui.sleep(0.5)
                pyautogui.click(chopX, chopY)
                print("Chopping down tree: " + str(i))
                pyautogui.sleep(8)

            else:
                print("Chop down action could not be located...")
                pyautogui.sleep(1.5)

        else:
            print("No trees could be found, let's return from this function")
            return


def returnToReset():
    reset = pyautogui.locateCenterOnScreen(
        "./assets/actions/reset.png", confidence=0.4)

    if reset is not None:
        print("Found reset!")
        resetX = reset[0]
        resetY = reset[1]

        pyautogui.moveTo(resetX, resetY)
        pyautogui.sleep(0.5)
        pyautogui.click(resetX, resetY)
    else:
        print("Reset was not found!")
    return


def createFire():
    standingOnFire = pyautogui.locateOnScreen(
        "./assets/actions/standing on fire.png", confidence=0.7)

    if standingOnFire is not None:
        print("No we are already standing on a fire")
        return

    tinderBox = pyautogui.locateCenterOnScreen(
        "./assets/inventory/tinderbox.png", confidence=0.7)

    if tinderBox is not None:
        numOfFires = 0
        print("Tinder box is found! We should create a fire!")
        while (numOfFires < 5):
            standingOnFireAgain = pyautogui.locateOnScreen(
                "./assets/actions/standing on fire.png", confidence=0.7)
            if standingOnFireAgain is not None:
                print(
                    "Just double checking and we found that we are standing on fire again... let's return")
                return
            else:
                print("We're good to make a fire!")
                tinderBoxX = tinderBox[0]
                tinderBoxY = tinderBox[1]

                wood = pyautogui.locateCenterOnScreen(
                    "./assets/inventory/wood.png", confidence=0.7)

                if wood is not None:
                    print("Lighting up our " +
                          str(numOfFires + 1) + "piece of wood")

                    # Get wood x and y
                    # Move to click wood
                    pyautogui.moveTo(wood[0], wood[1])
                    pyautogui.sleep(0.5)
                    pyautogui.click(wood[0], wood[1])
                    # sleep between actions
                    pyautogui.sleep(1.5)
                    # move to tinder box
                    pyautogui.moveTo(tinderBoxX, tinderBoxY)
                    pyautogui.sleep(0.5)
                    pyautogui.click(tinderBoxX, tinderBoxY)

                    # Wait for it to light
                    pyautogui.sleep(7)
                    numOfFires = numOfFires + 1
                    print(
                        "We have successfully lit this number of fires: " + str(numOfFires))

                else:
                    print("Wood could not be found, return")
                    return

    return


Main()
