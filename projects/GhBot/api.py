from github.bot import GhBot
from fastapi import FastAPI,Request
from pydantic import BaseModel

app = FastAPI()


class ContentBody(BaseModel):
    text: str

class ResponseBody(BaseModel):
    status: str
    message: str
    info: dict


@app.post("/ghbot")
def ghBot(content:ContentBody, request:Request,response_model=ResponseBody):
    try:
        bot = GhBot()
        content = content.text
        data_dict,status,msg = bot.serve(content=content)

        if status == "success":
            return ResponseBody(
                status = status,
                message = msg,
                info = data_dict
            )
        else:
            return ResponseBody(
                status = "error",
                message = msg,
                info = data_dict
            )

    except Exception as e:
        print(e)
        return ResponseBody(
            status = "failure",
            message = "error",
            info = {}
        )