# Manim Starter (Community Edition)

This is a minimal starter to help you render your first Manim animation and keep your project tidy.

## 1) Create & activate a virtual environment
**Windows (PowerShell):**
```ps1
python -m venv .venv
.venv\Scripts\Activate.ps1
```
**macOS / Linux (bash/zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2) Install Manim
```bash
pip install --upgrade pip
pip install manim
```

## 3) Render a scene (no LaTeX needed)
```bash
manim -pql scenes/projection_intro.py ProjectionIntro
```
The `-pql` flag = preview + quick low quality.

## 4) (Optional) Enable LaTeX features
If you want the formula scene (`ProjectionFormula`), install a LaTeX distribution (e.g., MiKTeX on Windows, MacTeX on macOS, TeX Live on Linux).

Then run:
```bash
manim -pql scenes/projection_intro.py ProjectionFormula
```

## 5) Project layout
```
manim-starter/
├─ scenes/
│  └─ projection_intro.py
├─ assets/            # put images/audio here
├─ .gitignore
├─ requirements.txt
├─ render.sh          # macOS/Linux helper
├─ render.bat         # Windows helper
└─ README.md
```

## 6) Helpful commands
High quality export (1080p preset):
```bash
manim -pqh scenes/projection_intro.py ProjectionIntro
```

Export a transparent PNG sequence (for compositing) by adding `-t` and `-r` flags as needed; see docs for details.
