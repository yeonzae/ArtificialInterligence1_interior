from flask import Flask, render_template, request
import find_closest as pantone_find

app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the result page
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        # Process the form submission
        style = request.form.get('style')
        images, palettes, color_codes, pantone_codes = get_style_samples(style)
        return render_template('result.html', style=style, images=images, palettes=palettes, color_codes = color_codes, pantone_codes = pantone_codes )
    else:
        # Handle GET request for displaying the form
        return render_template('index.html')

# Define a helper function to retrieve style samples
def get_style_samples(style):
    # Implement the logic to retrieve style-specific samples and palettes
    # This function should return a list of image filenames and palette filenames
    # corresponding to the selected style
    if style == 'Asian':
        images = ['asian1.jpg', 'asian2.jpg', 'asian3.jpg', 'asian4.jpg', 'asian5.jpg', 'asian6.jpg']
        palettes = ['asian1_palette.png', 'asian2_palette.png', 'asian3_palette.png', 'asian4_palette.png', 'asian5_palette.png', 'asian6_palette.png']
        color_codes = [[(47, 29, 19), (166, 148, 133), (145, 128, 115), (45, 32, 20), (62, 39, 25), (97, 89, 86), (54, 37, 26), (15, 12, 10)],[(88, 64, 47), (139, 124, 122), (183, 162, 149), (156, 127, 112), (210, 179, 138), (206, 173, 130)],[(118, 107, 95), (135, 120, 97), (132, 119, 97), (91, 72, 49), (100, 82, 58)],[(90, 81, 67), (135, 106, 92), (82, 52, 50), (149, 135, 131), (113, 92, 89)],[(52, 41, 26), (58, 51, 44), (104, 89, 60), (130, 105, 78)],[(125, 112, 100), (196, 192, 189), (116, 109, 106), (196, 189, 183)]]
        pantone_codes = []
        for color_group in color_codes:
            pantone_group = []
            for color in color_group:
                r, g, b = color
                closest = pantone_find.closest_pantone(r, g, b)
                pantone_group.append(closest)
            pantone_codes.append(pantone_group)
    elif style == 'Coastal':
        images = ['coastal1.jpg', 'coastal2.jpg', 'coastal3.jpg', 'coastal4.jpg', 'coastal5.jpg', 'coastal6.jpg']
        palettes = ['coastal1_palette.png', 'coastal2_palette.png', 'coastal3_palette.png', 'coastal4_palette.png', 'coastal5_palette.png', 'coastal6_palette.png']
        color_codes = [[(190, 184, 178), (188, 177, 167), (173, 164, 154), (209, 205, 198)],[(184, 162, 142), (171, 175, 170), (197, 195, 182), (173, 169, 153)],[(216, 210, 204), (192, 186, 182), (211, 210, 205), (215, 212, 207)],[(156, 147, 153), (179, 184, 179), (164, 169, 173), (166, 165, 163)],[(188, 167, 135), (158, 148, 131), (176, 171, 163), (185, 185, 178), (199, 199, 191)],[(195, 177, 156), (141, 141, 142), (118, 118, 101), (204, 200, 197)]]
        pantone_codes = []
        for color_group in color_codes:
            pantone_group = []
            for color in color_group:
                r, g, b = color
                closest = pantone_find.closest_pantone(r, g, b)
                pantone_group.append(closest)
            pantone_codes.append(pantone_group)
    else:
        # Handle the case where an invalid style is selected
        images = []
        palettes = []
        color_codes = []
        pantone_codes = []

    return images, palettes, color_codes, pantone_codes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)
    # app.run(port = 5000, debug=True)