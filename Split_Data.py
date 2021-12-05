import csv
import os
import pandas as pd

# .csv在本地的绝对地址
path0 = 'C:\Project\Python Project\Face_Identify\表情识别.csv'
path1 = 'C:\Project\Python Project\Face_Identify\label.csv'
path2 = 'C:\Project\Python Project\Face_Identify\data.csv'

def split_csv_label(path, total_len, train_len):
    with open(path, 'r', newline='') as file:
        csvreader = csv.reader(file)
        i = 0
        for row in csvreader:
            if i < train_len:
                # train.csv存放路径
                csv_path = os.path.join("C:\Project\Python Project\Face_Identify\dataset", 'train_label.csv')

                with open(csv_path, 'a', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
            elif (i >= train_len) and (i < total_len):
                # vali.csv存放路径
                csv_path = os.path.join("C:\Project\Python Project\Face_Identify\dataset", 'test_label.csv')

                # 存在的时候就往里面添加
                with open(csv_path, 'a', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
            else:
                break

    print("训练集和验证集分离成功")
    return


def split_csv_data(path, total_len, train_len):
    with open(path, 'r', newline='') as file:
        csvreader = csv.reader(file)
        i = 0
        for row in csvreader:
            if i < train_len:
                # train.csv存放路径
                csv_path = os.path.join("C:\Project\Python Project\Face_Identify\dataset", 'train_data.csv')

                with open(csv_path, 'a', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
            elif (i >= train_len) and (i < total_len):
                # vali.csv存放路径
                csv_path = os.path.join("C:\Project\Python Project\Face_Identify\dataset", 'test_data.csv')

                # 存在的时候就往里面添加
                with open(csv_path, 'a', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
            else:
                break

    print("训练集和验证集分离成功")
    return


if __name__ == '__main__':
    # 读取数据
    df = pd.read_csv(path0)

    # 提取label数据
    df_y = df[['emotion']]

    # 提取feature（即像素）数据
    df_x = df[['pixels']]

    # 将label写入label.csv
    df_y.to_csv('label.csv', index=False, header=False)

    # 将feature数据写入data.csv
    df_x.to_csv('data.csv', index=False, header=False)

    #将标签进一步划分为训练和测试两部分
    total_len = len(open(path1, 'r').readlines())# csv文件行数
    train_len = 28709
    split_csv_label(path1, total_len, train_len)

    #将数据进一步划分为训练和测试两部分
    total_len = len(open(path2, 'r').readlines())# csv文件行数
    train_len = 28709
    split_csv_data(path2, total_len, train_len)