# python script to extract zip files
from zipfile import ZipFile

try:
    # the zip file name you want to extract
    name = (input("Enter the file.zip file name : "))

    # opening in read mode
    with ZipFile(name, 'r') as x:
        x.printdir()
        # extracting the files
        print("Extracting all files now")
        x.extractall()
        print("Done!")

except FileNotFoundError as e:
    print("File Not Found.. ")
except:
    print("Unsupported Zip file format!")
