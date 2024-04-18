This is the repository for the third project of UVA DS 4002 project group 6: Miranda Khoury, Georgia Davidson, and Brian Bippert. This project involves developing a supervised neural network to classify X-ray images as showing or not showing bone fracture(s).


## Section 1: Software and platform

Software used: We used the coding language R and IDE software RStudio OR the coding language python and the IDE software VS Code to divide our images (we have 2 alternate scripts for making test/train splits that others can use), as well as the coding language Python and IDE PyCharm/VS Code to classify the images and to create a test and train model. 

Add-on packages installed with software:

Python libraries
-keras
-os
-Numpy 
-tensorflow
-Pillow
-pandas

No R packages used

Platform: We used the platform Windows for our project.


## Section 2: Map of documentation
 
Data folder: 

-Data Appendix.pdf 
-Data_explanation.pdf

Output folder:

-model_all vs. model_fractured
-model_all.keras
-model_all_balanced.keras
-model_fractured.keras
-model_hand.keras
-model_hip.keras
-model_leg.keras
-model_mixed.keras
-model_shoulder.keras
-model_stats.csv


Scripts folder:

-all_image.py
-image_classification.py
-image_divide.Rmd
-image_divide_WITH_REBALANCING.py


## Section 3: Instructions for reproducing results

To replicate our results, first obtain the dataset by accessing the site (https://figshare.com/articles/dataset/The_dataset/22363012). Scroll down and click the download button, and unzip the file to obtain access to the data. 

If not already installed, install R and RStudio, as well as Python and either the PyCharm or VS Code IDE. You can download R by selecting one of the mirrors from this site (https://cran.r-project.org/mirrors.html) and selecting “Download R for [your operating system]”. You can download RStudio from this site (https://posit.co/download/rstudio-desktop/). You can download Python from this tutorial (https://www.digitalocean.com/community/tutorials/install-python-windows-10) and PyCharm through this site (https://www.jetbrains.com/pycharm/download/?section=windows).

Download all script files from the Scripts folder, and then in the images subfolder of the unzipped FracAtlas folder, create two more folders, named ‘test’ and ‘train’. In each of these folders, create two more folders named ‘Fractured’ and ‘Not Fractured’. Then open RStudio, set the directory that contains the FracAtlas folder to be the current working directory, and then run image_divide.Rmd. This will populate the two folders with images.

Alternatively, if you want to rebalance the dataset, after making the various folders, open VS Code and run image_divide_WITH_REBALANCING.py. You’ll have to set the Frac_Atlas_path variable at the top of the file to point to wherever you downloaded FracAtlas. This will populate the two folders with images while also balancing the dataset so there are an equal number of fractured and non-fractured data points.

Once your dataset has been split into test/train cohorts using one of the two methods above, open up a python interpreter and run image_classification.py. Various lines include brackets that indicate what should go in that place to gather the correct results. This includes providing the file path to the ‘test’ and ‘train’ folders previously created, as well as how many images are in each folder and the name of the output file. Running this code should output various metrics on the loss and accuracy of the model that is being trained. Then the all_image.py script can be run, which takes in a model, which is once again indicated by brackets and a short description of what goes there, and outputs the average score of the model where 0 indicates a fracture and 1 indicates no fracture. This script also needs an input on the last line to correctly compute the average. In order to generate different models, lines 29 and 30 of image_divide.Rmd can be changed as specified in that file. Then running the image_classification.py script will create the new models from the freshly divided data. At this point, all models and values obtained from our research will be found.


