# Library Imports
from fastapi import FastAPI
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from fastapi.responses import FileResponse, RedirectResponse
import logging

# App Definition
app = FastAPI()

# Model Cofiguration
model_id = "stabilityai/stable-diffusion-2-1"

# Model Pipeline Initialization
logging.info("Initializing Model Pipeline")
pipe = StableDiffusionPipeline.from_pretrained(model_id)

# Model Pipeline Configuration
logging.info("Configuring Model Pipeline")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
# pipe = pipe.to("cuda")

# API Endpoint
@app.get("/generate_image")
def generate_image(prompt, num_inference_steps: int = 3):
    """
    This endpoint takes a text prompt as input and returns an image.

    Args:
        prompt (str): Text prompt to generate image from.

    Returns:
        FileResponse: Image file response.
    """

    # Generate Image
    logging.info("Generating Image")
    image = pipe(prompt, num_inference_steps=num_inference_steps).images[0]

    # Save Image
    logging.info("Saving Image")
    image.save("image.png")
    
    return FileResponse("image.png")

@app.get("/health_check")
def health_check():
    """
    This endpoint is a health check for the API.

    Args:
        None

    Returns:
        dict: Health check response.
    """

    return {"msg": "Hello World"}

@app.get("/")
def root():
    """
    This endpoint redirects to the API documentation.

    Args:
        None

    Returns:
        RedirectResponse: Redirect to API documentation.
    """

    return RedirectResponse("/docs")