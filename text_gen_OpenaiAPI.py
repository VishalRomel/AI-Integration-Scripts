from openai import OpenAI
import os
from dotenv import load_dotenv


#Check your .env file and place your openai key there
load_dotenv()
client = OpenAI(
     api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_response(user_input: str) -> str:
    message: str = user_input.lower()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
         messages=[{"role": "system", "content":'You are a helpful assistant name Jeff'},
                   {"role": "user", "content": message}]

        )
   # print(response) print everything thats send back from open ai
    return response.choices[0].message.content.strip() 


# Main function to call the get_response function
def main():
   
    question = "Dogs or cats?"  # Example question to ask the assistant
    response = get_response(question)  # Call the function to get the response from the assistant

    # Output the response
    print("Assistant Jeff's response:", response)

if __name__ == "__main__":
    main()




    #If you like to add context replace message in line 15 with thi. the second row gives the ai context
  
                    # {"role": "system", "content": "You are a helpful assistant."},
                    # {"role": "user", "content": f"Here is data: {"add your context here"}."},
                    # {"role": "user", "content": f"Based on the above data, please answer the following query: {message}."}
