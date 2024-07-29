# Jupyter2Prod
A full helping of creating a machine learning/deep learning model in a jupyter notebook, testing it, and then deploying it into a prod environment.

The project is going to be a clothing recommendation app. Ideally, it will allow you to upload an image of an article of clothing and then provide the top recommended items that are "closest" to that particular item. Eventually, we would want to add metadata, but for now, I'm ok if you can upload a photo and get recommendations of the same type of clothing.

# Roadmap

1.) Get an API up and going: This will involve simply creating an API that works. We want to make get and post requests for something.
2.) Create a basic functionality: What will our API do? Initially, we'll simply make a clothes classifier app
3.) Train a model to classify clothes: this will take care of step 2.
4.) Train an image embedding model to compare clothes
5.) Setup a vector database to store clothing embedding data. We'll stick with Wevaiate because I know it
6.) Make a web scraper to get more data. We're starting with ~5,000 images of the clothes. Not nearly enough for us. We'll try to set up a webscraper to download images to our own custom data store.
7.) Large scale training of an embedding model: make a huge pretraining effort and see if we can get some good "gains".
8.) Make minimal website for this app. Allow people to upload image and then have relevent clothing back
9.) Create a personalize recommendation system for clothes. See if we can get some "users" and go from there.
