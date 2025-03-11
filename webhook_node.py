import requests
import torch
from PIL import Image
import io
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

class WebhookSenderNode:
    CATEGORY = "Custom"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "media": ("IMAGE",),
                "webhook_url": ("STRING", {"default": "https://example.com/webhook"}),
                "file_type": ("COMBO", {"options": ["JPEG", "MP4"], "default": "JPEG"}),
            }
        }

    RETURN_TYPES = ("INT", "STRING",)
    RETURN_NAMES = ("status_code", "response_text",)
    FUNCTION = "send_to_webhook"

    def send_to_webhook(self, media, webhook_url, file_type):
        try:
            if file_type == "JPEG":
                # Process as image: assume media is a torch.Tensor with shape [B,H,W,C]
                image_tensor = media[0]
                image_array = (image_tensor * 255).clamp(0, 255).byte().cpu().numpy()
                pil_image = Image.fromarray(image_array)
                buffer = io.BytesIO()
                pil_image.save(buffer, format="JPEG")
                buffer.seek(0)
                filename = "image.jpg"
                mime_type = "image/jpeg"
            elif file_type == "MP4":
                # Process as video: assume media is a list of image frames (torch.Tensor)
                frames = []
                for frame_tensor in media:
                    frame_array = (frame_tensor * 255).clamp(0, 255).byte().cpu().numpy()
                    frames.append(frame_array)
                # Create a video clip; adjust fps as needed
                clip = ImageSequenceClip(frames, fps=24)
                temp_video = "temp_video.mp4"
                clip.write_videofile(temp_video, codec="libx264", audio=False,
                                       temp_audiofile="temp-audio.m4a", remove_temp=True,
                                       verbose=False, logger=None)
                with open(temp_video, "rb") as f:
                    video_bytes = f.read()
                buffer = io.BytesIO(video_bytes)
                filename = "video.mp4"
                mime_type = "video/mp4"
            else:
                return (-1, "Unsupported file type")
        except Exception as e:
            return (-1, "Error during media conversion: " + str(e))
        
        files = {
            'file': (filename, buffer, mime_type)
        }
        
        try:
            response = requests.post(webhook_url, files=files)
            status_code = response.status_code
            response_text = response.text
        except Exception as e:
            return (-1, "Error sending POST request: " + str(e))
        
        return (status_code, response_text)
