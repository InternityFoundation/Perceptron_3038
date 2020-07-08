# Deep-learning-with-opencv

###### Steps:
- Capturing faces from the training video using haarcascode_frontalface_default.xml
face_detection.py

- Created the 128-d embeddings for each face in the dataset and stored it in eci.picke file
Encoding_dataset_into_different_folders.py

- Using the 128-d embedding i.e. feature vectors compared the images and cluster them into different folders.
final_encoding.py

- Updated the pickle file and stored it in emb.picke file 
getting_dataset_ready.py

- Using these embeddings to recognize the faces of the characters in video streams.
recognition.py
