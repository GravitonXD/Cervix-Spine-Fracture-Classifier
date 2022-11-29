import re
import os

# replace with file locations
train_frac_LOCATION = r'TRAIN FRACTURE LOCATION HERE'
train_norm_LOCATION = r'TRAIN NORMAL LOCATION HERE'
val_frac_LOCATION = r'TEST FRACTURE LOCATION HERE'
val_norm_LOCATION = r'TEST NORMAL LOCATION HERE'

# use this to keep track of variations (this is not used)
def rename_keep_var(location, prefix_here):
    patterns = ['[A-Z 0-9]+']
    codes = []
    for item in os.listdir(location):
        for p in patterns:
            match = re.findall(p, item)
        if(match[0] not in codes):
            codes.append(match[0])
        for i in codes:
            if i in item:
                newname = item.replace(i, f"{prefix_here}{codes.index(i)+1} ")
                print(f"from {item} to {newname}")
                # rename: 
                # os.rename(f'{location}\{item}', f'{location}\{newname}')
    print(codes)

# rename files, 1-n 
def rename(location, prefix_here):
    patterns = ['[A-Z 0-9]+']
    codes = []
    count = 0
    for item in os.listdir(location):
        count = count + 1
        for p in patterns:
            match = re.findall(p, item)
        if(match[0] not in codes):
            codes.append(match[0])
        for i in codes:
            if i in item:
                newname = item.replace(i, f"{prefix_here}{count} ")
                print(f"from {item} to {newname}")
                # rename: 
                os.rename(f'{location}\{item}', f'{location}\{newname}')
    print(codes)

rename(train_frac_LOCATION, "train_frac_")
rename(train_norm_LOCATION, "train_norm_")
rename(val_frac_LOCATION, "test_frac_")
rename(val_norm_LOCATION, "test_norm_")