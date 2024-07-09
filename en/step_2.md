<h2 class="c-project-heading--task">Background</h2>

--- task ---
➡️ Change the background colour
--- /task --- 

The `draw_background()` function contains the code to draw the background. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 8
---
def draw_background():
    BROWN = Color(185, 155, 115)
    BLUE = Color(130, 195, 255)
    background(BLUE) 
    fill(BROWN)
    rect(0,300,400,100)

--- /code ---
</div>

Change the colour of the background. 

**Test:** Run your code and see the new colour you have selected. 

<div class="c-project-callout c-project-callout--tip">

### Tip

Colours are created using (R)ed, (G)reen, and (B)lue values. Use a [colour picker](https://htmlcolorcodes.com/){:target="_blank"} to help you find the values for the colour you want. 

</div>
