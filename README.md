This template is a simple template of data preprocessing processes commonly used in machine learning algorithms.

You need to edit the parameters and indexes in the code according to your own dataset.

I left a small piece of code about the dataframe slice in the template. We usually use this process to combine the remaining columns after removing them from the middle of the data set when our dependent variable is not in the last column.

It is related to how much you will divide the test_size parameter in the splitting section for your training and testing. You can change it according to your data set or you can perform training with all your data and test with unique values without dividing it as a train, test. (Pay attention to the overfitting situation.)