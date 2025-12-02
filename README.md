# Monster Notes

This is a python based terminal app that runs on the Code Institute mock terminal on Heroku. 

It is a note taking app with a monster theme

## How to use

Monster notes is a function terminal based notes app. 

Users enter a note which is saved as a text file

Users can also alter or delete notes 


## Features

### Existing Features

- Notes are saved upon entry
  - Notes are saved as a text file with timestamps
- Ability to alter notes
- Option to delete notes
- Input validation
  - When inputting a menu option you must enter numbers
  - Empty notes will not save

### Future Features

- Export notes as pdf
- Generate to do list from notes
- Develop GUI for notes app

## Testing

I have manually tested this project by doing the following:

- I have passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: string where numbers are expected, where text is expected.
- I have also tested this on my local terminal and the Code Institute terminal on heroku

### Bugs

#### Solved Bugs

- While writing the project I was getting an error that the save option wasnt working. This was due to it not checking there was text present
- For the ASCII Art and the menu was not displaying below the image. This was due to the menu not being nested under the image.

#### Remaining Bugs
- No bugs remaining

## Validator Testing
- PEP8
  - No errors were returned from [PEP8](https://pep8ci.herokuapp.com/)
<img width="400" height="300" alt="Screenshot 2025-12-02 144759" src="https://github.com/user-attachments/assets/7a211023-2c90-497e-b925-80023b9c5a90" />

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

