# coding:utf-8
import sys
import os

# 你把原先框架的顺序修改了，修改的不对，下边这句就是把目录放到sys.path中，先执行这句才能获取到script和SRC，否则就会报错，sys无法找到script
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from script import addPathToPython, initSettings, selectModel


addPathToPython()
initSettings()
selectModel()

from SRC.main import Main
# Main('人力资源-员工管理职位.xml').run()
# Main('人力资源-员工管理.xml').run()
# Main('人力资源-劳动合同.xml').run()
Main('人力资源-假勤管理.xml').run()
Main('人力资源-薪资核算.xml').run()
Main('基本脚本录制.xml').run()
# Main('人力资源-员工服务.xml').run()
# Main('财务管理-总账.xml').run()
