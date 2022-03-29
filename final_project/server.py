#import machinetranslation
from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = english_to_french(textToTranslate).get('translations')[0].get('translation')
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return french_to_english(textToTranslate).get('translations')[0].get('translation')  

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

