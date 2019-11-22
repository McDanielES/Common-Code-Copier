#!/usr/bin/python
import sys
import curses

def init(screen):
  curses.start_color()
  curses.use_default_colors()
  curses.init_pair(1, curses.COLOR_RED, -1)

  screen.border(0)
  screen.addstr(1, 5, "Welcome to the")
  screen.attron(curses.A_BOLD)
  screen.addstr(1, 20, "Common Code Copier", curses.color_pair(1))
  screen.attroff(curses.A_BOLD)
  screen.addstr(2, 6, "by Eric McDaniel, November 2019")
  
  box1 = curses.newwin(30, 40, 3, 1)
  box1.box()
  screen.refresh()
  box1.refresh()

  screen.getch()
  

def main():
  init(curses.initscr())
  from subprocess import call
  call("exit 0", shell=True)

# Start Program with main
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit(1)
  except Exception:
    sys.exit(2)