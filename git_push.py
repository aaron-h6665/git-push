class Italian_Brainrot:
    def __init__(self, name, image, image_url):
        self.name = name
        self.image = Image(image_url)

class Image:
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f"Image URL: {self.url}"