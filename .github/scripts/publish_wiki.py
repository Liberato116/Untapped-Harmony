from pathlib import Path

SOURCE = Path("progress/latest-release.md")
TARGET = Path("wiki/Latest-MC-Release-Mod-list-progress.md")

content = f"""# Latest Minecraft Release – Mod Progress

This page is **auto-generated** from the repository.
Do not edit directly.

---

{SOURCE.read_text(encoding="utf-8")}
"""

TARGET.write_text(content, encoding="utf-8")
