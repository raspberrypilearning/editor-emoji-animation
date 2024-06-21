<h2 class="c-project-heading--task">Where does it start?</h2>

--- task ---
➡️ Change the starting position of the seeds
--- /task --- 

The `sow_seeds()` function contains code to draw the seed emoji at a `x`, `y` coordinate.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 22
line_highlights: 18
---
def sow_seeds():
    global seed_position
    if seed_position < 300:
        seed_position = seed_position + 5
        text('🫘', 200, seed_position)
--- /code ---
</div>

Change the value `200` and the value of the variable `seed_position` so that the seeds start in a different place. 

**Test:** Run your code and you should see the seeds start in a different place.

<div class="c-project-callout c-project-callout--tip">

### Tip

You might also want to change when the seeds stop, or the direction they move in. Can you work out which values to change to do this?

</div>