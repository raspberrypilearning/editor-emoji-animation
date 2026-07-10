## Emoji

> [!TASK]
>
> ➡️ Change the flower emoji to another emoji

The `flower()` function contains the code to draw the flower.

```python line_numbers="true" line_number_start="15"
def flower():
    if seed_position >= 300:
        text('🌱', 200, 300)    
    if frame_count > grow: 
        draw_background()
        text('🌷', 200, 300)
```

Change the flower emoji to a different emoji, so that something else grows!

## Now run your code

Run your code and see your new emoji at the end of the animation.

> [!TIP]
>
> You can search for and copy emojis from an [emoji chooser](https://emojipedia.org/){:target="_blank"}.
