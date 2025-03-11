# __init__.py
from .nodes import WebhookSenderNode

NODE_CLASS_MAPPINGS = {
    "Webhook Sender Node": WebhookSenderNode
}

# Optionally rename how the node appears in ComfyUI's Add Node menu
NODE_DISPLAY_NAME_MAPPINGS = {
    "Webhook Sender Node": "Webhook Sender Node"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
