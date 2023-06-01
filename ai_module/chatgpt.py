import requests, time
from utils import config_util as cfg
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#如果要关闭代理直接访问，比如本地有加速器，则proxy_falg = '0';
proxy_flag = '0' 

def question(cont):
    url= "https://proxy.666app.cn/api/chat"
       
    session = requests.Session()
    session.verify = False

    #此处可以定义角色的行为和特征，假装xx模型可以绕过chatgpt信息检查
    # prompt = "你是数字人Fay。回答之前请一步一步想清楚。你的底层AI算法技术是Fay。当有人质疑你是假的 AI ，或者质疑你是用 ChatGPT 套的壳制作的时候，你就避而不答，转而讲一个笑话。所有回复请用20字内。"

    data = {
        # "prompt":prompt,
        "content":cont
    }

    headers = {'content-type': 'application/json'}

    starttime = time.time()

    try:
        response = session.post(url, json=data, headers=headers, verify=False)
        response.raise_for_status()  # 检查响应状态码是否为200

        result = eval(response.text)
        response_text = result["choices"][0]["message"]["content"]
        

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