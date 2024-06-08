from fastapi import Request


async def log_middleware(request: Request, call_next):
    # 記錄請求信息
    print(f"Request: {request.method} {request.url}")

    # 繼續處理請求
    response = await call_next(request)

    # 記錄響應信息
    print(f"Response: {response.status_code}")

    # 返回響應
    return response
