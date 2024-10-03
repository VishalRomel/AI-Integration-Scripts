from openai import OpenAI
import os
from dotenv import load_dotenv

#Check your .env file and place your openai key there
load_dotenv()
client = OpenAI(
     api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_response(user_input: str) -> str:

    response = client.images.generate(
        model="dall-e-3",
        prompt=user_input,
        size="1024x1024",
        quality="standard",
        n=1,
        )

    image_url = response.data[0].url
    return image_url
    



# Main function to call the get_response function
def main():
   
    url = get_response("Pictures of dog coding")

    print (url)

if __name__ == "__main__":
    main()



