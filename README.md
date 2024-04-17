This is an Item Tracker for the Death's Door Mod DeathsDoor.ItemChanger
## Prerequirements
Download the latest release of <a href="https://github.com/dpinela/DeathsDoor.ItemChanger/releases">DeathsDoor.ItemChanger</a>
## How it works
Starting a randomizer using ItemChanger will create a file in your Death's Door SAVEDATA containing all the information about your seed and your current progress.
DD_rando_tracker will read that files and show respective data.
You can adjust the colors and the size of the tracker to match your stream. This configuration will be saved in your Death's Door Appdata-Folder.
## How to build
```
pyinstaller --onefile --noconsole --clean --icon "icon.ico" --add-data "images;images" --add-data "themes/breeze-dark;themes/breeze-dark" --add-data "themes;themes" --paths "src" DD_rando_tracker.py
```
