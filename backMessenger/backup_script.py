import subprocess
import datetime
import os


MAX_BACKUP_NUMBER = 5

# deletes the oldest file
def prepare_backup_dir():
    list_of_files = os.listdir('backups')
    full_path = ["backups/{0}".format(x) for x in list_of_files]

    if len([name for name in list_of_files]) >= MAX_BACKUP_NUMBER:
        oldest_file = min(full_path, key=os.path.getctime)
        print(oldest_file)
        os.remove(oldest_file)


def make_backup_file():
    subprocess.run('./manage.py dumpdata > backups/backup_{}'.format(
        datetime.datetime.now().strftime("%d_%m_%Y_%H:%M:%S")), shell=True)


if __name__ == "__main__":
    prepare_backup_dir()
    make_backup_file()
