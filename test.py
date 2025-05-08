import os

# 1. Hole die erste Bilddatei aus dem Ordner ".panels"
panel_dir = ".panels"
output_dir = ".output"

# Unterstützte Bildtypen (kannst du erweitern)
image_extensions = (".png", ".jpg", ".jpeg", "webp")

# Finde alle Bilddateien im Ordner
panel_files = [f for f in os.listdir(panel_dir) if f.lower().endswith(image_extensions)]

# Falls keine Bilddateien vorhanden sind
if not panel_files:
    raise FileNotFoundError("Keine Bilddateien im Ordner .panels gefunden.")

# Nimm die erste Bilddatei
first_image = panel_files[0]

# Pfade definieren
img_path = os.path.join(panel_dir, first_image)

# Trenne Namen und Erweiterung
name, ext = os.path.splitext(first_image)
output_path = os.path.join(output_dir, f"{name}_translated{ext}")
