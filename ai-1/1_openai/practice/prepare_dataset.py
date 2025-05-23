import json
import os
import pandas as pd



def convert_json_to_jsonl(json):
    li = json["utterances"]
    new_datas = []
    for i in range(int(len(li)/2)):
        new_data = {}
        new_data["prompt"] = li[i]["text"]
        new_data["completion"] = li[i+1]["text"]
        new_datas.append(new_data)
    return new_datas



final_datas = []



lst = os.listdir('./archiv')
for folder in lst:
    jsonlist = os.listdir('./archiv/'+ folder)
    for each_file in jsonlist:
        with open('./archiv/'+ folder +'/' +each_file,'r') as f:
            each_str = ""
            for i in f:
                each_str += i
            
            each_json = json.loads(each_str)
            each_data_li = convert_json_to_jsonl(each_json)
            for data in each_data_li:
                final_datas.append(data)

print(final_datas)
print(len(final_datas))           


with open('result.json', 'w') as f:
    for entry in final_datas:
        f.write(json.dumps(entry,ensure_ascii=False)+'\n')
            
            
            
               
