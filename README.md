# AI-Workflow-Pipeline

https://ai-student-workflow-pipeline.streamlit.app

How to use:

To use our agent you will click the provided link to our page. Here you will be prompted to upload a file or to simply paste paste text in the textbox which you want it to read. From here you will click the button to create the study material.

NOTE\* if attempting to run it from the code repository, you will need to isntall the dependencies in the requirements.txt, and a chatgpt api key. Remember you can use different models with the same key so you might have to change the model in the gpt_client file. you will also need to create a “.streamlit” folder outside of the source folder of the repository and create a file inside the folder called secrets.toml inside of this folder you will put this: GPT_API_KEY = “your_api_key”.

After downloading these, you will need to go to the terminal, navigate to the filepath of your code using the “cd” command and run this command:

streamlit run app.py

Once this runs it will redirect you to a locally hosted webpage that lets you run it.
Of course all of this can be avoided by simply using our link that we provide.
