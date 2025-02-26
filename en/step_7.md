<h2 class="c-project-heading--task">Another emoji</h2>

--- task ---
➡️ Add a function to draw another emoji
--- /task --- 

You can create a new function to draw and animate another emoji.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 18
---
def my_function_name():
    text('🦙', 300, 300)
--- /code ---
</div>

Create a new function and use it to draw another emoji. Call the function inside `draw()`.

**Test:** Run your code and see your new emoji.


<div class="c-project-callout c-project-callout--debug">

### Debugging

You need to call your function inside `draw()` for it to execute.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 34
line_highlights: 38
---
def draw(): 
    draw_background()
    flower()
    sow_seeds()
    my_function_name()
--- /code ---
</div>

</div>
