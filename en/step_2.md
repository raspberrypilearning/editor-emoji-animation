## Background

> [!TASK]
>
> ➡️ Change the background colour

The `draw_background()` function contains the code to draw the background.

```python line_numbers="true" line_number_start="8"
def draw_background():
    BROWN = Color(185, 155, 115)
    BLUE = Color(130, 195, 255)
    background(BLUE) 
    fill(BROWN)
    rect(0,300,400,100)
```

Change the colour of the background.

## Now run your code

Run your code and see the new colour you have selected.

> [!TIP]
>
> Colours are created using (R)ed, (G)reen, and (B)lue values. Use a [colour picker](https://htmlcolorcodes.com/){:target="_blank"} to help you find the values for the colour you want.
