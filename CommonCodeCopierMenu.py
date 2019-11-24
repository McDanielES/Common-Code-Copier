#!/usr/bin/python
import sys
import curses
import pyperclip

window_height = 40
window_width  = 30


def draw_window(screen):
  curses.start_color()
  curses.use_default_colors()
  curses.init_pair(1, curses.COLOR_RED, -1)

  screen.border(0)
  screen.addstr(1, 5, "Welcome to the")
  screen.attron(curses.A_BOLD)
  screen.addstr(1, 20, "Common Code Copier", curses.color_pair(1))
  screen.attroff(curses.A_BOLD)
  screen.addstr(2, 6, "by Eric McDaniel, November 2019")
  
  
  box1 = curses.newwin(window_width, window_height, 3, 1)
  box1.box()
  screen.refresh()
  box1.refresh()
  screen.addstr(4, 6, "Please choose one option from")
  screen.addstr(5, 9, "the following selection")
  for x in range(2, window_height):
    screen.addch(6, x, curses.ACS_HLINE)
  
  # Read the textfile
  Code = readFile()
  row = 7 # starting row
  for line in Code:
    screen.addstr(row, 3, "{}. {}".format((row - 6), line.strip()))
    row = row + 1

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
    
  # print("\nYour selection: ", end = "")
  # selection = input()
  # print("You chose:")
  # print(codeList[int(selection) - 1])

  # pyperclip.copy(codeList[int(selection) - 1])
  
# Implement
def getWindowText(file):
  Text = []
  

def main():
  draw_window(curses.initscr())

  # from subprocess import call
  # call("exit 0", shell=True)

# Start Program with main
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit(1)
