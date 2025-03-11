from .webhook_node import WebhookSenderNode

NODE_CLASS_MAPPINGS = {
    "Webhook Sender Node": WebhookSenderNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Webhook Sender Node": "Webhook Sender Node",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
