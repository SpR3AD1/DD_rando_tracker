This is an Item Tracker for the Death's Door Mod DeathsDoor.ItemChanger
## Prerequirements
Download the latest release of <a href="https://github.com/dpinela/DeathsDoor.ItemChanger/releases">DeathsDoor.ItemChanger</a>
## How it works
Starting a randomizer using ItemChanger will create a file in you Death's Door SAVEDATA containing all the information about your seed and your current progress.
DD_rando_tracker will read that file and show respective data.
## How to build
```
pyinstaller --onefile --noconsole --clean --icon="icon.ico" --add-data="images;images" DD_rando_tracker.py
```
