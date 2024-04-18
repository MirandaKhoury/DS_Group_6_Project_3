#### make test train split WITH REBALANCING (undersampling) ####

### first make a df containing all jpeg file names and their classes ###
import os
import numpy as np

Frac_Atlas_path = "C://Users/mrkho/OneDrive/Documents/4th year/DS-4002/" # change to the directory where FracAtlas is

frac = pd.DataFrame(os.listdir(Frac_Atlas_path + "FracAtlas/images/Fractured"))
frac_name = pd.DataFrame(np.repeat("Fractured", 717))
frac_df = pd.concat([frac, frac_name], axis=1, ignore_index=True)

nonfrac = pd.DataFrame(os.listdir(Frac_Atlas_path + "FracAtlas/images/Non_fractured"))
nonfrac_name = pd.DataFrame(np.repeat("Non-fractured", 3366))
nonfrac_df = pd.concat([nonfrac, nonfrac_name], axis=1, ignore_index=True)

# randomly undersample the nonfrac data
import random
index_list = random.sample(range(0, 3365), 717) # get 717 random indices
nonfrac_df2 = nonfrac_df.iloc[index_list,:] # get just those rows from the nonfrac data

df = pd.concat([frac_df, nonfrac_df2], axis = 0 , ignore_index=True)

### split into X and y ###
X = df[0]
y = df[1]

### run test_train_split on X and y ###
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.30, shuffle=True,random_state = 0)

### use lists of jpegs to sort all images into appropriate folders ###

## first set up directories:
# in FracAtlas, make a new directory called "Split", then make 2 directories inside "Split" named "test" and "train"
# Within the "Test" and "Train" directories, make 2 folders named "Fractured" and "Non-fractured" as well
# Now copy all images from both "Fractured" and "Non-fractured" in "images" to "Split"

## now get a list of all the file names...
Split_path = Frac_Atlas_path + "FracAtlas/Split"
from os import listdir
from os.path import isfile, join
file_list = [f for f in listdir(Split_path) if isfile(join(Split_path, f))] # get JUST files, not the Test/Train directories

## and check if they're in X_train or not
for file in file_list:
    if X_train[0].str.contains(file).any():
        os.rename(Split_path+"/"+file, Split_path+"/train/"+file)
    else:
        os.rename(Split_path+"/"+file, Split_path+"/test/"+file)
    # move to train if they are or test if they aren't

## now split test and train further into fractured and non-fractured categories

# for Test:
Test_file_list = [f for f in listdir(Split_path+"/test") if isfile(join(Split_path+"/test", f))]
# if file in test appears in the frac list,
for file in Test_file_list:
    if frac[0].str.contains(file).any():
        # put in Frac folder
        os.rename(Split_path+"/test/"+file, Split_path+"/test/Fractured/"+file)
    else:
        # put in Nonfrac folder
        os.rename(Split_path+"/test/"+file, Split_path+"/test/Non-fractured/"+file)

# for Train:
Train_file_list = [f for f in listdir(Split_path+"/train") if isfile(join(Split_path+"/train", f))]
# if file in test appears in the frac list,
for file in Train_file_list:
    if frac[0].str.contains(file).any():
        # put in Frac folder
        os.rename(Split_path+"/train/"+file, Split_path+"/train/Fractured/"+file)
    else:
        # put in Nonfrac folder
        os.rename(Split_path+"/train/"+file, Split_path+"/train/Non-fractured/"+file)
