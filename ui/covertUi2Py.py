import os
import os.path

# UI文件所在路径
dir = './'


# 列出目录下的所有UI文件
def list_ui_file():
    ui_files = []
    files = os.listdir(dir)
    for file in files:
        if os.path.isfile(dir + file) and file.endswith('.ui'):
            ui_files.append(file)
    return ui_files


# 把扩展名为.ui的文件改成扩展名为.py的文件
def trans_py_file(file):
    return os.path.splitext(file)[0] + '.py'


# 调用系统命令把UI文件转换成Python文件
def run_main():
    ui_files = list_ui_file()
    for ui_file in ui_files:
        py_file = trans_py_file(ui_file)
        cmd = 'pyuic5 -o {py_file} {ui_file}'.format(py_file=py_file, ui_file=ui_file)
        # print(cmd)
        os.system(cmd)


# 程序的主入口
if __name__ == '__main__':
    run_main()
