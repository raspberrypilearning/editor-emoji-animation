<h2 class="c-project-heading--task">Background</h2>

Change the background colour

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

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

### Tip
<div class="c-project-callout c-project-callout--tip">
Colours are created using (R)ed, (G)reen, and (B)lue values. Use a [colour picker](https://htmlcolorcodes.com/){:target="_blank"} to help you find the values for the colour you want.
</div>

## Now run your code

Check the new colour you have selected.
