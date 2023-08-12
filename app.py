import openai
openai.api_key = "" #Enter your OPEN-AI key
from flask import Flask, render_template, request, jsonify
app = Flask(__name__,template_folder='Template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    caption = request.json['caption']

    # Call the model or image generation code here with the caption
    # Replace this with your own implementation
    image_url = generate_image_from_caption(caption)

    # Return the generated image URL as a JSON response
    return jsonify({'image_url': image_url})

def generate_image_from_caption(caption):
    # Implement your code to generate the image from the caption here
    # Return the image URL or file path
    response = openai.Image.create(
    prompt=caption,n=1,
    size="512x512")
    image_url = response['data'][0]['url']
    return image_url
app.run(debug=False, host="0.0.0.0", port=0, threaded=True)
