# from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
# from langchain import OpenAI
# import sys
# import os
# from IPython.display import Markdown, display

# def construct_index(resume_directory):
#     # set maximum input size
#     max_input_size = 4096
#     # set number of output tokens
#     num_outputs = 2000
#     # set maximum chunk overlap
#     max_chunk_overlap = 20
#     # set chunk size limit
#     chunk_size_limit = 600

#     # define prompt helper
#     prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

#     # define LLM
#     llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))

#     documents = SimpleDirectoryReader(resume_directory).load_data()

#     service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    
#     indexes = {}
#     for resume in documents:
#         filename_without_extension = os.path.splitext(resume.metadata['filename'])[0]
#         index = GPTSimpleVectorIndex.from_documents([resume], service_context=service_context)
#         indexes[filename_without_extension] = index  # Use the filename without extension as the key
#         index.save_to_disk(f'index_{filename_without_extension}.json')

#     return indexes



# # def ask_ai():
# #     index = GPTSimpleVectorIndex.load_from_disk('index.json')
# #     default_questions = [
# #         "Tell me about yourself.",
# #         "What is your greatest strength?",
# #         "What is your biggest weakness?",
# #         "Why do you want to work here?",
# #         "Can you describe a challenging situation you've faced at work and how you handled it?",
# #         "Where do you see yourself in five years?",
# #         "Do you have any questions for us?"
# #     ]
# #     job_description_question = "What is the job description?"
# #     predefined_job_description_prompt = """
# #         Generate a job description for a Full Stack Engineer position. Include details about the responsibilities, qualifications, and skills needed for the role.
# #         ---
# #         Job Description:
# # We are looking for an experienced Full Stack Engineer to join our development team. In this role, you will be responsible for the overall development and implementation of front and back-end software applications. Your responsibilities will extend from designing system architecture to high-level programming, performance testing, and systems integration. To ensure success as a full stack engineer, you should have advanced programming skills, experience with application development, and excellent troubleshooting skills. Top-rated full stack engineers create and implement advanced software systems that perfectly meet the needs of the company.

# # Responsibilities:
# # - Meeting with the software development team to define the scope and scale of software projects.
# # - Designing software system architecture.
# # - Completing data structures and design patterns.


# # Qualifications:
# # - Bachelor’s degree in computer engineering or computer science.
# # - Previous experience as a full stack engineer.
# # - Advanced knowledge of front-end languages including HTML5, CSS, JavaScript, C++, and JQuery.


# # Skills:
# # - Strong problem-solving abilities.
# # - Team player with excellent interpersonal skills.
# # - Ability to work independently and take ownership of projects.
# # - Adaptability to new technologies and frameworks.

# # To apply, please submit your resume and a cover letter detailing your relevant experience and qualifications.

# # Location: [Lakebrains Technology,Udaipur]
# # Contact NUmber:+919664353500
# #     """

# #     documents = SimpleDirectoryReader("C:/Users/nites/OneDrive/Desktop/AI_CHATBOT/resume").load_data()  # Update the path

# #     while True:
# #         query = input("What do you want to ask? ")
        
# #         if query.lower() in ["exit", "quit", "bye"]:
# #             print("Exiting...")
# #             break

# #         if query.lower() in ["default", "default questions"]:
# #             for question in default_questions:
# #                 print(f"Question: {question}")
# #                 for resume in documents:  # Loop through each resume in your data
# #                     print(f"Resume: {resume}")  # Display the current resume being processed
# #                     response = index.query(f"{question} {resume}")  # Ask the question with the resume text
# #                     print(f"Response: {response.response}")  # Corrected this line
# #         elif query.lower() == job_description_question.lower():
# #             # Provide the predefined job description prompt
# #             print(predefined_job_description_prompt)
# #         else:
# #             response = index.query(query)
# #             print(f"Response: {response.response}")  # Corrected this line




# # os.environ["OPENAI_API_KEY"] = "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"
# # construct_index("resume")
# # ask_ai() 
# def ask_ai(indexes):
#     while True:
#         query = input("What do you want to ask? ")

#         if query.lower() in ["exit", "quit", "bye"]:
#             print("Exiting...")
#             break

#         if query.lower() == "list":
#             print("Available resumes:")
#             for i, resume in enumerate(indexes.keys()):
#                 print(f"{i + 1}. {resume}")
#             selected_index = input("Enter the number of the resume you want to select: ")
#             try:
#                 selected_index = int(selected_index) - 1
#                 selected_resume = list(indexes.keys())[selected_index]
#                 response = indexes[selected_resume].query(query)
#                 print(f"Response: {response.response}")
#             except (ValueError, IndexError):
#                 print("Invalid selection.")
#         else:
#             response = indexes[default_resume].query(query)
#             print(f"Response: {response.response}")

