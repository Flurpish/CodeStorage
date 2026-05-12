import time
import curses

from Board import displayBoard, pieceDown, pieceLeft, pieceRight, pieceRotate

MOVEMENT_DELAY = 0.3 # In seconds, the time it takes to move the piece

def main(stdscr):
    curses.noecho() # Won't show user input
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True) # No while waiting for user input


    while(True):
        input = stdscr.getch()
        while input != -1:
            match input:
                case curses.KEY_LEFT:
                    pieceLeft()
                case curses.KEY_RIGHT:
                    pieceRight()
                case curses.KEY_DOWN:
                    pieceDown()
                case curses.KEY_UP:
                    pieceRotate()
                case curses.KEY_END:
                    stdscr.clear()
                    stdscr.addstr("Thanks for playing!")
                    stdscr.refresh()

                    time.sleep(1)
                    break

            input = stdscr.getch() # This gets out of the while loop

        displayBoard(stdscr)
        time.sleep(MOVEMENT_DELAY)

        #Move piece downward every movement_delay
        pieceDown()

        #Clear the window so we don't spam prints
        stdscr.clear()

curses.wrapper(main)