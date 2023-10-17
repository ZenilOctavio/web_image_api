from WebImageCreator.image_creator import ImageCreator

image_creator = ImageCreator()

content = image_creator.use_component('first_component', {'logs': [{ "name": 'SP&500', "open": 500, "close": 600, "change": 20.5 }]})

with open('./photo.png','wb') as photo:
  photo.write(content.read())
  photo.close()