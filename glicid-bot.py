import random

# Define responses related to the GLiCID supercomputer
responses_glicid = {
    "what is GLiCID?": ["GLiCID is a supercomputing center in Nantes used for high-performance computing (HPC) tasks in various scientific and research fields."],
    "where is GLiCID located?": ["GLiCID is located in Nantes."],
    "how can I access GLiCID?": ["To access GLiCID, you'll need to set up SSH access. You can find instructions on setting up SSH access at https://doc.glicid.fr/GLiCID-PUBLIC/latest/."],
    "where can I find documentation for GLiCID?": ["You can find documentation and user guides for GLiCID on the official website or in the documentation section of the GLiCID supercomputer."],
    "what is Slurm?": ["Slurm is a Workload Management System (WMS) that handles resources on the cluster. It is used for job scheduling, resource allocation, and job management on high-performance computing (HPC) clusters like GLiCID."],
    "what is Module command?": ["The Module command is used to manage software environment modules on GLiCID. It allows users to load, unload, and list available modules for their computing needs."],
    "what is Compiler?": ["A compiler is a program that translates source code written in a high-level programming language into machine code that can be executed by the computer's processor. On GLiCID, various compilers are available for different programming languages."],
    "what is Micromamba?": ["Micromamba is a package manager for the Conda ecosystem. It is used on GLiCID for managing and installing software packages and dependencies in Conda environments."],
    "what is Apptainer?": ["Apptainer is a containerization tool used on GLiCID for packaging and deploying applications with their dependencies. It provides a lightweight and portable way to run applications in isolated environments."],
    "what is Podman?": ["Podman is a container management tool similar to Docker. It is used on GLiCID for managing containers and container images, allowing users to run, build, and manage containerized applications."],
    "what is Guix?": ["Guix is a package manager and functional package management tool used on GLiCID. It provides a declarative and reproducible way to manage software packages and environments."],
    "bye": ["Goodbye! Please visit GLiCID documentation for more information."],
}

def get_response_glicid(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input matches any predefined responses related to the GLiCID supercomputer
    for key in responses_glicid:
        if user_input in key:
            return random.choice(responses_glicid[key])
    
    # If the user input doesn't match any predefined responses, provide a default response
    return "Sorry, I'm not sure how to help with that. Please check the GLiCID documentation for more information at https://www.glicid.fr."

def chat_glicid():
    print("GLiCID Bot: Hello! I'm here to provide information and assistance related to the GLiCID supercomputing center in Nantes. How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("GLiCID Bot: Goodbye! Please visit GLiCID documentation for more information.")
            break
        response = get_response_glicid(user_input)
        print("GLiCID Bot:", response)

if __name__ == "__main__":
    chat_glicid()

