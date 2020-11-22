from . import sender
from typing import Dict
from .tag_requests import *
from .tag_responses import *

def receive(event: str, body: Dict) -> str:
    if event == "CreateTag":
        tag = create_tag(**body)
        return sender.send("confirm_tag_creation", confirm_tag_creation(tag))
    
    elif event == "UpdateTag":
        tag = update_tag(**body)
        return sender.send("confirm_tag_update", confirm_tag_update(tag))

    elif event == "DeleteTag":
        delete_tag(**body)
        return sender.send("confirm_tag_update", confirm_tag_deletion())

    elif event == "RequestTag":
        tag = request_tag(**body)
        return sender.send("return_tag", return_tag(tag))

    elif event == "RequestTagsForPost":
        tags = request_tags_for_post(**body)
        return sender.send("return_tags_for_post", return_tags_for_post(tags))