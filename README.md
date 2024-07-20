This is an item tracker for the Death's Door mod DeathsDoor.ItemChanger
## How to use
Just download the latest <a href="https://github.com/SpR3AD1/DD_rando_tracker/releases">release</a> and run the exe file.
There is nothing more to it if you've already got the mod set up.
## Prerequirements
Requires the latest version of the <a href="https://github.com/dpinela/DeathsDoor.ItemChanger/releases">DeathsDoor.ItemChanger</a> mod.
## How it works (for everyone interested)
Starting a randomizer using ItemChanger will create a file in your Death's Door SAVEDATA containing all the information about your seed and your current progress.
DD_rando_tracker will read that files and show respective data.
You can adjust the colors and the size of the tracker to match your stream. This configuration will be saved in your Death's Door Appdata-Folder.
## How to build (for developers)
```
pyinstaller --onefile --noconsole --clean --icon "icon.ico" --add-data "images;images" --add-data "themes/breeze-dark;themes/breeze-dark" --add-data "themes;themes" --paths "src" DD_rando_tracker.py
```
