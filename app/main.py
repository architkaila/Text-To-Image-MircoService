# Library Imports
from fastapi import FastAPI
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from fastapi.responses import FileResponse

# App Definition
app = FastAPI()

# Model Cofiguration
model_id = "stabilityai/stable-diffusion-2-1"

# Model Pipeline Initialization
pipe = StableDiffusionPipeline.from_pretrained(model_id)

# Model Pipeline Configuration
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

# API Endpoint
@app.get("/vector_image")
def image_endpoint(prompt):
    """
    This endpoint takes a text prompt as input and returns an image.

    Args:
        prompt (str): Text prompt to generate image from.

    Returns:
        FileResponse: Image file response.
    """

    # Generate Image
    image = pipe(prompt, num_inference_steps=10).images[0]

    # Save Image
    image.save("image.png")
    
    return FileResponse("image.png")