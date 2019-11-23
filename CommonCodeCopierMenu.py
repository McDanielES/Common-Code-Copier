#!/usr/bin/python
import sys
import curses
import pyperclip

window_height = 40
window_width  = 30


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
  
  box1 = curses.newwin(window_width, window_height, 3, 1)
  box1.box()
  screen.refresh()
  box1.refresh()

  screen.getch()
  
def readFile():
  clipboard = open("code-options.txt", "r")
  print("Please choose one option from the following")
  count = 1
  codeList = []
  for line in clipboard:
    codeList.append(line)
    print("  {}. {}".format(count, line), end = "")
    count = count + 1
  print("\nYour selection: ", end = "")
  selection = input()
  print("You chose:")
  print(codeList[int(selection) - 1])

  pyperclip.copy(codeList[int(selection) - 1])
  
# Implement
def getWindowText():
  Text = []
  Text.append("Please choose one option from the following")
  

def main():
  # readFile()
  init(curses.initscr())
  # from subprocess import call
  # call("exit 0", shell=True)

# Start Program with main
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit(1)
