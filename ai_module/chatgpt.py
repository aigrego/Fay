import requests, time, json
from utils import config_util as cfg
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#如果要关闭代理直接访问，比如本地有加速器，则proxy_falg = '0';
proxy_flag = '0' 

def question(cont):
    data = {
        "content":cont
    }

    starttime = time.time()

    try:
        response = requests.post("https://proxy.666app.cn/api/chat", data=data, stream=True)
        response.raise_for_status()  # 检查响应状态码是否为200

        json_data = ''
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                json_data += chunk.decode('utf-8')
                try:
                    result = json.loads(json_data)
                    json_data = ''
                    print(result)
                    response_text = result["choices"][0]["message"]["content"]
                except json.JSONDecodeError:
                    pass
        

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        response_text = "抱歉，我现在太忙了，休息一会，请稍后再试。"


    print("接口调用耗时 :" + str(time.time() - starttime))

    return response_text

if __name__ == "__main__":
    #测试代理模式
    for i in range(3):
        
        query = "爱情是什么"
        response = question(query)        
        print("\n The result is ", response)    