from keras import layers
from tensorflow import data as tf_data

image_size = (180, 180)
batch_size = 128

train_ds, val_ds = keras.utils.image_dataset_from_directory(
    "path/to/folder/containing/2/subfolders/Fractured/and/Nonfractured",
    validation_split=0.2,
    subset="both",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)
