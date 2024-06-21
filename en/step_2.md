### Setup your project



Add code to `setup()` to get your project ready. 



**Choose:** Add a size that suits the pattern you want to create. You can always change this later as your project evolves.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 7
---
def setup():
    size(400, 400)  # Choose a size 

--- /code ---




Think about where you want to draw your background. You can:
+ Add code to `setup()` so that the background is drawn once when you run your project  
+ Add code to `draw()` so that the background is redrawn each time the `draw()` function runs

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 8
---
def setup():
    size(400, 400)
    background(255, 255, 255)  # Try different numbers to change the colour 

--- /code ---

