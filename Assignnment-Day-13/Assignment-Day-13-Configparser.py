from configparser import ConfigParser
import os 

config=ConfigParser()
config.read("E:\\Py Ex\Advance_py\\ex_config.ini")

path=config.get("Exten","path")
old_ext=config.get("Exten","OE")
new_ext=config.get("Exten","NE")

os.chdir(path)
os.getcwd()

for file in os.listdir():
    if file.endswith(old_ext):
        print(file)
        first_name=file.rsplit(".",1)[0]
        new_name=first_name + "." + new_ext
        print(new_name)
        os.rename(file, new_name)
      
    

        
        



    

