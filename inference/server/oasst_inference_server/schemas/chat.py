import pydantic
from oasst_shared.schemas import inference


class CreateMessageRequest(pydantic.BaseModel):
    parent_id: str | None = None
    content: str = pydantic.Field(..., repr=False)
    work_parameters: inference.WorkParameters = pydantic.Field(default_factory=inference.WorkParameters)

    @property
    def worker_compat_hash(self) -> str:
        return inference.compat_hash(model_name=self.work_parameters.model_name)


class CreateMessageResponse(pydantic.BaseModel):
    prompter_message: inference.MessageRead
    assistant_message: inference.MessageRead


class TokenResponseEvent(pydantic.BaseModel):
    token: inference.TokenResponse | None
    error: str | None


class VoteRequest(pydantic.BaseModel):
    score: int


class ReportRequest(pydantic.BaseModel):
    report_type: inference.ReportType
    reason: str


class CreateChatRequest(pydantic.BaseModel):
    pass


class ChatListRead(pydantic.BaseModel):
    id: str


class ChatRead(pydantic.BaseModel):
    id: str
    messages: list[inference.MessageRead]


class ListChatsResponse(pydantic.BaseModel):
    chats: list[ChatListRead]
