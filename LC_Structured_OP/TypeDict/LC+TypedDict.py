from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional , Literal

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-3.6-flash")

#Simple example of structured output using TypedDict
# class review(TypedDict):
#     summary:str
#     sentiment:str

# Using Annotated 
class review(TypedDict):
    summary:Annotated[str, "A brief summary of the review"]
    sentiment:Annotated[Literal["positive", "negative"], "The sentiment of the review"]
    pros:Optional[Annotated[str, "The positive aspects of the movie"]]
    cons:Optional[Annotated[str, "The negative aspects of the movie"]]
    name:Annotated[Optional[str],"Name of the reviewer"]

structured_output=model.with_structured_output(review, method="function_calling")


result=structured_output.invoke('''The movie 3 Idiots is an excellent film that combines comedy, friendship, and an important message about education. 
The story follows three engineering students who face academic pressure while discovering their passions and life goals. 
The performances of the actors are impressive, and the dialogues are both entertaining and meaningful. The film encourages students to focus on learning rather than simply chasing marks and ranks. 
Its engaging storyline, emotional scenes, and memorable music make it enjoyable for audiences of all ages. Overall, 3 Idiots is a highly recommended movie that 
inspires people to follow their dreams and think differently about success. Review by: John Doe''')   

print(result)   
# print("summary:", result["summary"])
# print("sentiment:", result["sentiment"])
# print("pros:", result["pros"])
# print("cons:", result["cons"])
# print("name:",result["name"])