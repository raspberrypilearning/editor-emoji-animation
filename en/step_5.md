## When does it happen?

> [!TASK]
>
> ➡️ Change when the flower grows

The global variable `grow` contains a frame number.

```python line_numbers="true" line_number_start="6"
grow = 150
```

The `flower()` function contains code to check whether this frame number has passed, and if so, draw the flower.

```python line_numbers="true" line_number_start="15" line_highlights="18"
def flower():
    if seed_position >= 300:
        text('🌱', 200, 300)    
    if frame_count > grow: 
        draw_background()
        text('🌷', 200, 300)
```

Change the value of the variable `grow` to change when your emoji appears.

## Now run your code

Run your code and see the emoji you chose appear earlier or later.

> [!TIP]
>
> You can create more variables containing frame numbers, and use them to control when different things happen in your animation.
