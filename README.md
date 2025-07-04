FUN FACT GENERATOR

A Streamlit-based web app that generates interesting, lesser-known fun facts on any topic using OpenAI’s GPT-3.5-turbo model. Enter any topic and instantly receive creative, surprising facts in an easy-to-use interface.

FEATURES:

Enter any topic (e.g., space, music, food)

Generates an interesting, lesser-known fact using GPT-3.5-turbo

Clean, responsive Streamlit interface

Informative prompts for empty inputs

Displays results in a stylish, readable format

HOW IT WORKS:

User enters a topic in the input field.

On clicking Generate Fun Fact, the app sends a prompt to OpenAI’s GPT-3.5-turbo:

arduino
Copy
Edit
"Give me one interesting and lesser-known fun fact about {topic} in one or two sentences."
The model responds with a short, creative fact.

The app displays the result in a clean, styled box.

| Technology        | Purpose                             |
| ----------------- | ----------------------------------- |
| **Python 3.x**    | Core programming language           |
| **Streamlit**     | Building interactive web UI         |
| **OpenAI API**    | GPT-3.5-turbo for text generation   |
| **python-dotenv** | Securely load environment variables |

