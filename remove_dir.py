import os
import glob
import shutil

folder = '//faith/rf_gcf_logs/4G_RF/Regression/CY_2016/1quarter'
top = '//faith/rf_gcf_logs/4G_RF/Regression/CY_2016/1quarter'
the_file = 'SignallingLogs'
file_path = ''
for dirpath, dirnames, filenames in os.walk(top, topdown=False):
    for dirname in dirnames:
        if dirname == "SignallingLogs":
            file_path = os.path.join(dirpath, dirname)
    print(file_path)
    try:
        if os.path.isdir(file_path): 
            shutil.rmtree(file_path)
    except Exception as e:
        print(e)
