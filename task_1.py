import os

p_list = {'my_project': [{'settings'[]}, {'mainapp'[]}, {'adminapp'[]}, {'authapp'[]}]}
# создаем папки
for key, value in p_list.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))
