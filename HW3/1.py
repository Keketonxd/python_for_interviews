from glob import glob


def get_file_name(file):
    print(file.split('.')[0])
    all_files = glob(f'C:/**/**/**/**/{file}', recursive=True)
    print(all_files)


get_file_name('1.py')
