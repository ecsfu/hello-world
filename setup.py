from setuptools import setup

setup(
    name='install_test',# 需要打包的名字,即本模块要发布的名字
    version='v1.0',#版本
    description='A  module for test', # 简要描述
    py_modules=['test'],   #  需要打包的模块
    author='eiuc', # 作者名
    author_email='',   # 作者邮件
    url='https://github.com/eiuc/hello-world', # 项目地址,一般是代码托管的网站
    # requires=['requests','urllib3'], # 依赖包,如果没有,可以不要
    license='MIT'
)

 
