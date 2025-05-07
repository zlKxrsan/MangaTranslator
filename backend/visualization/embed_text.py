from PIL import Image, ImageDraw, ImageFont

# Bild laden
image = Image.open(".panels/coworker.png")
draw = ImageDraw.Draw(image)


def get_best_font_size(text, font_path, max_width, max_height):
    font_size = 10
    while True:
        font = ImageFont.truetype(font_path, size=font_size)
        wrapped = wrap_text(text, font, max_width)

        total_height = sum(
            font.getbbox(line)[3] - font.getbbox(line)[1] for line in wrapped
        )
        max_line_width = max(
            font.getbbox(line)[2] - font.getbbox(line)[0] for line in wrapped
        )

        if total_height > max_height or max_line_width > max_width:
            return font_size - 1  # vorherige Größe passt noch
        font_size += 1


# Funktion zum Berechnen des Textumbruchs und der Textplatzierung
def draw_bounding_boxes_and_text_with_pillow(image, draw, speech_bubbles_data):
    width, height = image.size
    for bubble in speech_bubbles_data:
        cluster = bubble[:-1]
        text = bubble[-1]

        x_min = int(min([p[0] for p in cluster]))
        x_max = int(max([p[0] for p in cluster]))
        y_min = int(min([p[1] for p in cluster]))
        y_max = int(max([p[1] for p in cluster]))

        # Versuche die Farbe eines Pixels direkt unterhalb der Box zu lesen
        sample_x = (x_min + x_max) // 2  # Mittlerer X-Wert
        sample_y = y_max + 1
        if 0 <= sample_x < width and 0 <= sample_y < height:
            background_color = image.getpixel((sample_x, sample_y))
        else:
            background_color = (0, 0, 0)  # Fallback: Schwarz

        # Box mit der ermittelten Farbe (leicht transparent, z.B. 160) füllen
        draw.rectangle([x_min, y_min, x_max, y_max], fill=(*background_color[:3], 160))

        # Bestimme passende Schriftgröße
        try:
            max_width = x_max - x_min - 10  # z.B. 5px Padding links und rechts
            max_height = y_max - y_min - 10  # z.B. 5px Padding oben und unten

            font_path = ".fonts/Bangers-Regular.ttf"
            best_size = get_best_font_size(text, font_path, max_width, max_height)
            font = ImageFont.truetype(font_path, size=best_size)
        except IOError:
            font = ImageFont.load_default()

        max_width = x_max - x_min - 10
        max_height = y_max - y_min - 10

        wrapped_text = wrap_text(text, font, max_width)
        text_height = sum(
            font.getbbox(line)[3] - font.getbbox(line)[1] for line in wrapped_text
        )
        y_offset = y_min + (max_height - text_height) // 2

        # Berechne Helligkeit (Luminanz) nach ITU-R BT.709-Standard
        r, g, b = background_color[:3]
        luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b

        # Bestimme Textfarbe je nach Helligkeit
        text_color = (0, 0, 0) if luminance > 160 else (255, 255, 255)

        for line in wrapped_text:
            text_width = font.getbbox(line)[2] - font.getbbox(line)[0]
            x_offset = x_min + (max_width - text_width) // 2
            draw.text((x_offset, y_offset), line, font=font, fill=text_color)
            y_offset += font.getbbox(line)[3] - font.getbbox(line)[1]

    return image


# Funktion zum Umbruch des Texts
def wrap_text(text, font, max_width):
    lines = []
    words = text.split()
    current_line = []

    for word in words:
        current_line.append(word)
        # Berechne die Breite des Texts mit getbbox
        width = (
            font.getbbox(" ".join(current_line))[2]
            - font.getbbox(" ".join(current_line))[0]
        )

        if width > max_width:
            lines.append(" ".join(current_line[:-1]))
            current_line = [word]

    if current_line:
        lines.append(" ".join(current_line))

    return lines


def embed_text_in_image(image_path, speech_bubbles_data):
    # Lade das Bild
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Zeichne die Bounding Boxen und Texte
    result_image = draw_bounding_boxes_and_text_with_pillow(
        image, draw, speech_bubbles_data
    )

    # Speichere das Ergebnis
    result_image.save(".output/coworkerPillow2.png")
