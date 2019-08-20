from flask import (
    Flask,
    render_template
    request
)
import requests, zipfile, io, os
import connexion
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, load_img
import pandas as pd 
import numpy as np
import os
import json
model = load_model('model13.h5')
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model._make_predict_function()
# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/predict', methods=['GET'])
def diagnose():
    season_id = request.args.get('season_id')
    # season_id.str()
   
    IMAGE_WIDTH=128
    IMAGE_HEIGHT=128
    IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
    IMAGE_CHANNELS=3
    
    path = "http://localhost/app-server/public/api/zip/"
    fullpath = path + season_id
    current_directory = os.getcwd()
    zips_folder = current_directory + "/"+season_id

    r = requests.get(path+farm_id)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(zips_folder)


    # test_filenames = os.listdir("/home/sheila/Desktop/Learning_data_science/crop check/images/test1")
    test_filenames = os.listdir(zips_folder)

    test_df = pd.DataFrame({
        'filename': test_filenames
    })
    nb_samples = test_df.shape[0]

    batch_size=15
    test_gen = ImageDataGenerator(rescale=1./255)
    test_generator = test_gen.flow_from_dataframe(
    test_df, 
    zips_folder, 
    x_col='filename',
    y_col=None,
    class_mode=None,
    target_size=IMAGE_SIZE,
    batch_size=batch_size,
    shuffle=False
    )
    predict = model.predict_generator(test_generator, steps=np.ceil(nb_samples/batch_size))
    9+90

    test_df['category'] = np.argmax(predict, axis=-1)

    d = test_df.to_dict(orient='records')
    j = json.dumps(d)

    # submission_df = test_df.copy()
    # submission_df['id'] = submission_df['filename'].str.split('.').str[0]
    # submission_df['label'] = submission_df['category']
    # submission_df.drop(['filename', 'category'], axis=1, inplace=True)
    # submission_df.to_csv('submission_test1.csv', index=False)
    print(j)

    # return [j[key] for key in sorted(j.keys())]
    return j

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)