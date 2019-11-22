#!/usr/bin/python
import sys
import pyperclip

def main():
  # pyperclip.copy('The text to be copied to the clipboard.')
  # spam = pyperclip.paste()
  # print(spam)
  
  clipboard = open("code-options.txt", "r")
  print("Please choose one option from the following")
  count = 1
  codeList = []
  for line in clipboard:
    codeList.append(line)
    print("  {}. {}".format(count, line), end="")
    count = count + 1
  print("\nYour selection: ", end="")
  selection = input()
  print("You chose:")
  print(codeList[int(selection) - 1])
  
  


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit(1)
  except Exception:
    sys.exit(2)