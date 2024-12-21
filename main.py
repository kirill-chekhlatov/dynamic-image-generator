from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

class CreateImage:
    """
    A class for creating an image with dynamically resized height 
    to fit a given text. The text is automatically wrapped to fit 
    within the specified width of the image.

    Usage:
    - Specify the text, font, font size, and output image path, along with optional 
      parameters such as initial image dimensions and margins.
    - Call the `main()` method to generate an image with the given text.
    """

    def __init__(self, text: str, font_path: str, font_size: int, output_image_path: str, margin: int = 10, initial_width: int = 800, initial_height: int = 600):
        """
        Initializes image and text parameters.

        Args:
            text (str): The text to display on the image.
            font_path (str): Path to the font file (.ttf).
            font_size (int): Font size for the text.
            output_image_path (str): File path where the resulting image will be saved.
            margin (int): Margin around the text in pixels.
            initial_width (int): Initial width of the image in pixels.
            initial_height (int): Initial height of the image in pixels.
        """
        self.text = text
        self.font_path = font_path
        self.font_size = font_size
        self.output_image_path = output_image_path
        self.margin = margin
        self.initial_width = initial_width
        self.initial_height = initial_height
        self.line_spacing = 5  # Spacing between lines in pixels
        self.default_y_position = 10  # Initial y-coordinate for text placement

        self.validate_font_path()
        self.font = ImageFont.truetype(font=self.font_path, size=self.font_size)

    def validate_font_path(self):
        """Checks if the provided font file exists. Raises an error if not."""
        if not os.path.exists(self.font_path):
            raise FileNotFoundError(f"Font file '{self.font_path}' not found.")

    def create_base_image(self) -> tuple[Image.Image, ImageDraw.ImageDraw]:
        """
        Creates a blank image with a white background.

        Returns:
            tuple: A tuple containing the Image object and the associated ImageDraw object.
        """
        image = Image.new('RGB', (self.initial_width, self.initial_height), color='white')
        draw = ImageDraw.Draw(image)
        return image, draw

    def calculate_max_chars_per_line(self) -> int:
        """
        Calculates the maximum number of characters that can fit in a single line 
        based on the font size and image width.

        Returns:
            int: Maximum number of characters that can fit in one line.
        """
        test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        total_width = self.font.getbbox(test_string)[2]
        avg_char_width = total_width / len(test_string)
        return int((self.initial_width - 2 * self.margin) / avg_char_width)

    def wrap_text(self, max_chars_per_line: int) -> list[str]:
        """
        Wraps the text into lines that fit within the allowed width.

        Args:
            max_chars_per_line (int): Maximum number of characters per line.

        Returns:
            list[str]: A list of strings representing the wrapped text.
        """
        lines = self.text.split('\n')
        wrapped_lines = []
        for line in lines:
            wrapped_lines.extend(textwrap.wrap(line, width=max_chars_per_line) if line else [''])
        return wrapped_lines

    def calculate_total_height(self, wrapped_lines: list[str]) -> int:
        """
        Calculates the total height required to fit the wrapped text.

        Args:
            wrapped_lines (list[str]): A list of text lines to fit into the image.

        Returns:
            int: Total height required for the image in pixels.
        """
        return self.default_y_position + len(wrapped_lines) * (self.font_size + self.line_spacing)

    def adjust_image_size(self, image: Image.Image, required_height: int) -> Image.Image:
        """
        Adjusts the image height if the required height exceeds the initial height.

        Args:
            image (Image.Image): The original image object.
            required_height (int): The height required to fit all text.

        Returns:
            Image.Image: The resized image object.
        """
        if required_height > self.initial_height:
            return image.resize((self.initial_width, required_height))
        return image

    def draw_text(self, draw: ImageDraw.ImageDraw, wrapped_lines: list[str]):
        """
        Draws the wrapped text onto the image.

        Args:
            draw (ImageDraw.ImageDraw): The ImageDraw object for the image.
            wrapped_lines (list[str]): The wrapped text lines to draw.
        """
        y_position = self.default_y_position
        for line in wrapped_lines:
            draw.text((self.margin, y_position), line, font=self.font, fill='black')
            y_position += self.font_size + self.line_spacing

    def save_image(self, image: Image.Image):
        """
        Saves the final image to the specified output path.

        Args:
            image (Image.Image): The final image object.
        """
        image.save(self.output_image_path)

    def main(self):
        """
        The main method to generate and save the image with the text.
        It creates a base image, wraps the text, adjusts the image size if needed, 
        draws the text, and saves the final result.
        """
        image, draw = self.create_base_image()
        max_chars_per_line = self.calculate_max_chars_per_line()
        wrapped_lines = self.wrap_text(max_chars_per_line)
        total_height = self.calculate_total_height(wrapped_lines)
        image = self.adjust_image_size(image, total_height)
        draw = ImageDraw.Draw(image)  # Recreate draw object if image was resized
        self.draw_text(draw, wrapped_lines)
        self.save_image(image)

if __name__ == '__main__':
    """
    Infinite loop for generating images with user-provided text.
    """
    font_path = 'arial.ttf'  # Path to your font file
    font_size = 20           # Font size
    output_image_base = 'output_image'  # Base name for output images

    print("📸 Dynamic Text Image Generator")
    print("Type 'exit' to stop the program.\n")

    image_counter = 1  # Counter for image filenames

    while True:
        # Wait for user input
        text = input("📝 Enter your text (or type 'exit' to quit): ").strip()
        
        if text.lower() == 'exit':
            print("👋 Exiting the program. Goodbye!")
            break
        
        if not text:
            print("⚠️ Text cannot be empty. Please try again.")
            continue
        
        # Generate unique image name
        output_image_path = f"{output_image_base}_{image_counter}.jpg"
        
        try:
            # Create an image with the provided text
            CreateImage(
                text=text,
                font_path=font_path,
                font_size=font_size,
                output_image_path=output_image_path,
            ).main()
            
            print(f"✅ Image saved as '{output_image_path}'")
            image_counter += 1  # Increment the image counter
            
        except FileNotFoundError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")

