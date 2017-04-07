#!/usr/bin/python3

"""This script parse the content of a xml file"""

import os
import shutil

if not os.path.exists('./tmp'):
    os.system('mkdir tmp')
if not os.path.exists('./release'):
    os.system('mkdir release')

while True:
    APK_PATH = input("please input apk path:")
    APK_PATH = APK_PATH.strip()
    if APK_PATH == 'q':
        break
    APK_NAME = os.path.basename(APK_PATH)

    TMP_PATH = './tmp/' + APK_NAME
    RELEASE_PATH = './release/' + APK_NAME
    shutil.copyfile(APK_PATH, TMP_PATH)
    CMD = "zip -d %s \"META-INF*\"" %(TMP_PATH)
    os.system(CMD)
    CMD = "./zipalign -v -p 4 %s %s" %(TMP_PATH, RELEASE_PATH)
    os.system(CMD)
    CMD = "./apksigner sign --v2-signing-enabled false --ks release.jks --ks-pass pass:123456 %s" %(RELEASE_PATH)
    os.system(CMD)
    CMD = "./apksigner verify -v  %s" %(RELEASE_PATH)
    os.system(CMD)
    CMD = "rm %s" %(TMP_PATH)
    os.system(CMD)

# FILES = os.listdir('./')

# for file in FILES:
#     if file.endswith('.apk'):
#         print(file)
#         TMP_PATH = './tmp/' + file
#         RELEASE_PATH = './release/' + file
#         shutil.copyfile(file, TMP_PATH)
#         CMD = "zip -d %s \"META-INF*\"" %(TMP_PATH)
#         os.system(CMD)
#         CMD = "./zipalign -v -p 4 %s %s" %(TMP_PATH, RELEASE_PATH)
#         os.system(CMD)
#         CMD = "./apksigner sign --v2-signing-enabled false --ks release.jks --ks-pass pass:123456 %s" %(RELEASE_PATH)
#         os.system(CMD)
#         CMD = "./apksigner verify -v  %s" %(RELEASE_PATH)
#         os.system(CMD)
#         CMD = "rm %s" %(TMP_PATH)
#         os.system(CMD)
