import os
# import shutil

classes = ["bicycle", "motorbike", "bus", "car", "dog", "person", "train"]
main_path =     'VOCdevkit/VOC2007/ImageSets/Main/'
train_set = set()
test_set = set()

'''
def rm_unnecessary_files():
    # 删除无用的文件夹 
    for file in FOLDER_TO_DELETE:
        if os.path.exists(file):
            shutil.rmtree(file)
    # 清空无用和过期的label文件
    for file in os.listdir(main_path):
        if 'person' not in file:
            os.remove(os.path.join(VOC2007_label, file))
    print('[0] remove unnecessary files done')
'''

def get_index(dataset_path):
    person_index = []
    with open(dataset_path,'r') as f:
        line = f.readline()
        while line:
            if line[-3] != '-':
                index = line.split(' ')[0]
                if index not in person_index:
                    person_index.append(index)
            line = f.readline()
        f.close
    print('[1] extract pics: %d'%(len(person_index)))
    return person_index


def write_txt(person_index, label_path):
    # 所有的训练数据写入train
    with open(os.path.join(main_path, label_path),'w') as f:
        for index in person_index:
            line = index + '\n'
            f.write(line)
    f.close
    print('    write labels into txt finished')


if __name__ == '__main__':
    for cls in classes:
        trainval = main_path + cls + '_trainval.txt'
        test = main_path + cls + '_test.txt'
        print("train test file name", trainval, test)
        train_index = get_index(trainval)
        test_index = get_index(test)
        train_set.update(train_index)
        test_set.update(test_index)

    train_index = list(train_set)
    test_index = list(test_set)
    train_index.sort()
    test_index.sort()
    write_txt(train_index, 'train.txt')
    write_txt(test_index, 'test.txt')
