import dropbox
import os

class TransferFiles:
   def __init__(self, access_token):
      self.access_token = access_token
   def uploadFile(self, file_from, file_to):
      dbx = dropbox.Dropbox(self.access_token)
      for root, dirs, files in os.walk(file_from):
         for file in files:
            local_path = os.path.join(root, file)
            rel_path = os.path.relpath(local_path, file_from)
            #removes excess part till file_from in path
            dropbox_path = os.path.join(file_to, rel_path)
            with open(local_path, 'rb') as f:
               dbx.files_upload(f.read(), dropbox_path)

def main():
   access_token ="sl.BEQ7sKTa1Drxm6CuvFqcW-le0GlivVZEXpFdDwuBPA1BBYd-3MfmRFk_7a6Nbl24QkrM7fAAjn1XKk6s-7bUHTF5Xt6cHum96-2cCVw9WxNRFqew27U2l4MDWVeW93MI06Xm6TsJSMw"
   file_from = input('Enter path of folder in which files are contained: ')
   file_to = input('Enter path where files are to be uploaded in dropbox: ')
   transfer = TransferFiles(access_token)
   transfer.uploadFile(file_from, file_to)
   print("Files uploaded")

main()