# os.environ["OPENAI_API_KEY"] = "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"
# resume_directory = "C:/Users/nites/OneDrive/Desktop/AI_CHATBOT/resume"
# documents = SimpleDirectoryReader(resume_directory).load_data()

# default_resume = "default_resume.txt"  # Set the default resume filename

# indexes = construct_index(resume_directory)

# ask_ai(indexes)

from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display

def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 2000
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600

    # define prompt helper
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

    index.save_to_disk('index.json')

    return index

# def ask_ai():
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     while True:
#         query = input("What do you want to ask? ")
#         response = index.query(query)
#         # response = index.query(prompt)
#         print("Response:", response.response)
# def ask_ai():
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     default_questions = [
#         "Tell me about yourself.",
#         "What is your greatest strength?",
#         "What is your biggest weakness?",
#         "Why do you want to work here?",
#         "Can you describe a challenging situation you've faced at work and how you handled it?",
#         "Where do you see yourself in five years?",
#         "Do you have any questions for us?"
#     ]

#     while True:
#         query = input("What do you want to ask? ")
        
#         if query.lower() in ["exit", "quit", "bye"]:
#             print("Exiting...")
#             break

#         if query.lower() in ["default", "default questions"]:
#             for question in default_questions:
#                 print(f"Question: {question}")
#                 for resume in documents:  # Loop through each resume in your data
#                     print(f"Resume: {resume}")  # Display the current resume being processed
#                     response = index.query(f"{question} {resume}")  # Ask the question with the resume text
#                     print(f"Response: {response.response}")  # Corrected this line
#         else:
#             response = index.query(query)
#             print(f"Response: {response.response}")  # Corrected this line
# def ask_ai():
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     default_questions = [
#         "Tell me about yourself.",
#         "What is your greatest strength?",
#         "What is your biggest weakness?",
#         "Why do you want to work here?",
#         "Can you describe a challenging situation you've faced at work and how you handled it?",
#         "Where do you see yourself in five years?",
#         "Do you have any questions for us?"
#     ]
#     job_description_question = "What is the job description?"
#     predefined_job_description_prompt = """
#         Generate a job description for a Full Stack Engineer position. Include details about the responsibilities, qualifications, and skills needed for the role.
#         Job Description:
# We are looking for an experienced Full Stack Engineer to join our development team. In this role, you will be responsible for the overall development and implementation of front and back-end software applications. Your responsibilities will extend from designing system architecture to high-level programming, performance testing, and systems integration. To ensure success as a full stack engineer, you should have advanced programming skills, experience with application development, and excellent troubleshooting skills. Top-rated full stack engineers create and implement advanced software systems that perfectly meet the needs of the company.

# Responsibilities:
# - Meeting with the software development team to define the scope and scale of software projects.
# - Designing software system architecture.
# - Completing data structures and design patterns.


# Qualifications:
# - Bachelor’s degree in computer engineering or computer science.
# - Previous experience as a full stack engineer.
# - Advanced knowledge of front-end languages including HTML5, CSS, JavaScript, C++, and JQuery.


# Skills:
# - Strong problem-solving abilities.
# - Team player with excellent interpersonal skills.
# - Ability to work independently and take ownership of projects.
# - Adaptability to new technologies and frameworks.

# To apply, please submit your resume and a cover letter detailing your relevant experience and qualifications.

# Location: [Lakebrains Technology,Udaipur]
# Contact NUmber:+919664353500
#     """

#     while True:
#         query = input("What do you want to ask? ")
        
#         if query.lower() in ["exit", "quit", "bye"]:
#             print("Exiting...")
#             break

#         if query.lower() in ["default", "default questions"]:
#             for question in default_questions:
#                 print(f"Question: {question}")
#                 for resume in documents:  # Loop through each resume in your data
#                     print(f"Resume: {resume}")  # Display the current resume being processed
#                     response = index.query(f"{question} {resume}")  # Ask the question with the resume text
#                     print(f"Response: {response.response}")  # Corrected this line
#         elif query.lower() == job_description_question.lower():
#             # Provide the predefined job description prompt
#             print(predefined_job_description_prompt)
#         else:
#             response = index.query(query)
#             print(f"Response: {response.response}")  # Corrected this line

# def ask_ai():
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     default_questions = [
#         "Tell me about yourself.",
#         "What is your greatest strength?",
#         "What is your biggest weakness?",
#         "Why do you want to work here?",
#         "Can you describe a challenging situation you've faced at work and how you handled it?",
#         "Where do you see yourself in five years?",
#         "Do you have any questions for us?"
#     ]
    
#     documents = SimpleDirectoryReader("C:/Users/nites/OneDrive/Desktop/AI_CHATBOT/resume").load_data()  # Update the path
    
#     print("Select a resume:")
#     for i, resume in enumerate(documents, start=1):
#         print(f"{i}. {resume}")
    
#     resume_choice = input("Enter the number of the resume you want to select (or type 'exit' to quit): ")
    
#     if resume_choice.lower() in ["exit", "quit", "bye"]:
#         print("Exiting...")
#         return
    
#     try:
#         resume_index = int(resume_choice) - 1
#         selected_resume = documents[resume_index]
#     except (ValueError, IndexError):
#         print("Invalid choice.")
#         return
    
#     print(f"Selected resume: {selected_resume}")
    
#     for question in default_questions:
#         response = index.query(f"{question} {selected_resume}")
#         print(f"Question: {question}\nResponse: {response.response}\n")

# os.environ["OPENAI_API_KEY"] = "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"
# construct_index("resume")
# ask_ai()

def ask_ai():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    default_questions = [
        "Tell me about yourself.",
        "What is your greatest strength?",
        "What is your biggest weakness?",
        "Why do you want to work here?",
        "Can you describe a challenging situation you've faced at work and how you handled it?",
        "Where do you see yourself in five years?",
        "Do you have any questions for us?"
    ]
    
    job_description_question = "What is the job description?"
    predefined_job_description_prompt = """
        Job Description:
We are looking for an experienced Full Stack Engineer to join our development team. In this role, you will be responsible for the overall development and implementation of front and back-end software applications. Your responsibilities will extend from designing system architecture to high-level programming, performance testing, and systems integration. To ensure success as a full stack engineer, you should have advanced programming skills, experience with application development, and excellent troubleshooting skills. Top-rated full stack engineers create and implement advanced software systems that perfectly meet the needs of the company.

Responsibilities:
- Meeting with the software development team to define the scope and scale of software projects.
- Designing software system architecture.
- Completing data structures and design patterns.
- Designing and implementing scalable web services, applications, and APIs.
- Developing and maintaining internal software tools.
- Writing low-level and high-level code.
- Troubleshooting and bug fixing.
- Identifying bottlenecks and improving software efficiency.
- Collaborating with the design team on developing micro-services.
- Writing technical documents.

Qualifications:
- Bachelor’s degree in computer engineering or computer science.
- Previous experience as a full stack engineer.
- Advanced knowledge of front-end languages including HTML5, CSS, JavaScript, C++, and JQuery.
- Proficient in back-end languages including Java, Python, Rails, Ruby, .NET, and PHP.
- Knowledge of database systems and SQL.
- Advanced troubleshooting skills.
- Familiarity with JavaScript frameworks.
- Good communication skills.
- High-level project management skills.

Skills:
- Strong problem-solving abilities.
- Team player with excellent interpersonal skills.
- Ability to work independently and take ownership of projects.
- Adaptability to new technologies and frameworks.

To apply, please submit your resume and a cover letter detailing your relevant experience and qualifications.

Location: [Lakebrains Technologu,Udaipur]
Contact NUmber:+919664353500
    """
    
    documents = SimpleDirectoryReader("C:/Users/nites/OneDrive/Desktop/AI_CHATBOT/resume").load_data()  # Update the path
    
    while True:
        print("Options:")
        print("1. Ask a question")
        print("2. Select a resume")
        print("3. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            query = input("What do you want to ask? ")
            response = index.query(query)
            print("Response:", response.response)
            
        elif choice == "2":
            print("Select a resume:")
            for i, resume in enumerate(documents, start=1):
                print(f"{i}. {resume}")
            
            resume_choice = input("Enter the number of the resume you want to select: ")
            
            try:
                resume_index = int(resume_choice) - 1
                selected_resume = documents[resume_index]
            except (ValueError, IndexError):
                print("Invalid choice. Please enter a valid number.")
                continue
            
            print(f"Selected resume: {selected_resume}")
            
            job_description_response = index.query(f"{job_description_question} {selected_resume}")
            print(f"Job Description Prompt: {job_description_question}\nResponse: {job_description_response.response}\n")
            
            for question in default_questions:
                response = index.query(f"{question} {selected_resume}")
                print(f"Question: {question}\nResponse: {response.response}\n")
            
        elif choice == "3":
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please enter a valid number.")

os.environ["OPENAI_API_KEY"] = "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"
construct_index("resume")
ask_ai()
# This code offers three options: asking a question, selecting a resume, or exiting. Depending on the user's choice, the program will respond accordingly.





