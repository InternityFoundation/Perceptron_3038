Deep-learning-with-opencv
This repository consist of deep learning approach towards computer vision.
Steps:
1)Capturing faces from the training video using haarcascode_frontalface_default.xml
https://github.com/InternityFoundation/Perceptron_3038/blob/master/Sprint%20Cycles/Navjot%20Singh/Image%20Clustering/face_detection.py
2)Created the 128-d embeddings for each face in the dataset and stored it in eci.picke file 
https://github.com/InternityFoundation/Perceptron_3038/blob/master/Sprint%20Cycles/Navjot%20Singh/Image%20Clustering/Encoding_dataset_into_different_folders.py
3)Using the 128-d embedding i.e. feature vectors compared the images and cluster them into different folders.
https://github.com/InternityFoundation/Perceptron_3038/blob/master/Sprint%20Cycles/Navjot%20Singh/Image%20Clustering/final_encoding.py
4)Updated the pickle file and stored it in emb.picke file 
https://github.com/InternityFoundation/Perceptron_3038/blob/master/Sprint%20Cycles/Navjot%20Singh/Image%20Clustering/getting_dataset_ready.py
4)Using these embeddings to recognize the faces of the characters in both images and video streams
https://github.com/InternityFoundation/Perceptron_3038/blob/master/Sprint%20Cycles/Navjot%20Singh/Image%20Clustering/recognition.py
