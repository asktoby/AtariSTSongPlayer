# Waveshare LCD1602 I2C Module

- [English Version](./README.md)

用惯了传统的的LCD1602液晶屏，来尝试一下我们的I2C通信的LCD1602屏吧，对比传统的占用引脚更少，操作更简单


#产品链接(https://www.waveshare.net/shop/LCD1602-I2C-Module.htm)

    SKU：23991

#目录介绍
* examples：示例源码文件
* ib：LCD1602驱动文件

# 概述

 Waveshare LCD1602 I2C Module 多种背光颜色液晶屏可以显示2x16个字符，支持屏幕滚动，光标移动，背光亮度调节等功能

# 硬件连接
LCD1602 	-> Pico/Pico w/Pico2/Pico2 W

VCC 	-> 3V3
GND  	-> GND
SCL 	-> BCM3
SDA 	-> BCM2

# 库安装
## python
  sudo apt install python3-smbus

# 示例运行
 cd ~
 wget https://files.waveshare.net/wiki/LCD1602%20I2C%20Module/LCD1602_I2C_Module_Demo.zip
 cd ~/LCD1602_I2C_Module_code/Raspberry/python/examples
 python Character_display.py
总共五个示例，用python运行即可展示不同效果、

# 函数介绍

```MicroPython

  def command(self, cmd)
    '''
      @brief send command
      @param cmd 发送的命令
    '''

  def data(self,data)
    '''
      @brief write character
      @param data 写入的数据
    '''

  def setCursor(self,col,row)
    '''
      @brief 设置光标位置
      @param col 列数 可选范围 0-39
      @param row 行数 可选范围 0-1，0代表了第一行，1代表了第二行
    '''

  def clear(self)
    '''
      @brief 清除显示并将光标回到初始位置（0位置）
    '''

  def printout(self,arg)
    '''
      @brief 向液晶屏输出显示
      @param arg 输出的数据
    '''

 def createChar(self, location, charmap)
    '''
      @brief 允许我们将前8个CGRAM位置填充自定义字符
      @param location  代替字符 范围（0-7）
      @param charmap 字符列表 大小8个字节
    '''

  def scrollDisplayLeft(self)
    '''
      @brief 向左滚动显示
    '''

  def scrollDisplayRight(self)
    '''
      @brief 向右滚动显示
    '''

  def cursor(self)
    '''
      @brief 打开下划线光标
    '''

  def nocursor(self)
    '''
      @brief 关闭下划线光标
    '''

  def leftToRight(self)
    '''
      @brief 此函数用于从左到右流动的文本
    '''

  def rightToLeft(self)
    '''
      @brief 此函数用于从右到左流动的文本
    '''

  def autoscroll(self)
    '''
      @brief 这将使文本从显示光标处“右对齐”
    '''

  def noautoscroll(self)
    '''
      @brief 这将使文本从显示光标处“左对齐”
    '''

  def display(self)
    '''
      @brief 打开显示
    '''

 def set_brightness(self, Value)
    '''
      @brief 设置背光亮度
      @param Value 范围（0-100）
    '''

 def set_mode(self, Mode)
    '''
      @brief 背光模式
      @param Mode 正常模式（0x00）,呼吸模式（0x20）
    '''
```

# 兼容性

| 开发板	| 工作正常 | 工作错误 | 未测试	| 备注	|
| ----------	| :-------: | :-------: | :-------: | :-------: |
| Rpi 4 	    |     √     |           |           |         	|
| Rpi 5	      |     √  	  |           |           |         	|
| Rpi zero 	  |         	|           |    √   	  |         	|
| Rpi zero w	|     √    	|           |        	  |         	|
| Rpi zero 2w	|     √    	|           |        	  |         	|
| Rpi 3B+ 	  |     √     |           |           |         	|

# 历史

- 日期 2025-01-06
- 版本 V1.0.0

