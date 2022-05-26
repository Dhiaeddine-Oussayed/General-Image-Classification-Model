# General-Image-Classification-Model
A simple image classification model that works on different image datasets.

To use this model, you just import your data and run the "train.py" file. A directory named "claasification_model" will be created on your workspace containing the saved weights of your model.
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
N.B: Your labels will have the same name as your sub-folders name as the sub-folders are the classes.
