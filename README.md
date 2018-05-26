## 七牛云图床自动上传workflow



主要代码fork自[tiann/markdown-img-upload](https://github.com/tiann/markdown-img-upload)



## 特性

本工具主要使用了七牛提供的`qshell`工具，借助Alfred实现将本地的图片快速上传至[七牛云]()图床，上传主要分为三步：

1. 获取图片

2. 使用hotkey `CMD + Control + Option + V`上传图片

3. 上传返回的图片链接自动放入到系统剪切版中，可以直接使用`cmd + V` 使用

    

第一步中获取图片可以使用的图片来源有三种：

- Finder中复制图片文件

- Mac自带截图工具(`CMD + SHIFT + 4`)截取图片

- 浏览器右键复制**（目前只支持链接后缀为图片格式的，如jpg，png等）**

  

## 预览

暂无



## 安装

在安装前请确保已经申请了七牛云的服务，并获取AK和SK

### 依赖安装

本工具已经自带`qshell`可执行文件，无需手动安装

- wget（mac自带）
- pbpaste
- python requests (`pip install requests`)
- pyobjc(`pip install pyobjc`)

直接下载本项目中的`Alfred Picture Bed Uploader.alfredworkflow`，双击打开即可



## 使用



1. 小帽子中输入`mdimgsetup`打开七牛云配置

![](http://oodo7tmt3.bkt.clouddn.com/blog_20180526211020.png)

2. 配置AK，SK，URL和Bucket

![](http://oodo7tmt3.bkt.clouddn.com/blog_20180526210834.png)

3. 复制图片（本地，截图或web复制链接）
4. 快捷键`CMD + Control + Option + V`
5. 看到右上角提示后，上传完成，使用`CMD + V`粘贴至Markdown编辑器

## TODO

- 图片最好经过压缩以后再上传，否则流量容易爆掉
- 来源于浏览器右键的图片还没有完全适配，现在只支持link的末尾是图片后缀的
- gif动图预览
- 其他源文件的



## Contact with Me

​	欢迎所有建议，princewang1994@gmail.com