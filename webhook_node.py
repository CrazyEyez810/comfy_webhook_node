# Import required libraries
import requests          # For sending HTTP POST requests
import torch             # For working with image tensors
from PIL import Image    # For image conversion/manipulation
import io                # For in-memory byte streams

class WebhookSenderNode:
    """
    A custom node that takes a media input (image) and a webhook URL,
    converts the media to JPEG format, and sends it via a POST request.
    """

    # Place the node in a "Custom" category in the add-node menu.
    CATEGORY = "Custom"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # The media input; we assume it is an IMAGE batch (torch.Tensor)
                "media": ("IMAGE",),
                # The webhook URL as a string; default can be changed by the user.
                "webhook_url": ("STRING", {"default": "https://example.com/webhook"}),
            }
        }
    
    # Define the outputs: HTTP status code and response text.
    RETURN_TYPES = ("INT", "STRING",)
    RETURN_NAMES = ("status_code", "response_text",)
    
    # Specify the name of the function that will be executed.
    FUNCTION = "send_to_webhook"

    def send_to_webhook(self, media, webhook_url):
        """
        Converts the first image in the media input (assumed as a torch.Tensor with shape [B,H,W,C])
        to a JPEG file and sends it as a POST request to the provided webhook URL.
        
        Parameters:
            media (torch.Tensor): Batch of images with shape [B, H, W, C] (values in 0-1).
            webhook_url (str): The URL to which the file will be posted.
            
        Returns:
            tuple: (status_code, response_text) from the POST request, or an error indicator.
        """
        # Convert the torch.Tensor (assumed batch of images) to a PIL Image
        try:
            if isinstance(media, torch.Tensor):
                # Extract the first image from the batch (shape [H,W,C])
                image_tensor = media[0]
                # Scale pixel values from 0-1 to 0-255 and convert to uint8
                image_array = (image_tensor * 255).clamp(0, 255).byte().cpu().numpy()
                # Create a PIL Image (assuming RGB channels)
                pil_image = Image.fromarray(image_array)
            else:
                # If the media is not a tensor, assume it is already a PIL Image
                pil_image = media

            # Save the PIL image to an in-memory bytes buffer in JPEG format
            buffer = io.BytesIO()
            pil_image.save(buffer, format="JPEG")
            buffer.seek(0)  # Reset buffer pointer to the beginning
        except Exception as e:
            # Return error code -1 and an error message if conversion fails
            return (-1, "Error converting media to JPEG: " + str(e))

        # Prepare the file payload for the POST request.
        files = {
            'file': ('image.jpg', buffer, 'image/jpeg')
        }
        
        try:
            # Send a POST request to the provided webhook URL with the image file attached.
            response = requests.post(webhook_url, files=files)
            status_code = response.status_code
            response_text = response.text
        except Exception as e:
            # Return error code -1 and an error message if the POST request fails
            return (-1, "Error sending POST request: " + str(e))
        
        # Return the HTTP status code and response text from the request.
        return (status_code, response_text)
