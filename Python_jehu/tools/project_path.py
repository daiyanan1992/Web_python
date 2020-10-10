import os




path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(path)


# D:\Web_python2\Python_jehu\test_result\html_report\test_juhe_report_new.html
#测试报告地址
HtmlReport_path=path+'\\test_result\html_report\\test_juhe_report_new.html'

#日志打印地址
Log_path=path+'\\test_result\log\py11.txt'

#文件目录地址D:\Web_python2\Python_jehu\test_data\test_case925.xlsx
Dir_path=path+'\\test_data\\test_case925.xlsx'
# print(Dir_path)