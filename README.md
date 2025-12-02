# Monster Notes

This is a python based terminal app that runs on the Code Institute mock terminal on Heroku. 

It is a note taking app with a monster theme

[Here is the link to the deployed project](https://monster-notes-d2488111218c.herokuapp.com/)

<img width="537" height="325" alt="Menu Screen" src="https://github.com/user-attachments/assets/e0990cad-c46a-4853-94e4-bd769aaad6db" />

## Table of Contents

1. [Flowchart](#flowchart)
2. [How to use](#how-to-use)
3. [Features](#features)
   - [Existing Features](#existing-features)
   - [Future Features](#future-features)

4. [Testing](#testing)
   - [Validator Testing](#validator-testing)

5. [Bugs](#bugs)
   - [Solved Bugs](#solved-bugs)
   - [Remaining Bugs](#remaining-bugs)

6. [Deployment](#deployment)

7. [Credits](#credits)

## Flowchart

<img width="781" height="516" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/b4d9115f-a32e-4992-bf4d-ae3171f9013e" />


## How to use

Monster notes is a function terminal based notes app. 

Users enter a note which is saved as a text file

Users can also read, alter or delete notes


## Features

### Existing Features

- Notes are saved upon entry
  - Notes are saved as a text file with timestamps

<img width="537" height="325" alt="Note Saved" src="https://github.com/user-attachments/assets/15dad170-dfa6-4791-826d-dafb9aa73c9c" />


- Ability to alter notes

<img width="537" height="325" alt="Amending Note" src="https://github.com/user-attachments/assets/b9a6955d-5206-415e-8781-b64700af2aa8" />


- Option to delete notes

<img width="537" height="325" alt="Deletion Confirmation" src="https://github.com/user-attachments/assets/9b70ee9d-9fbf-4fa1-89df-2d9a8f318a14" />


- Input validation
  - When inputting a menu option you must enter numbers
  - Empty notes will not save
 
  <img width="537" height="325" alt="Menu Validation" src="https://github.com/user-attachments/assets/27520de3-e2dd-493e-8310-ef55aa667a2e" />
  


### Future Features

- Export notes as pdf
- Generate to do list from notes
- Develop GUI for notes app

## Testing

I have manually tested this project by doing the following:

- I have passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: string where numbers are expected, where text is expected.
- I have also tested this on my local terminal and the Code Institute terminal on heroku

## Validator Testing
- PEP8
  - No errors were returned from [PEP8](https://pep8ci.herokuapp.com/)
<img width="400" height="300" alt="Screenshot 2025-12-02 144759" src="https://github.com/user-attachments/assets/7a211023-2c90-497e-b925-80023b9c5a90" />

### Bugs

#### Solved Bugs

- While writing the project I was getting an error that the save option wasnt working. This was due to it not checking there was text present
- For the ASCII Art and the menu was not displaying below the image. This was due to the menu not being nested under the image.

#### Remaining Bugs
- No bugs remaining

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment
 - Fork or clone this repository
 - Create a new Heroku app
 - Set the buildbacks to Python and NodeJS in that order
 - Link the Heroku app to the repository
 - Click on Deploy

## Credits
- Code Institute for the deployment terminal
- [tomi3-11](https://github.com/tomi3-11) for the initial notes idea

