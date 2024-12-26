from fastapi import status 
from fastapi.responses import Response, JSONResponse
from fastapi.requests import Request

@app.middleware('http')
async def notFoudException(request: Request, call_next)-> Response | JSONResponse:
  try:
    return await call_next(request)
  except Exception as error:
    message = f"exception {str(error)}, item not found :'c"
    statusError = status.HTTP_404_NOT_FOUND
    return JSONResponse(content = message, status_code = statusError) 