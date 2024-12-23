from talon import Module, actions, skia, ui
from talon.experimental import locate

mod = Module()


def find_pixel_pattern(colors: list[int]):
    # Create a 2x2 image with the specified colors
    width = 2
    height = 8
    pixels = []

    # Fill the pixels array with colors
    for color in colors:
        # RGB format (no alpha)
        red = (color >> 16) & 0xFF
        green = (color >> 8) & 0xFF
        blue = color & 0xFF
        pixels.extend([red, green, blue, 255])  # Force full opacity

    print(pixels)

    # Convert to bytes
    pixels = bytes(pixels)

    # Create image from pixels
    stride = width * 4  # 4 bytes per pixel
    img = skia.Image.from_pixels(
        pixels,
        stride,
        width,
        height,
        skia.Image.ColorType.RGBA_8888,
        skia.Image.AlphaType.OPAQUE,  # Using OPAQUE since we're forcing full opacity
    )

    img.write_file("/Users/david/Desktop/pattern.png")

    print(img)
    rect = ui.active_window().rect
    print(rect)

    # Add a small delay to ensure pattern is rendered
    actions.sleep("50ms")

    # Find this pattern on screen with a slightly lower threshold
    matches = locate.locate(img, rect=rect, threshold=0.75)  # Reduced from 0.80

    # If no match found, try one more time after a longer delay
    if not matches:
        actions.sleep("100ms")
        matches = locate.locate(img, rect=rect, threshold=0.75)

    return matches


@mod.action_class
class Actions:
    def locate_pattern():
        """Find a pixel pattern on the screen"""
        colors = [
            0xFF0000,  # Pure Red
            0x00FF00,  # Pure Green
            0x0000FF,  # Pure Blue
            0xFFFF00,  # Yellow
            0xFF0000,  # Pure Red
            0x00FF00,  # Pure Green
            0x0000FF,  # Pure Blue
            0xFFFF00,  # Yellow
            # ... repeat pattern 3 more times to maintain the same length
            0xFF0000,
            0x00FF00,
            0x0000FF,
            0xFFFF00,
            0xFF0000,
            0x00FF00,
            0x0000FF,
            0xFFFF00,
            0xFF0000,
            0x00FF00,
            0x0000FF,
            0xFFFF00,
            0xFF0000,
            0x00FF00,
            0x0000FF,
            0xFFFF00,
            0xFF0000,
            0x00FF00,
            0x0000FF,
            0xFFFF00,
            0xFF0000,
            0x00FF00,
            0x0000FF,
            0xFFFF00,
            0xFF0000,
            0x00FF00,
            0x0000FF,
            0xFFFF00,
            0xFF0000,
            0x00FF00,
            0x0000FF,
            0xFFFF00,
        ]
        matches = find_pixel_pattern(colors)
        print("matches", matches)
        if matches:
            print(f"Found pattern at: {matches[0]}")
            return matches[0]
            # actions.mouse_move(matches[0].x, matches[0].y)
