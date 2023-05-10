# Lamini Translator

This is a simple translator application built with [lamini-ai's LLM engine](https://github.com/lamini-ai/lamini), a demo for this application is available [here](https://translator.xuyuxin28.com/).

## Setup your own translator
- Clone the repository and navigate to the repository folder.
```console
git clone https://github.com/kenken28/lamini_translator.git
cd lamini_translator
```
- Create a virtual environment with `python3.9`, and install the dependent packages.
```console
python3.9 -m venv 'translator_venv'
source translator_venv/bin/activate
pip install -r requirements.txt
```
- Create an account at https://lamini.ai, as you will need an API key to use the `lamini` package. Go to your account page and copy the API key.
- Create a yaml config file with `$ touch configure_llama.yaml` and put your key in it like so:
```yaml
production:
    key: "<YOUR-KEY-HERE>"
```
- Now you can run your translator locally on a Flask application.
```console
flask --app translator_app.py
```
