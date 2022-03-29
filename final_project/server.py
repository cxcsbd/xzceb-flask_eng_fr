import machinetranslation
# from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = english_to_french(textToTranslate).get('translations')[0].get('translation')
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = french_to_english(textToTranslate).get('translations')[0].get('translation')
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    '''code to render index.html template'''
    return render_template(index.html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
#    app.run(host="127.0.0.1", port=8080)
