from pixabay import Image, Video

API_KEY = '11260031-f9096042a465b94c202846550'
image = Image(API_KEY)

# custom image search
ims = image.search(q='cats dogs',
             lang='es',)
