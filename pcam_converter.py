# %%
import numpy as np
from keras.utils import HDF5Matrix
import imageio

# set data paths
train_img_path = "/Users/IrmavandenBrandt/Downloads/Internship/PCam/camelyonpatch_level_2_split_train_x.h5"
train_label_path = "/Users/IrmavandenBrandt/Downloads/Internship/PCam/camelyonpatch_level_2_split_train_y.h5"
val_img_path = "/Users/IrmavandenBrandt/Downloads/Internship/PCam/camelyonpatch_level_2_split_valid_x.h5"
val_label_path = "/Users/IrmavandenBrandt/Downloads/Internship/PCam/camelyonpatch_level_2_split_valid_y.h5"
test_img_path = "/Users/IrmavandenBrandt/Downloads/Internship/PCam/camelyonpatch_level_2_split_test_x.h5"
test_label_path = "/Users/IrmavandenBrandt/Downloads/Internship/PCam/camelyonpatch_level_2_split_test_y.h5"

# load data into hdf5 type and convert the data values to numpy arrays
x_train = np.asarray(HDF5Matrix(train_img_path, 'x').data)
y_train = np.asarray(HDF5Matrix(train_label_path, 'y').data)
x_val = np.asarray(HDF5Matrix(val_img_path, 'x').data)
y_val = np.asarray(HDF5Matrix(val_label_path, 'y').data)
x_test = np.asarray(HDF5Matrix(test_img_path, 'x').data)
y_test = np.asarray(HDF5Matrix(test_label_path, 'y').data)


def unzip_labels(y):
    """
    :param y: array with labels in lists
    :return: array with labels in one list
    """
    tmp = []
    y = np.array(y)
    for i in range(0, len(y)):
        tmp.append(int(y[i]))
    y = np.array(tmp)

    return y


# remove the unnecessary lists around the labels
y_train = unzip_labels(y_train)
y_val = unzip_labels(y_val)
y_test = unzip_labels(y_test)

# combine all data to prepare for nfolds-cross-validation
x_all = np.concatenate((x_train, x_val, x_test), axis=0)
y_all = np.concatenate((y_train, y_val, y_test), axis=0)

# save images as png locally
for index in range(len(y_all)):
    imageio.imwrite(f'/Users/IrmavandenBrandt/Downloads/Internship/PCam/png_images/{index}_label={y_all[index]}.png',
                    x_all[index])
