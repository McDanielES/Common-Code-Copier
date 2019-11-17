#!/usr/bin/python
import sys
import curses


# def main():

  
  
  
  
def init(screen):
  screen.border(0)
  
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
  except EOFError:
    sys.exit(2)