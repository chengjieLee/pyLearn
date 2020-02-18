import os

print(os.name)
now_path = os.path.abspath('.') # 查看当前文件的绝对路径
test_path = os.path.join(now_path, 'testdir')
os.rmdir(test_path)