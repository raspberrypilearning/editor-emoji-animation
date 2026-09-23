## Move speed

> [!TASK]
>
> ➡️ Make the seeds move faster or slower

The `sow_seeds()` function contains the code that tells the seeds to move down from the top of the screen.

```python line_numbers="true" line_number_start="22"
def sow_seeds():
    global seed_position
    if seed_position < 300:
        seed_position = seed_position + 5
        text('🫘', 200, seed_position)
```

Change one of the numbers in the code so that the seeds move faster or slower.

## Now run your code

Run your code and see the seeds moving faster or slower.

You will adjust the other timings in the next step.

> [!TIP]
>
> If you are not sure, change one of the numbers and then run the code to see what happens!
