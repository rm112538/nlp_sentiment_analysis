from zipfile import ZipFile

def load_data():  
  try:
      with ZipFile('./sentiment+labelled+sentences.zip', 'r') as UnZipObject:
        UnZipObject.extractall('./data')
  except RuntimeError:
     print("The ZipFile not found")   

if __name__=='__main__':
  load_data()
