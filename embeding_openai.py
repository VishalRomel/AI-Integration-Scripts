from openai import OpenAI
import os
from dotenv import load_dotenv

#Check your .env file and place your openai key there
load_dotenv()
client = OpenAI(
     api_key=os.environ.get("OPENAI_API_KEY"),
)
def get_response(user_input: str) -> str:
    
    response = client.embeddings.create(
        input=user_input,
        model="text-embedding-3-small"
    )

    return response.data[0].embedding 



# Main function to call the get_response function
def main():
   
    question = "Your text goes here"  # Example of text
    response = get_response(question)  # Call the function to get the response from the embedding

    # Output the response
    print( response)

if __name__ == "__main__":
    main()
