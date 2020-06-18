from zipfile import ZipFile

with ZipFile('./SR/DIV2K_train_LR_bicubic_X2.zip', 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall()