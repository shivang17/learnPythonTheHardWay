#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'PYTHON'))
	print(os.getcwd())
except:
	pass

#%%
name = "Shivang"
age = 23
print(f"My name is {name} and I am {age} years old")


#%%
greeting = "Kem Chho!!!"
print(f"My name is {name} and I am {age} years old. {greeting}")


#%%
print("Shivang\nSuchak\t23")


#%%
from sys import argv
script, file_name = argv
fo = open(file_name,'r')
read_file = fo.readfile()
print(read_file)


#%%
files = []
for i in range(100):
    filename = f"file_no_{i}.txt"
    files.append(filename)
print(files)


#%%
real_files = " ".join(files)
print(real_files)


#%%
# def file_filter(real_file_list,start=0,end=100):
#     real_files_list = real_files.split()
#     filtered_files = []
#     for file in real_files_list:
        
#         file_number = int(file.split("_")[-1].split(".")[0])
#         if file_number >= start and file_number <= end:
#             filtered_files.append(file)
#     return filtered_files
# result = file_filter(real_files)


def file_filter_noformat(real_files, start, end):
    if start > end:
        print("Start position should be smaller than end, please give valid input")
        return None
    else:
        real_files_list = real_files.split()
        filtered_files = []
        for number in range(start, end+1):
            for filename in real_files_list:
                if "_"+str(number) + "." in filename:
                    filtered_files.append(filename)
        return filtered_files

result = file_filter_noformat(real_files, 35,35)
print(result)


#%%
names = [1,2,3,4,5,6,7,8,9,["Shivang","Suchak",23]]
names.append("Hey where will I get added")

for i in names:
    print(i)


#%%
import os
check_file =os.listdir("/home/shivang/Desktop/PYTHON/")

for i in check_file:
    if str(i) == "settings.py":
        print("It exists")
        break
    else:
        print("No it doesn't exist")
        break


#%%

#%%



