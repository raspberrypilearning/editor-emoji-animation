## Another emoji

> [!TASK]
>
> ➡️ Add a function to draw another emoji

You can create a new function to draw and animate another emoji.

```python line_numbers="true" line_number_start="7" line_highlights="7-8"
def my_function_name():
    text('🦙', 300, 300)
```

Create a new function and use it to draw another emoji. Call the function inside `draw()`.

## Now run your code

Run your code and see your new emoji.

> [!DEBUG]
>
> You need to call your function inside `draw()` for it to execute.
>
> ```python line_numbers="true" line_number_start="34" line_highlights="38"
> def draw(): 
>     draw_background()
>     flower()
>     sow_seeds()
>     my_function_name()
> ```
