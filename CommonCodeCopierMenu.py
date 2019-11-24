#!/usr/bin/python
import sys
import curses
import pyperclip

box_width        = 40   # Adjustable. Default size option set to 40. Minimum value of 35
box_height       = 30   # Default
input_box_height = 4    # Minimum value of 3

# screen.move(50, 50)


def draw_window(screen):
  # Initialize borders and color schema
  curses.start_color()
  screen.border(0)
  curses.use_default_colors()
  curses.init_pair(1, curses.COLOR_RED, -1)
  curses.init_pair(2, curses.COLOR_CYAN, -1)
  
  # Declaration of strings
  intro              = "Welcome to the"[:box_width-1]
  title              = "Common Code Copier"[:box_width-1]
  subtitle           = "by Eric McDaniel, November 2019"[:box_width-1]
  instructionsTop    = "Please choose one option from"[:box_width-1]
  instructionsBottom = "the following selection"[:box_width-1]

  # Define x starting position for flexible window creation
  start_x_intro              = int((box_width // 2) - (len(intro + title) // 2) - len(intro) % 2) + 1
  start_x_title              = int((box_width // 2)  - len(title) % 2)
  start_x_subtitle           = int((box_width // 2) - (len(subtitle) // 2) - len(subtitle) % 2) + 2
  start_x_instructionsTop    = int((box_width // 2) - (len(instructionsTop) // 2) - len(instructionsTop) % 2) + 2
  start_x_instructionsBottom = int((box_width // 2) - (len(instructionsBottom) // 2) - len(instructionsBottom) % 2) + 2
  
  # Render the text in appropriate location
  screen.addstr(1, start_x_intro, intro)
  screen.attron(curses.A_BOLD)
  screen.addstr(1, start_x_title, title, curses.color_pair(1))
  screen.attroff(curses.A_BOLD)
  screen.addstr(2, start_x_subtitle, subtitle)
  
  # Create main box and render centered instructions
  box1 = curses.newwin(box_height, box_width, 3, 1)
  box1.box()
  screen.refresh()
  box1.refresh()
  screen.addstr(4, start_x_instructionsTop, instructionsTop)
  screen.addstr(5, start_x_instructionsBottom, instructionsBottom)
  # Prints the horizontal bar across the top below the instructions
  for x in range(2, box_width):
    screen.addch(6, x, curses.ACS_HLINE)
  
  # Read the textfile
  Code = readFile()
  row = 7 # starting row, after instructions and window box lines
  for line in Code:
    screen.addstr(row, 3, "{}. {}".format((row - 6), line.strip()))
    row = row + 1
    
  # Draw User selection box
  input_box = curses.newwin(input_box_height, box_width - 2, box_height - input_box_height + 2, 2)
  input_box.box()
  input_box.refresh()
  screen.addstr(box_height - input_box_height + 3, 6, "User Selection: ", curses.color_pair(2))


  # Throw an exception if user input is improper
  selection = screen.getch()
  if (selection < 48 or selection > 48 + len(Code)):
    raise ValueError
  
  # Ascii value conversion of char 1 to decimal 1
  selection = selection - 49

  # 10 matches keyboard value of enter key, only save to clipboard when confirmed
  enterButtonPressed = screen.getch()  
  if (enterButtonPressed == 10):
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
