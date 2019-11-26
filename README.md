# Common Code Copier
### A solution to boost efficiency and copy common code snippets into users' clipboards for faster software development
![Two instances of the application running](https://i.imgur.com/T3CwboH.png)

<i>Image 1. Two instances of the application running. Left: the main menu. Right: Help and Instructions</i>

---

Welcome to Common Code Copier, written by Eric McDaniel - November 2019.

#### Purpose
The inspiration for this program came from developing other software. I found myself wasting an absurd amount of time rewriting the same lines of code over and over again. While debugging a code in a java project, I would frequently type `System.out.println();` throughout the project, so much where I fantasized the thought of copying and pasting the line instead of writing it out explicitly. 

#### Installation
This script has one dependency, `pyperclip`, so you must install `pyperclip` before attempting to run this application.
```
sudo pip install pyperclip
```
You can test that this application is functioning normally from the command line by entering in the project root directory `python3 CommonCodeCopierMenu.py`. A curses menu should appear as pictured above (on the left) and should guide you from there.

#### To Run This Application
Included in this repo is a text file titled `code-options.txt` of some code that you'd like to have available for use. This is the file that you can customize by adding and removing lines of code, which you cannot do from the application directly. Also included in this repo is a bash shell script. First make it executable by typing in the command line:
```
sudo chmod u+x CommonCodeCopier.sh
```
Then, to get the most out of this program, configure your keyboard to bind a key combination to the `CommonCodeCopier.sh` script. This script will automatically call the python script, rendering the curses window and will display the options. This can be done from your window manager's .config file on Linux desktops as well.

#### Troubleshooting
+ If the python script does not open and exits with error code 3, it means the terminal window is too small and needs to be enlarged. Terminal font sizes vary, so stating how many pixels at minimum won't be too helpful. Some experimentation is necessary. Another possibility is that the `code-options.txt` text file with all of the customized code options has too much text written into it, which cannot be rendered on to the screen. Either grow window size or shrink file to resolve the issue.
+ If the python script exits with exit code 2, then nothing was copied to the clipboard. An improper value was received, such as a '5' when it expected a ranger between 1 to 3, or a letter, etc. Adjust accordingly.

#### Contact the Author
Should you find an error in the program or would like to contact me for any suggestions, improvements, or threats, you can use GitHub's `@McDanielES` mention system to contact me. I will try to respond as soon as I am available.

I am a third-year computer science student at the University of Wisconsin - Madison. I am learning the fundamentals of programming in Java, Python, and C/C++. This program was written primarily for my benefit and to apply the skills learned in class into a real-world context. I am aware that it may not be realistic and often crude or unsophisticated. But <i>live and learn</i>.

You are free to clone, fork, modify and use this application as you please.