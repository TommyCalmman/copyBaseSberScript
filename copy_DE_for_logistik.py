# 04.02.2022
#
import schedule    
import time
import os
import shutil
def job():
    # file_targetname - имя+путь куда копировать
    file_targetname = f'C:\\test\testFile.jpg'
    # file_newname_newfile - имя для бэкапа
    file_newname_newfile = f'C:\\test\testFile_{time.strftime("%Y%m%d", time.localtime())}.jpg'
    # имя настоящего файла (какой копируем)
    real_file = f'C:\\testFile.jpg'

    os.rename(file_targetname, file_newname_newfile)   
    print(time.strftime("%Y%m%d", time.localtime()),"renamed")

    time.sleep(3)

    shutil.copyfile(real_file, file_targetname)
    print(time.strftime("%Y%m%d", time.localtime()),"copied")
    time.sleep(3)
   
schedule.every().day.at("02:10").do(job) 
print(f'Starting at {time.ctime()}')
while True:
    try:
        schedule.run_pending()
    except:
        print('Ошибка копирования...')
        time.sleep(30)
    time.sleep(1)
