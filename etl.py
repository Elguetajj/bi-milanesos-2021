def getFiles(folder,engine,drive,fileFormat=".csv"):
    folder_id = ''

    file_list = drive.ListFile({'q': "'1THD1cqlgpxsNj1ZFeQeg255Ne0As6DQL' in parents and trashed=false"}).GetList()
    for file in file_list:
        if(file['title'] == folder):
            folder_id = file['id']
            break
    
#     print('folder title: %s, folder id: %s' % (folder, folder_id))
          
    query_str = f"title contains '{fileFormat}' and '{folder_id}' in parents and trashed=false"  
    
    file_list = drive.ListFile({'q': query_str}).GetList()
    
    return file_list