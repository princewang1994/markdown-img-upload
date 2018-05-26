import ConfigParser
import os 
import sys
import shutil

CONFIG_FILE = 'config.ini'

def make_blank_config(config_file):
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.add_section('qiniu')
    config.set('qiniu', 'ak', value='your QiNiu AppKey')
    config.set('qiniu', 'sk', value='your QiNiu Secret Key')
    config.set('qiniu', 'url', value='your http prefix')
    config.set('qiniu', 'bucket', value='your Bucket')
    config.write(open(config_file, 'w'))
    return config

def upload_to_qiniu(file_path, config):

    ak = config.get('qiniu', 'ak')
    sk = config.get('qiniu', 'sk')
    url = config.get('qiniu', 'url')
    bucket = config.get('qiniu', 'bucket')

    # authenticate
    os.system('/usr/bin/qshell account {} {}'.format(ak, sk))

    # upload
    os.system('./qshell fput princepicbed {} {} > /dev/null 2>&1'.format(file_path, file_path))

    # clear tmp file
    os.remove(file_path)

    return '![]({})'.format(os.path.join(url, file_path))


if __name__ == '__main__':
    
    file_path = sys.argv[1]

    if not os.path.exists(CONFIG_FILE):
        exit(0)
    else:
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.read(CONFIG_FILE)
    

    markdown_format = upload_to_qiniu(file_path, config)
    print markdown_format
