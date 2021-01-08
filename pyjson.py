import json
dict = {}

def get_json_keyValue(key):
    # 获取json里面数据
 
    with open('config.json', 'rb') as f:
        # 定义为只读模型，并定义名称为f
 
        params = json.load(f)
        # 加载json文件中的内容给params

        keyValue = params['data'][0][key]
        print("keyValue",keyValue)

    dict = keyValue
    f.close()
    # 关闭json读模式


    return dict
    # 返回dict字典内容

def get_json_data():
    # 获取json里面数据
 
    with open('config-backup.json', 'rb') as f:
        # 定义为只读模型，并定义名称为f
 
        params = json.load(f)
        # 加载json文件中的内容给params
        # for i in range(len(params)):
        id = params['data'][0]['id']#[0]是固定值，这个json只有一个成员
        project_name = params['data'][0]['project_name']
        print("project_name",project_name)
        params['data'][0]['project_name'] = '好样的'
        # 修改内容
        dict = params
        # 将修改后的内容保存在dict中
 
    f.close()
    # 关闭json读模式
 
    return dict
    # 返回dict字典内容
 
 
def write_json_data(dict):
    # 写入json文件
 
    with open('config.json', 'w') as r:
        # 定义为写模式，名称定义为r
 
        json.dump(dict, r)
        # 将dict写入名称为r的文件中
 
    r.close()
    # 关闭json写模式
 
 
# the_revised_dict = get_json_data()
# write_json_data(the_revised_dict)
print(str(get_json_keyValue('project_name_old')))