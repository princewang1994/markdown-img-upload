# PYTHON=/Users/prince/anaconda/bin/python
# png_name=blog_`date +%Y%m%d%H%M%s`.png
# # png_name=abc.png
# pb_content=`pbpaste`

# if [[ $pb_content =~ .*\.[png|jpg|jpeg|bmp] ]]; then
	
# 	pb_content=`$PYTHON clipboard.py`
# 	cp $pb_content $png_name

# 	if [ $? -eq 0 ]; then
# 		query=$png_name
# 	else
# 		query=`cat alfred.log`
# 		rm alfred.log
# 	fi
# else
# 	/usr/local/bin/pngpaste $png_name 2> alfred.log
# 	if [ $? -eq 0 ]; then
# 		query=$png_name
# 	else
# 		query=`cat alfred.log`
# 		rm alfred.log
# 	fi
# fi
import re
import time
import shutil
import sys
import os
from clipboard import get_paste_img_file

data_type = ['png', 'bmp', 'jpg', 'jpeg']
re_postfix = '({})'.format('|'.join(data_type))
pattern = re.compile(r'https?://.*\.' + re_postfix)

def make_filename(type):
    return time.strftime('blog_%Y%m%d%H%M%S') + '.' + type

def copy_from_local(path, dst_path):
    # print('cp {} {}'.format(path, dst_path))
    shutil.copy(path, dst_path)

def copy_from_web(url, dst_path):
    os.system('/usr/local/bin/wget {} -q -O {}'.format(url, dst_path))

def copy_from_snapshot(dst_path):
    os.system('/usr/local/bin/pngpaste {} > /dev/null 2>&1'.format(dst_path))


if __name__ == '__main__':
    
    if len(sys.argv) > 1: # web or local
        pb_content = sys.argv[1]
        file_type = os.path.basename(pb_content).split('.')[-1]
        file_path = make_filename(file_type)

        if file_type not in data_type:
            exit(0)
        
        if re.match(pattern, pb_content): # from web url
            copy_from_web(pb_content, file_path)

        else:
            src_path = get_paste_img_file()
            if src_path and os.path.exists(src_path): # from local file
                copy_from_local(src_path, file_path)

    else: # from snapshot
        file_path = make_filename('png')
        copy_from_snapshot(file_path)
    
    print file_path
