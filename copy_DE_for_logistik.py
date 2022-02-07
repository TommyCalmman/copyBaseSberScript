# 04.02.2022
#
import schedule    
import time
import os
import shutil
def job():
    # file_targetname - имя куда копировать
    file_targetname = f'C:\\Users\\afranchuk\\Desktop\\uHqX6WAEDDA\\uHqX6WAEDDA_logistik.jpg'
    # file_newname_newfile - имя для бэкапа
    file_newname_newfile = f'C:\\Users\\afranchuk\\Desktop\\uHqX6WAEDDA_logistik_{time.strftime("%Y%m%d", time.localtime())}.jpg'
    # имя настоящего файла (какой копируем)
    real_file = f'C:\\Users\\afranchuk\\Desktop\\uHqX6WAEDDA.jpg'

    os.rename(file_targetname, file_newname_newfile)   
    print(time.strftime("%Y%m%d", time.localtime()),"renamed")

    time.sleep(10)

    shutil.copyfile(real_file, file_targetname)
    print(time.strftime("%Y%m%d", time.localtime()),"copied")
    time.sleep(10)
   
schedule.every().day.at("20:01").do(job) 

while True:
    try:
        schedule.run_pending()
    except:
        print('Ошибка копирования...')
    time.sleep(1)