from PIL import Image, ImageDraw
import random

# Function to generate an abstract image
def generate_abstract_image(user_handle):
    width, height = 512, 512
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    for _ in range(150):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        color = tuple(random.randint(0, 255) for _ in range(3))
        shape_type = random.choice(['ellipse', 'rectangle', 'line'])

        if shape_type == 'ellipse':
            draw.ellipse([x1, y1, x2, y2], fill=color, outline=color)
        elif shape_type == 'rectangle':
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=color)
        elif shape_type == 'line':
            draw.line([x1, y1, x2, y2], fill=color, width=3)

    # Add a subtle text overlay with the user handle
    text_position = (20, height - 50)
    text_color = (50, 50, 50, 128)  # Subtle semi-transparent gray
    draw.text(text_position, f"@{user_handle}", fill=text_color)

    # Save the image
    image_path = f"{user_handle}_abstract.png"
    image.save(image_path)
    return image_path
