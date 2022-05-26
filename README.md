# General-Image-Classification-Model
A simple image classification model that works on different image datasets.

To use this model, you just import your data and run the "train.py" file. A directory named "claasification_model" will be created on your workspace containing the saved weights of your model. All along with the label encoder fitted on your classes to use it later on predictions.
To run the "train.py" file without having any errors you need to arrange your data as follow:


               MAIN_DIRECTORY
              ├── 1st class
              │   ├── image 1
              │   ├── image 2
              │   ├── ...
              │   └── last image
              ├── 2nd class
              │   ├── image 1
              │   ├── ...
              │   └── image feature
              │
              ├── ...
              │
              │
              └── last class
                  ├── image 1
                  ├── ...
                  └── last image
                  
With :
  - "MAIN_DIRECTORY" is a folder having all your sub-folders.
  - "1st class, 2nd class... last class" are the sub-folders containing the images you intend to classify.

P.N: Your labels will have the same name as your sub-folders name as the sub-folders are the classes.

When training is done you will have a link to check the tensorboard callbacks and the evaluation accuracy of your model.
The "predict.py" file contains a pre-built function that you can use to test your model.
the function takes as arguments:
 - The image path for prediction
 - The model that you would use. You need to load your saved model using tensorflow.keras.models.load_model("path to your model")
 - The label encoder fitted on your training data. Try importing the encoder file using pickle.load(open("path to your encoder", "rb"))


P.N: You can customize the "train.py" file as you see fit. You can change the the size of the images, dimension, the number of convolutional layers and their filters, the structure of the fully connected neural network...
