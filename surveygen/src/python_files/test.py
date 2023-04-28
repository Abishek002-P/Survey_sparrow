import openai
import json
import os
import csv

# Authenticate with OpenAI API

openai.api_key = "OPEN_AI_API_KEY"

file_name = "input.json"

file_extension = os.path.splitext(file_name)[1]

if(file_extension==".json"):
    # Load JSON input file
    with open(file_name, 'r') as f:
        input_data = json.load(f)
    # temp_array = json.dumps(input_data)

elif(file_extension==".csv"):
    with open(file_name, mode='r') as csv_file:
    
        # Create a CSV reader object
        csv_reader = csv.DictReader(csv_file)
        
        # Convert the CSV data into a list of dictionaries
        input_data = []
        for row in csv_reader:
            input_data.append(row)


prompt = "generate 10 survey question to a person based on the keyword from search history given below:\n \n"
prompt+=str(input_data[0])

print(prompt)
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=1000,
    n=1,
    stop=None,
    timeout=10,
)

    # Save generated survey questions to output file
with open(f"keyword_question2.txt", "w") as f:
    f.write(response.choices[0].text)