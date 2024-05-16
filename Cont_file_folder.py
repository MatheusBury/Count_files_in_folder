import os
import pandas as pd

"""
version 0
@Author:Jennifer Oliveira Creator:09/05/24

"""

root=r'G:\Drives compartilhados\Modec\MV30\fotos_embarque_2024\imagens_360_convertidas_para_scan_points\imagens_360_convertidas_resolução original compressed'
list_root=os.listdir(root)


quantidades_folders = {'fpso area':[],'folders': [], 'quantidade': []}


for i,folder in enumerate(list_root):
    
    folders_fpso_area=os.path.join(root, folder)

    
    list_folder_fpso_area=os.listdir(folders_fpso_area)


    
    for i, folder_module in enumerate(list_folder_fpso_area):
         
        
        folders_modules = os.path.join(folders_fpso_area,folder_module)
        folders_modules = os.listdir(folders_modules)
        
        num_files = len(folders_modules)
        quantidades_folders['fpso area'].append(folder)
        quantidades_folders['folders'].append(folder_module)
        quantidades_folders['quantidade'].append(num_files)
    
        
print(quantidades_folders)


df=pd.DataFrame(quantidades_folders)
df.to_excel('quantidade de fotos por pasta.xlsx', index=False)
   






















folder = r'G:\Drives compartilhados\Modec\MV30\fotos_embarque_2024\imagens_360_convertidas_para_scan_points'
list_folder = os.listdir(folder)

os.path.join(folder,list_folder)

'G:\Drives compartilhados\Modec\MV30\fotos_embarque_2024\imagens_360_convertidas_para_scan_points\topside'
os.path.join('G:\Drives compartilhados\Modec\MV30\fotos_embarque_2024\imagens_360_convertidas_para_scan_points\topside','m01')

numer = len(list_folder)






