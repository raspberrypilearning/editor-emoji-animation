<h2 class="c-project-heading--task">Move speed</h2>

--- task ---
➡️ Make the seeds move faster or slower
--- /task --- 

The `sow_seeds()` function contains the code that tells the seeds to move down from the top of the screen. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 8
---
def sow_seeds():
    global seed_position
    if seed_position < 300:
        seed_position = seed_position + 5
        text('🫘', 200, seed_position)

--- /code ---
</div>

Change one of the numbers in the code so that the seeds move faster or slower.

**Test:** Run your code and see the seeds moving faster or slower. 

You will adjust the other timings in the next step.

<div class="c-project-callout c-project-callout--tip">

### Tip

If you are not sure, change one of the numbers and then run the code to see what happens!

</div>
