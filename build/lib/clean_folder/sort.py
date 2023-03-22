from pathlib import Path
import sys
import shutil
from .normalize import normalise


archives = 'archives'

EXTENSIONS = {
    'images': ['.jpeg', '.png', '.jpg', '.svg'],
    'video': ['.avi', '.mp4', '.mov', '.mkv'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'music': ['.mp3', '.ogg', '.wav', '.amr'],
    archives: ['.zip', '.gz', '.tar']
}

###################################

def move(file:Path, path:Path, category:str):

    if category == 'unknown':

        return file.replace(path.joinpath(file.name))

    path_to_k = path.joinpath(category)

    if not path_to_k.exists():

        path_to_k.mkdir()

        file_stem = normalise(file.stem)

    return file.replace(path_to_k.joinpath(f'{file_stem}{file.suffix}'))

###################################

###################################

def get_categories(file:Path):

    extension = file.suffix.lower()
     
    for k, v in EXTENSIONS.items():

        if extension in v:

            return k
    
    return 'unknown'

###################################

###################################

def sort(path:Path, current_dir:Path):

    for item in [f for f in current_dir.glob('*') if f.name not in EXTENSIONS.keys()]:

        if item.is_file():

            category = get_categories(item)

            new_path = move(item, path, category)
        
        else:

            sort(path, item)

            item.rmdir()

###################################

###################################

def unpack(path:Path, arc_name:Path, extension:str ):

    f_unpack = path / arc_name.stem

    f_unpack.mkdir

    shutil.unpack_archive(arc_name, f_unpack, extension)

###################################

###################################
def unpack_in(archive:Path, s_dict:dict):

    for arc in archive.glob('?*.*'):

        extension = arc.suffix


    
    if extension in s_dict[archive.name]:

        extension = extension.split('.')[1]

        unpack(archive, arc, extension)
  
###################################

###################################
def main():

    try:
        path = Path(sys.argv[1])

    except IndexError:

        return f'No path to folder. Take as parameter'
    
    if not path.exists():

        return 'Sorry, folder not exists'
    
    sort(path, path)
    

    archive = path / archives

    unpack_in(archive, EXTENSIONS )

###################################

###################################

if __name__ == '__main__':

   print( main())

###################################
