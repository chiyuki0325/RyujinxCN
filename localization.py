#!env /usr/bin/python
import json, sys, os

print("Ryujinx 翻译生成脚本")
ryujinx_root = sys.argv[1]
form_list = json.loads(open(sys.path[0] + "/_FormList.json", 'r', encoding='utf-8').read())
for form_path in form_list["_FormList"]:
    # localize_json = json.loads(open(os.getcwd+"/"+form_name+".json",'r').read())
    form_name = form_path.split("/")[-1]
    print(form_name)
    original_str = open(ryujinx_root + form_path, 'r').read()
    replace_str = original_str
    localize = json.loads(open(sys.path[0] + "/Patch/" + form_name + ".json", 'r', encoding='utf-8').read())
    if ".cs" in form_name:
        # CSharp
        for str in localize:
            replace_str = replace_str.replace('"' + str + '"', '"' + localize[str] + '"')
    else:
        # Glade
        for str in localize:
            replace_str = replace_str.replace('>' + str + '<', '>' + localize[str] + '<')
    os.rename(ryujinx_root + form_path, ryujinx_root + form_path + ".bak")
    open(ryujinx_root + form_path, "w", encoding='utf-8').write(replace_str)
    print("翻译" + form_path)
print("翻译完毕！")
