import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
counter = 0
while True:
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 20, "Up")
        break
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(3, 20, "Down")
        counter += 1
        print(counter)


curses.endwin()