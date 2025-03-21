# Comfy Webhook Node

**A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that sends generated media (images or videos) to a specified webhook endpoint.**

## Overview

The **Webhook Sender Node** accepts:
- **Media Input:** A batch of images (as a torch.Tensor).
- **Webhook URL:** A string URL where the media will be sent via an HTTP POST request.
- **File Type:** A dropdown option to choose between `"JPEG"` (for images) and `"MP4"` (for videos).

**Behavior:**
- For **JPEG**: Converts the first image in the batch to JPEG format using Pillow.
- For **MP4**: Converts a sequence of images into an MP4 video using MoviePy.
- Sends the converted file to the specified webhook using the `requests` library.

## Folder Structure

Place your custom node pack in the ComfyUI custom nodes folder:
ComfyUI/ └── custom_nodes/ └── comfy_webhook_node/ ├── init.py ├── webhook_node.py ├── requirements.txt (optional) └── README.md (this file

## Installation

### 1. Install Dependencies

Install the required packages in the Python environment that ComfyUI uses. In your ComfyUI portable folder, run:

```powershell
.\python_embeded\python.exe -m pip install requests pillow torch moviepy
2. Place the Node Pack
Copy the comfy_webhook_node folder into the ComfyUI/custom_nodes/ directory.
3. Restart ComfyUI
Restart ComfyUI so that it rescans the custom nodes and loads your new node.
Usage
Open ComfyUI and right-click on the canvas.
Navigate to the Custom category.
Add the Webhook Sender Node to your workflow.
Connect an image output (or video frames) to the node.
Enter your webhook URL (e.g., from Make.com or Webhook.site).
Select the file type: "JPEG" for images or "MP4" for videos.
Run your workflow. The node will convert the media and send it to the specified webhook.
Troubleshooting
Node Not Appearing:

Confirm your folder structure is correct.
Verify that your __init__.py file exports your node correctly:
from .webhook_node import WebhookSenderNode

NODE_CLASS_MAPPINGS = {
    "Webhook Sender Node": WebhookSenderNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Webhook Sender Node": "Webhook Sender Node",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
Restart ComfyUI and check the log for any errors.
ModuleNotFoundError for MoviePy:

Ensure MoviePy is installed in the embedded Python environment.
Use the correct import:
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

