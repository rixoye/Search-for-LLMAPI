from flask import Flask, request, Response, stream_with_context
import requests
import json

app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    user_data = request.json
    headers = {
        "Authorization": request.headers.get('Authorization'),
        "Content-Type": "application/json"
    }
    
    user_data['stream'] = True
    
    # 转发请求
    response = requests.post(
        "https://api.siliconflow.cn/v1/chat/completions",
        json=user_data,
        headers=headers,
        stream=True
    )
    
    def generate():
        is_first_reasoning = True
        last_was_reasoning = False
        
        for line in response.iter_lines():
            if line:
                json_str = line.decode('utf-8').replace('data: ', '')
                
                if json_str == '[DONE]':
                    if last_was_reasoning:
                        modified_data = {
                            'choices': [{
                                'delta': {
                                    'content': "</think>"
                                }
                            }]
                        }
                        yield f"data: {json.dumps(modified_data)}\n\n"
                    yield 'data: [DONE]\n\n'
                    break
                
                try:
                    response_data = json.loads(json_str)
                    if 'choices' in response_data and response_data['choices']:
                        choice = response_data['choices'][0]
                        if 'delta' in choice:
                            delta = choice['delta']
                            
                            reasoning = delta.get('reasoning_content', '')
                            if reasoning:
                                # 添加开始标签
                                if is_first_reasoning:
                                    modified_data = {
                                        'choices': [{
                                            'delta': {
                                                'content': "<think>"
                                            }
                                        }]
                                    }
                                    yield f"data: {json.dumps(modified_data)}\n\n"
                                    is_first_reasoning = False
                                
                                modified_data = {
                                    'choices': [{
                                        'delta': {
                                            'content': reasoning
                                        }
                                    }]
                                }
                                yield f"data: {json.dumps(modified_data)}\n\n"
                                last_was_reasoning = True
                            
                            content = delta.get('content', '')
                            if content:
                                # 添加结束标签
                                if last_was_reasoning:
                                    modified_data = {
                                        'choices': [{
                                            'delta': {
                                                'content': "</think>\n\n"
                                            }
                                        }]
                                    }
                                    yield f"data: {json.dumps(modified_data)}\n\n"
                                    last_was_reasoning = False
                                yield f"data: {json_str}\n\n"
                            
                            if not (reasoning or content):
                                yield f"data: {json_str}\n\n"
                        else:
                            yield f"data: {json_str}\n\n"
                    else:
                        yield f"data: {json_str}\n\n"
                        
                except json.JSONDecodeError:
                    yield f"data: {json_str}\n\n"
    
    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream'
    )

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000) 
