import os
import shutil
import datetime
import schedule
import time

source_dir = 'C://Users//flavi//Desktop//Backup'
destination_dir = 'G://Meu Drive'

do_it = False


def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f'Folder {source} copied to {dest_dir}')
    except FileExistsError:
        print(f'Folder {source} already exists in {dest_dir}')

if not do_it:
    schedule.every().day.at("17:35").do(lambda: copy_folder_to_directory(source_dir, destination_dir))
    while True:
        schedule.run_pending()
        time.sleep(60)
else:
    copy_folder_to_directory(source_dir, destination_dir)
