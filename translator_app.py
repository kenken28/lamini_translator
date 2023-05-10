from flask import Flask, redirect, url_for, render_template, request
from lamini_translator import LaminiTranslator

app = Flask(__name__)
translator = LaminiTranslator(config_path='./configure_llama.yaml')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        src_text = request.form['source_text']
        tar_lang = request.form['target_language']
        src_lang, translation = translator.translate(src_text, tar_lang)
        return render_template('index.html',
                               source_text=src_text,
                               target_language=tar_lang,
                               source_language=src_lang,
                               translation=translation,
                               result_visibility='visible')
    else:
        return render_template('index.html',
                               source_text='学而时习之，不亦说乎？\n有朋自远方来，不亦乐乎？',
                               target_language='English',
                               result_visibility='hidden')


@app.route('/<param>/')
def page_not_found(param):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
