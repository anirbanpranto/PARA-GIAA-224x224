import os

path = '/media/workstation/0832621B32620DCE/Bala/Para_Resize/PARA/imgs'

for i in range(1, 447):
    os.chdir(path + '/session'+str(i))
    os.system('pwd')
    os.system('mogrify -resize 224x224! *.jpg')
    os.chdir(path)
