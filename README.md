## 命令行翻译工具

[![asciicast](https://asciinema.org/a/277253.svg)](https://asciinema.org/a/277253)

> 中文->英文，英文->中文

### 翻译api: 
* 有道翻译
* 百度翻译

### 安装

* 下载代码

```shell
$ git clone git@github.com:raojinlin/cmd-fanyi.git
```

* 设置PYTHONPATH

```shell
$ cd cmd-fanyi
$ export PYTHONPATH=`pwd`
```

* 安装依赖

```shell
$ cd cmd-fanyi
$ pip3 install -r requirements.txt
```

Changelog
--

* 2020-06-14
    1. 代码重构
    2. 添加控制台
    3. 修复百度翻译授权(支持cookie传入)
