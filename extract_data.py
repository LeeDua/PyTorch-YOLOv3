import os
# import shutil

classes = ['bicycle', 'bus', 'car', 'dog', 'motorbike', 'person', 'train']

base = 'VOCdevkit/VOC2007/ImageSets/Main/'
hasTest = True
# base = 'VOCdevkit/VOC2012/ImageSets/Main/'

train_index = []
test_index = []


def get_index(dataset_path,l):
    with open(dataset_path,'r') as f:
        line = f.readline()
        # 判断文件是否结束
        while line:
            # 一行十个字符，最后一个字符是'\n'，因此检测倒数第三个字符即可
            if line[-3] != '-':
                index = line.split(' ')[0]
                # 如果该序列号不存在于列表，则添加
                if index not in l:
                    l.append(index)
            line = f.readline()
        f.close


def write_txt(person_index, label_path):
    # 所有的训练数据写入train
    with open(os.path.join(base, label_path),'w') as f:
        for index in person_index:
            line = index + '\n'
            f.write(line)
    f.close()
    print('    write labels into txt finished')


if __name__ == '__main__':

    for cls in classes:
        train = base + '/' +cls + '_trainval.txt'
        get_index(train, train_index)
        if hasTest:
            test = base + '/' + cls + '_test.txt'
            get_index(test, test_index)
    train_index.sort()
    test_index.sort()
    write_txt(train_index, 'train.txt')
    if hasTest:
        write_txt(test_index, 'test.txt')
