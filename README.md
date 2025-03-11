Comfy Webhook Node
Overview:
This custom node pack for ComfyUI sends generated media (images or videos) to a specified webhook endpoint. It supports both JPEG (for images) and MP4 (for videos).

The Webhook Sender Node accepts: • Media Input: A batch of images (as a torch.Tensor). • Webhook URL: A string URL where the media will be sent via an HTTP POST request. • File Type: A dropdown option to choose between "JPEG" and "MP4".

Depending on the file type:

For JPEG: It converts the first image in the batch to JPEG format using Pillow.
For MP4: It converts a sequence of images into a video using MoviePy.
Installation:
Place the custom node pack folder "comfy_webhook_node" inside your ComfyUI custom nodes folder: ComfyUI/custom_nodes/comfy_webhook_node

The folder should include the following files:

init.py
webhook_node.py
requirements.txt (optional)
README.md (this file)
Install the required dependencies using your embedded Python. In your ComfyUI portable folder, run: .\python_embeded\python.exe -m pip install requests pillow torch moviepy

Note: In webhook_node.py, the import for MoviePy must be: from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

Restart ComfyUI to load the new custom node.

Usage:
Open the ComfyUI interface and right-click on the canvas.
Navigate to the "Custom" category (as specified in the node class).
Add the "Webhook Sender Node" to your workflow.
Connect an image output (or video frames) and enter the webhook URL (from your service like Make.com or Webhook.site).
Select the desired file type ("JPEG" or "MP4").
Run the workflow. The node will convert the media and send it to the specified webhook.
Troubleshooting:
• If the node does not appear in ComfyUI:

Verify that the folder structure is correct (the node pack is in ComfyUI/custom_nodes/comfy_webhook_node).
Check that init.py and webhook_node.py contain the correct code with no errors.
Restart ComfyUI and review the logs for any error messages.
• If you encounter a ModuleNotFoundError for MoviePy:

Ensure MoviePy is installed in the embedded Python environment.
Confirm that the import statement in webhook_node.py is: from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
License:
This custom node pack is distributed under the MIT License.