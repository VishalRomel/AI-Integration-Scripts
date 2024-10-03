from diffusers import StableDiffusionPipeline
import torch


model_id = "sd-legacy/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)#change to float32 if you are useing CPU instead of cuda
#Change cuda to cpu if you have a Nvidia GPU a
pipe = pipe.to("cuda")

prompt = "Picture of dogs coding"
image = pipe(prompt).images[0]  
    
image.save("dog.png")
