import os
from PIL import Image

directory = '../dataset/raw'
new_dir = 'extracted_tiffs'
files_list = []

for path, directories, files in os.walk(directory):
     for file in files:
            if file.endswith(".tif"):
                files_list.append(os.path.join(path, file))
                
for each_file in files_list:
    print(each_file)
    split_string = each_file.split('/')
    folder_name_for_each_tiff = split_string[-1].split('.')[0]
    new_dir_absolute = os.path.join(split_string[0], split_string[1], new_dir, split_string[3], split_string[4], folder_name_for_each_tiff)
    print("new_dir_absolute", new_dir_absolute)
    if not os.path.exists(new_dir_absolute):
        os.makedirs(new_dir_absolute)
        
    full_tiff_image = Image.open(each_file)
    for each_frame_i in range(full_tiff_image.n_frames):
        new_filename = os.path.join(new_dir_absolute, folder_name_for_each_tiff + '_%s.tif'%(each_frame_i,))
        # print(new_filename)
        try:
            full_tiff_image.seek(each_frame_i)
            if not os.path.exists(new_filename):
                full_tiff_image.save(new_filename)
        except:
            pass
