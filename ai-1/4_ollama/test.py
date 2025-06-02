import requests
import json
import os

ollama_host = os.environ["OLLAMA_HOST"]
ollama_url = f"{ollama_host}/api/generate" # YOUR_DESKTOP_IP를 실제 데스크톱 IP로 변경

sample_data = {
  "model": "llama3:latest",
  "prompt": "1+1은?",
  "stream": False,
  "options": {
    "num_predict": 50, # 약 100자 이내를 위해 조정 필요
    "temperature": 0
  }
}

try:
    response = requests.post(ollama_url, data=json.dumps(sample_data))
    response.raise_for_status() # HTTP 오류가 발생하면 예외 발생

    result = response.json()
    generated_text = result.get("response", "").strip()

    print("생성된 조언:\n", generated_text)

except requests.exceptions.RequestException as e:
    print(f"Ollama 서버에 연결할 수 없거나 요청 중 오류 발생: {e}")
    print("Ollama 서버가 실행 중인지, IP 주소와 포트가 올바른지 확인해주세요.")
except Exception as e:
    print(f"응답 처리 중 오류 발생: {e}")