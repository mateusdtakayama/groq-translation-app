[PYTHON__BADGE]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[STREAMLIT__BADGE]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[FASTAPI__BADGE]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[GOOGLEAPI__BADGE]: https://img.shields.io/badge/Google%20API-4285F4?style=for-the-badge&logo=google&logoColor=white
[GROQ__BADGE]: https://img.shields.io/badge/GROQ-00BFFF?style=for-the-badge&logo=graphql&logoColor=white

<h1 align="center" style="font-weight: bold;">Translation API and App</h1>

![python][PYTHON__BADGE]
![streamlit][STREAMLIT__BADGE]
![fastapi][FASTAPI__BADGE]
![googleapi][GOOGLEAPI__BADGE]
![groq][GROQ__BADGE]

<p align="center">
 <a href="#about">About</a> • 
 <a href="#started">Getting Started</a> • 
 <a href="#colab">Collaborators</a>
</p>

<h2 id="about">📌 About</h2>

This repository contains two applications: 

1. **Translation App**: Built with Streamlit, this application uses the GROQ API to translate text into different languages. Users can input text and receive translations in both formal and informal styles.

2. **Translation Server**: Developed using FastAPI, this server interacts with the same GROQ API to provide translation services. It is designed to handle requests and return translations in a straightforward manner.

<h2 id="started">🚀 Getting Started</h2>

<h3>Prerequisites</h3>

Ensure you have the following installed:

- [Python 3.x](https://www.python.org/)
- [Git](https://git-scm.com/)

<h3>1. Cloning the Repository</h3>

Clone the project repository to your local machine:

```bash
git clone https://github.com/mateusdtakayama/groq-translation-app
cd groq-translation-app
```

<h3>2. Setting Up a Virtual Environment</h3>

It's recommended to use a virtual environment to manage your project dependencies. Follow these steps:

2.1 Create a virtual environment:

```bash
python -m venv venv
```

2.2 Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Configuring the GROQ API Key

To utilize GROQ services in this project, you'll need to configure your GROQ API key. Follow these steps to set it up:

#### 3.1 Obtain Your GROQ API Key

Sign up and obtain your API key from the GROQ API provider.

#### 3.2 Store the API Key Securely

In your project directory, create a `.env` file if it doesn't already exist.

Add your API key to the `.env` file in the following format:

```bash
GROQ_API_KEY=your-groq-api-key-here
```

<h3>4. Starting</h3>

4.1 Install dependencies

```bash
pip install -r requirements.txt
```

4.2 Start the Translation Application

To run the translation application, which uses the `app.py` script, execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit application and open it in your default web browser, allowing you to interact with the translation features.

4.3 Start the Translation Server

To run the FastAPI server, which uses the serve.py script, execute the following command:

```bash
python3 serve.py
```

This will start the FastAPI server, and you can interact with it through the /chain endpoint.

<h2 id="colab">🤝 Collaborator</h2>

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/104940896?s=400&u=71304eae379288b6ebce80280cd13a6a474de2ea&v=4" width="100px;" alt="Mateus Delai Takayama Profile Picture"/><br>
        <sub>
          <b>Mateus Delai Takayama</b>
        </sub>
      </a>
    </td>
  </tr>
</table>