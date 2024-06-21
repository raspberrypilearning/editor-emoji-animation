<h2 class="c-project-heading--task">When does it happen?</h2>

--- task ---
➡️ Change when the flower grows
--- /task --- 

The global variable `grow` contains a frame number.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 6
---
grow = 150

--- /code ---
</div>

The `flower()` function contains code to check whether this frame number has passed, and if so, draw the flower.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 18
---
def flower():
    if seed_position >= 300:
        text('🌱', 200, 300)    
    if frame_count > grow: 
        draw_background()
        text('🌷', 200, 300)

--- /code ---
</div>

Change the frame number to change when your emoji appears. 

**Test:** Run your code and you should see the emoji you chose appearing earlier or later. 

<div class="c-project-callout c-project-callout--tip">

### Tip

You can create more variables containing frame numbers, and use them to control when different things happen in your animation.

</div>