# Manim Animation Project Guidelines

This project uses [Manim Community Edition](https://www.manim.community/) to create mathematical animations. Here's what you need to know to work effectively in this codebase:

## Project Structure

- `scenes/`: Contains all animation scene classes
  - Each file defines one or more scene classes that inherit from `Scene`
  - Files are organized by topic/episode (e.g., `Ep1_WhatIsLinearSystem/`)
- `media/`: Generated animation outputs (videos, images, LaTeX)
- Helper scripts:
  - `render.bat` (Windows) / `render.sh` (Unix): Scene rendering shortcuts

## Key Conventions

### Scene Organization
```python
class MyScene(Scene):
    def construct(self):
        # 1. Configure scene (e.g., background)
        self.camera.background_color = "#080818"  # Dark background is standard
        
        # 2. Create and position objects
        # 3. Define animations
        # 4. Play animations sequence
```

### Animation Patterns

1. Group related objects with `VGroup`:
```python
objects = VGroup(obj1, obj2, obj3).arrange(DOWN, buff=0.35)
```

2. Common positioning:
```python
element.to_edge(UP)       # Move to top edge  
element.next_to(ref, DOWN, buff=0.12)  # Position below with spacing
```

3. Sequential animations with timing:
```python
self.play(FadeIn(obj, run_time=0.6))
self.play(LaggedStart(Write(obj1), Write(obj2), lag_ratio=0.2))
```

### Color Conventions
- Use constants for consistent coloring
- Light colors on dark background (#080818)
- Color-code related objects (e.g., `YELLOW` for oat milk elements)

## Development Workflow

1. Setup environment:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate   # Unix
pip install manim
```

2. Create new scene:
   - Add new .py file in `scenes/`
   - Define scene class inheriting from `Scene`
   - Implement `construct()` method

3. Test/preview (low quality, fast):
```bash
manim -pql scenes/your_file.py YourScene
```

4. Final render (high quality):
```bash
manim -pqh scenes/your_file.py YourScene
```

## Best Practices

1. Document scene flow in docstrings:
```python
class ExampleScene(Scene):
    """
    Sequence:
      1) First create/show X
      2) Then animate Y
      3) Finally transform into Z
    """
```

2. Break complex animations into commented sections:
```python
# -------- 1) Initial setup --------
...
# -------- 2) Main animation sequence --------
```

3. Reuse helper functions for common patterns:
```python
def make_col(vec, color, col_index):
    entries = VGroup(...).arrange(DOWN)
    return entries
```

4. Keep timing consistent:
- Quick transitions: 0.3-0.6s
- Standard animations: 0.8-1.0s
- Complex sequences: Use `LaggedStart` with 0.2 lag ratio

## Common Gotchas

- Remember to call `self.wait()` after important steps to let viewers process the scene
- Use `buff` parameter when arranging objects to prevent overlap
- For LaTeX, install a distribution (MiKTeX on Windows, MacTeX on macOS) before using `MathTex`
- Video output is in `media/videos/[quality]/[SceneName].mp4`