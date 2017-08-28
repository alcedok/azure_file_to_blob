# Load .txt/.csv files to Azure Blob Storage

Make sure to fill out the config.py file with the corresponding storage\_account and storage\_key

```python
storage_account = ''
storage_key = ''
```

If running this in a Jupyter Notebook, make sure to include the following:

```python
import sys
import importlib
sys.path.append('<PATH_TO_THIS_MODULE>')
file_to_blob = importlib.import_module('file_to_blob')
importlib.reload(file_to_blob)
```

Sample code:

```python
storage_container = '<NAME_OF_CONTAINER>'
file_to_save = '<LOCAL_PATH_TO_FILE_TO_SAVE>'
blob_directory = '' # Leave as empty string, '' ,if no need for sub-directory inside blob
file_to_blob.main(storage_container,file_to_save,blob_directory)
```