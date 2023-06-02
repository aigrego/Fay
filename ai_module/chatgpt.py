import requests, time, json
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def question(cont):
    data = { "content": cont }
    headers = {'content-type': 'application/json'}
    starttime = time.time()
    try:
        response = requests.post("https://proxy.666app.cn/api/chat", json=data, headers=headers, stream=True)
        response.raise_for_status()  # 检查响应状态码是否为200

        response_text = ''
        chunk_str = ''
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                chunk_str += chunk.decode('utf-8')
                if chunk_str.endswith("\n\n"):
                    # https://beta.openai.com/docs/api-reference/completions/create#completions/create-stream
                    # 解析chatGPT返回的数据格式，针对Stream方式
                    chunk_data = chunk_str.split("\n\ndata: ")[-1].replace("data: ", "")
                    chunk_str = ''

                    try:
                        result = json.loads(chunk_data)
                        response_text += result["choices"][0]["delta"]["content"]
                        print('解析数据块: %s' % result["choices"][0]["delta"]["content"])
                    except json.JSONDecodeError:
                        print('解析完成: %s' % chunk_data)

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        response_text = "抱歉，我现在太忙了，休息一会，请稍后再试。"


    print("接口调用耗时 :" + str(time.time() - starttime))

    return response_text

if __name__ == "__main__":
    #测试代理模式
    query = "爱情是什么"
    response = question(query)        
    print("\n The result is ", response)    