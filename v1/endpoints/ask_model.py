import fastapi
from pydantic import BaseModel
from core.process.rag import ask_model


class askRequest(BaseModel):
    query: str


class askResponse(BaseModel):
    answer: str


router = fastapi.APIRouter(prefix="/ask", tags=["ask"])


@router.get(
    path="",
    response_model=askResponse,
    name="ai",
)
def get_ai(request: askRequest = fastapi.Depends()):
    query = request.query

    answer = ask_model(query=query)

    return askResponse(answer=answer)
