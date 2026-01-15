import os 

def list_files_in_folder(folder_name):
    try:
        files = os.listdir(folder_name)
        return files,None
    except FileNotFoundError:
        return None
    except PermissionError:
        return None
def main():
    folder_paths=input("please provide  list of folders  names with spaces in between :").split()
    for folder_path in folder_paths:
        files,error_message=list_files_in_folder(folder_path)
        if files:
           print(f"files in {folder_path}:")
           for  file in files:
               print(file) 
        else:
            print(f"error in {folder_path}:{error_message}")
if __name__=="__main__":
    main()   
