from PIL import Image, ImageDraw, ImageFont
import textwrap

strings = [    "10 Simple Tips for Incorporating Mindfulness into Your Daily Life",    "The Benefits of Mindfulness for Stress Reduction and Improved Mental Health",    "Mindfulness for Beginners A Step by Step Guide",    "Mindful Eating How to Practice Mindfulness at Meal Times",    "The Role of Mindfulness in Achieving Work Life Balance",    "Mindfulness for Kids Teaching Children the Art of Being Present",    "Mindfulness and Creativity How to Boost Your Creative Process",    "The Science Behind Mindfulness How It Affects the Brain",    "Mindfulness and Sleep How to Improve Your Sleep Quality with Mindfulness Practices",    "Mindfulness and Self Compassion Keys to Building a Stronger, More Resilient Self",    "Mindfulness and Relationships How to Strengthen Your Connections with Others",    "Mindfulness and Emotional Intelligence Developing Your Emotional Intelligence through Mindfulness Practices",    "Mindfulness for Athletes How to Enhance Your Performance and Well Being",    "Mindfulness and the Workplace How to Implement Mindfulness in the Office",    "Mindfulness and Travel How to Practice Mindfulness on the Go",    "Mindfulness and Parenting Raising Mindful Children in a Fast Paced World",    "Mindfulness and Mental Health How to Use Mindfulness to Overcome Anxiety, Depression, and Other Mental Health Challenges",    "Mindfulness and Aging How to Age Gracefully and Mindfully",    "Mindfulness and Social Media How to Use Social Media Mindfully and Avoid Burnout",    "Mindfulness and the Environment How to Practice Mindfulness and Care for the Earth"]

for text in strings:
    # Create an image with a white background
    try:
        image = Image.new('RGB', (800, 400), 'white')

        # Set the font and create a drawing context
        font = ImageFont.truetype('LeagueSpartan-Regular.ttf', 32)
        draw = ImageDraw.Draw(image)

        # Set the text and wrap it to fit within the image
        wrapped_text = textwrap.wrap(text, width=50)

        # Split the wrapped text into two separate strings
        half = len(wrapped_text) // 2
        black_text = wrapped_text[:half]
        red_text = wrapped_text[half:]


        # Calculate the x and y coordinates to center the text
        x = (image.width - font.getsize(black_text[0])[0]) / 2
        y = (image.height - font.getsize(black_text[0])[1]) / 2

        # Add some extra padding around the text
        padding = 10
        x += padding
        y += padding

            
        # Draw the text, half in black and half in red
        for line in black_text:
            draw.text((x, y), line, font=font, fill='black')
            y += font.getsize(line)[1]
        for line in red_text:
            draw.text((x, y), line, font=font, fill='#ff5757')
            y += font.getsize(line)[1]

        # Set the font for the footer text
        footer_font = ImageFont.truetype('LeagueSpartan-Regular.ttf', 22)

        # Set the footer text
        footer_text = "SimplifyMindfulness.com"

        # Calculate the x and y coordinates for the footer
        footer_x = image.width - footer_font.getsize(footer_text)[0] - 10
        footer_y = image.height - footer_font.getsize(footer_text)[1] - 10

        # Add some padding around the footer text
        footer_padding = 14
        footer_x += footer_padding
        footer_y += footer_padding

        # Draw the footer text in the bottom-right corner of the image
        draw.text((footer_x, footer_y), footer_text, font=footer_font, fill='black')

        # Save the image
        image.save(f'Images/{text}'+'.png')
    except Exception as e:
        print(e)
    else:
        pass
    finally:
        pass