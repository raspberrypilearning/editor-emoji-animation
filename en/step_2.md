<h2 class="c-project-heading--task">Emoji</h2>

Change the flower emoji to another emoji

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

The `flower()` function contains the code to draw the flower.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 15
---
def flower():
    if seed_position >= 300:
        text('🌱', 200, 300)
    if frame_count > grow:
        draw_background()
        text('🌷', 200, 300)

--- /code ---
</div>

Change the flower emoji to a different emoji, so that something else grows!

### Tip
<div class="c-project-callout c-project-callout--tip">
You can search for and copy emojis from an [emoji chooser](https://emojipedia.org/){:target="_blank"}.
</div>

## Now run your code

Check your new emoji at the end of the animation.
