import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse, JSONResponse
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

app = FastAPI()

# DTO 정의
class RequestUserDto(BaseModel):
    nickname: str = Field(title='사용자 닉네임')
    email: EmailStr = Field(title='사용자 이메일 주소')
    phone: str = Field(title='사용자 휴대폰 번호', pattern='^010-\d{4}-\d{4}$')
    description: Optional[str] = Field(title='사용자 소개')

    class Config:
        schema_extra = {
            'example': {
                'nickname': '왓쓴',
                'email': 'watson@example.com',
                'phone': '010-1234-1234',
                'description': '버즈니왓슨입니다'
            }
        }

# Response용 DTO
class ResponseUserDto(RequestUserDto):  # 그대로 복사해서 반환만 할 거면 상속 사용 가능
    pass

# 헬스 체크 API
@app.get(
    path='/', 
    description='HealthCheck용 포인트입니다.',
    status_code=status.HTTP_200_OK,
    response_class=PlainTextResponse,
    responses={200: {"description": "Health check 응답"}}    
)
async def health_check():
    return "ok"

# 회원가입 요청 API
@app.post(
    path='/registerReq',
    description='회원가입 API (요청 값 그대로 보기)',
    status_code=201,
    response_class=JSONResponse,
    responses={
        201: {
            "description": "가입 사용자 정보",
            "content": {
                "application/json": {
                    'example': {
                        'nickname': '왓쓴',
                        'email': 'watson@example.com',
                        'phone': '010-1234-1234',
                        'description': '버즈니왓슨입니다'
                    }
                }
            }
        }
    }
)
async def register_req_usr(req: RequestUserDto):
    return req.dict()

# 회원가입 응답 모델 API
@app.post(
    path='/registerRes',
    description='회원가입 API (response_model 사용)',
    status_code=201,
    response_model=ResponseUserDto,
    responses={
        201: {
            "description": "가입 사용자 정보"
        }
    }
)
async def register_res_usr(req: RequestUserDto):
    return req

# 서버 실행
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3000, reload=True)
