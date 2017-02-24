# filename py
# coding:utf-8
import os
import os.path

rootdir = r'C:\Users\yinte\Desktop\gif'  # 指明被遍历的文件夹


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        print child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题

        newName = filename.replace(oldId, newId)
        print(filename, "---->", newName)
        os.rename(os.path.join(parent, filename), os.path.join(parent, newName))




if __name__ == "__main__":
    print("main")
    filePath = "D:\fdsf"
    i = 1
    # eachFile(filePath)
    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dirnames, filenames in os.walk(rootdir):
        for dirname in dirnames:  # 输出文件夹信息
            print "parent is: " + parent
            print "dirname is: " + dirname

        for filename in filenames:  # 输出文件信息
            print "filename is: " + filename
            newName = "today_gift_" + str(i) + ".png"
            i = i + 1
            print "new : " + newName
            os.rename(os.path.join(parent, filename), os.path.join(parent, newName))
