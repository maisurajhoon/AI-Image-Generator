from diffusers import StableDiffusionPipeline
import torch

class ImageGenerator:
    def __init__(self):
        # Load the Stable Diffusion pipeline (first time will download weights)
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32
        )
        self.pipe = self.pipe.to("cpu")  # Use "cuda" if you have a GPU

    def generate_image(self, prompt):
        # Generate image from prompt
        image = self.pipe(prompt).images[0]
        return image