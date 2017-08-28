import config
from azure.storage.blob import BlockBlobService,ContentSettings

'''
In the notebook to be used include the following:

import sys
import importlib
sys.path.append('<PATH_TO_THIS_MODULE>')
file_to_blob = importlib.import_module('file_to_blob')
importlib.reload(file_to_blob)

Example usage:
storage_container = '<NAME_OF_CONTAINER>'
file_to_save = '<LOCAL_PATH_TO_FILE_TO_SAVE>'
blob_directory = '' # Leave as empty string, '' ,if no need for sub-directory inside blob
file_to_blob.main(storage_container,file_to_save,blob_directory)

'''

def main(storage_container,file_to_save,blob_directory):
    block_blob_service = BlockBlobService(account_name=config.storage_account, account_key=config.storage_key)
    
    if len(blob_directory) == 0:
        name_blob_to_save = file_to_save.split('/')[-1]
        print('saving: ',name_blob_to_save)
        
    else:
        name_blob_to_save = blob_directory+'/'+file_to_save.split('/')[-1]
        print('saving: ',name_blob_to_save)
        
    block_blob_service.create_blob_from_path(storage_container,name_blob_to_save,file_to_save,
                                                 content_settings=ContentSettings(content_type='text/csv; charset=utf-8') )
    print("File saved to blob")
        
        
if __name__ == '__main__':
    print('start')
    if len(sys.argv) != 3:
        print('run script with <storage_container> <file_name> <blob_directory>')
        sys.exit(1)
        
    storage_container = sys.argv[1]
    file_name = sys.argv[2]
    blob_directory = sys.argv[3]
    
    try:
        main(storage_container,file_name,blob_directory)
    except Exception as e:
        print(e)
        print("Error occurred")
        pass
    
    print('end')
    

