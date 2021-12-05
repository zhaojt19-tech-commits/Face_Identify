import cv2
import numpy as np

# 指定存放图片的路径
path_train = 'C:\Project\Python Project\Face_Identify\Pictures\pictures_train'
path_test = 'C:\Project\Python Project\Face_Identify\Pictures\pictures_test'

if __name__ == '__main__':
    # 读取像素数据
    data_train = np.loadtxt('C:/Project/Python Project/Face_Identify/dataset/train_data.csv')
    data_test = np.loadtxt('C:/Project/Python Project/Face_Identify/dataset/test_data.csv')

    # 按行取数据(训练集)
    for i in range(data_train.shape[0]):
        face_array = data_train[i, :].reshape((48, 48)) # reshape
        cv2.imwrite(path_train + '//' + '{}.jpg'.format(i), face_array) # 写图片

    # 按行取数据(测试集)
    for i in range(data_test.shape[0]):
        face_array = data_test[i, :].reshape((48, 48))  # reshape
        cv2.imwrite(path_test + '//' + '{}.jpg'.format(i), face_array)  # 写图片