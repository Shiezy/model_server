# from datetime import datetime
# from keras.models import load_model
# from keras.preprocessing import image
# from keras.preprocessing.image import ImageDataGenerator, load_img
# import pandas as pd 
# import numpy as np
# import os
# import json
# model = load_model('model13.h5')
# model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
# model._make_predict_function()

# def get_timestamp():
#     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# # Data to serve with our API
# PEOPLE = {
#     "Farrell": {
#         "fname": "Doug",
#         "lname": "Farrell",
#         "timestamp": get_timestamp()
#     },
#     "Brockman": {
#         "fname": "Kent",
#         "lname": "Brockman",
#         "timestamp": get_timestamp()
#     },
#     "Easter": {
#         "fname": "Bunny",
#         "lname": "Easter",
#         "timestamp": get_timestamp()
#     }
# }

# # Create a handler for our read (GET) people
# def read():
#     """
#     This function responds to a request for /api/people
#     with the complete lists of people

#     :return:        sorted list of people
#     """
#     # Create the list of people from our data
#     return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

# # def diagnose():
# #     IMAGE_WIDTH=128
# #     IMAGE_HEIGHT=128
# #     IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
# #     IMAGE_CHANNELS=3
# #     model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# #     # test_filenames = os.listdir("/home/sheila/Desktop/Learning data science/crop check/images/test1")
# #     # # Create the list of people from our data
# #     # return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

# def diagnose():
#     IMAGE_WIDTH=128
#     IMAGE_HEIGHT=128
#     IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
#     IMAGE_CHANNELS=3

#     test_filenames = os.listdir("/home/sheila/Desktop/Learning_data_science/crop check/images/test1")

#     test_df = pd.DataFrame({
#         'filename': test_filenames
#     })
#     nb_samples = test_df.shape[0]

#     batch_size=15
#     test_gen = ImageDataGenerator(rescale=1./255)
#     test_generator = test_gen.flow_from_dataframe(
#     test_df, 
#     "/home/sheila/Desktop/Learning_data_science/crop check/images/test1/", 
#     x_col='filename',
#     y_col=None,
#     class_mode=None,
#     target_size=IMAGE_SIZE,
#     batch_size=batch_size,
#     shuffle=False
#     )
#     predict = model.predict_generator(test_generator, steps=np.ceil(nb_samples/batch_size))
#     9+90

#     test_df['category'] = np.argmax(predict, axis=-1)

#     d = test_df.to_dict(orient='records')
#     j = json.dumps(d)

#     submission_df = test_df.copy()
#     submission_df['id'] = submission_df['filename'].str.split('.').str[0]
#     submission_df['label'] = submission_df['category']
#     submission_df.drop(['filename', 'category'], axis=1, inplace=True)
#     submission_df.to_csv('submission_test1.csv', index=False)
#     print(j)

#     # return [j[key] for key in sorted(j.keys())]
#     return test_df

