


# assumptions that i have made about the input file if the file is empty,
# there will be no output file genrated. if input file has invalid city 
# names ,the output file will say invalid city name for that respective city.

from flask import Flask, request
from flask import render_template
from werkzeug.utils import secure_filename
import geocoding as gc
import os

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

#api route for uploading the input file
@app.route("/file",methods=['POST'])
def upload_file():
    if request.method=='POST':
        file=request.files['file']
        file.save(secure_filename('input.txt'))
        res=gc.compute()
        file.close()
        if(res):
            return render_template('output.html')
        if os.path.exists('output.txt'):
            os.remove('output.txt')
    return render_template('error.html')
       
    

   