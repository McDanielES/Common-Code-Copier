#!/usr/bin/python
import sys
import curses
import pyperclip

box_width  = 40
box_height = 30
input_box_height = 6

# screen.move(50, 50)


def draw_window(screen):
  curses.start_color()
  curses.use_default_colors()
  curses.init_pair(1, curses.COLOR_RED, -1)
  curses.init_pair(2, curses.COLOR_CYAN, -1)

  screen.border(0)
  screen.addstr(1, 5, "Welcome to the")
  screen.attron(curses.A_BOLD)
  screen.addstr(1, 20, "Common Code Copier", curses.color_pair(1))
  screen.attroff(curses.A_BOLD)
  screen.addstr(2, 6, "by Eric McDaniel, November 2019")
  
  
  box1 = curses.newwin(box_height, box_width, 3, 1)
  box1.box()
  screen.refresh()
  box1.refresh()
  screen.addstr(4, 6, "Please choose one option from")
  screen.addstr(5, 9, "the following selection")
  for x in range(2, box_width):
    screen.addch(6, x, curses.ACS_HLINE)
  
  # Read the textfile
  Code = readFile()
  row = 7 # starting row
  for line in Code:
    screen.addstr(row, 3, "{}. {}".format((row - 6), line.strip()))
    row = row + 1
    
  # Draw User selection box
  input_box = curses.newwin(input_box_height, box_width - 2, box_height - input_box_height + 2, 2)
  input_box.box()
  input_box.refresh()
  screen.addstr(box_height - 3, 6, "User Selection: ", curses.color_pair(2))


  # Throw an exception if user input is improper
  selection = screen.getch()
  if (selection < 48 or selection > 48 + len(Code)):
    raise ValueError
  
  # Ascii value conversion of char 1 to decimal 1
  selection = selection - 49
  pyperclip.copy(Code[int(selection)])

  
  screen.getch()  

def readFile():
  clipboard = open("code-options.txt", "r")
  count = 1
  codeList = []
  for line in clipboard:
    codeList.append(line)
    count = count + 1    
  clipboard.close()
  return codeList  

def main():
  draw_window(curses.initscr())

  # from subprocess import call
  # call("exit 0", shell=True)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit(1)
  except ValueError:
    sys.exit(2)
