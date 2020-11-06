Tutorial for run programming:

Step 1: 
          Find out database covering face_images
Step 2; 
          Create 2 forder : image (for training ) and image_output_1 (for test)
          copy images into 2 forder with the rate 80-20
Step 3:
 
          Run for training - Run in command line of WINDOWN
          python training_embeddings.py
          waiting for train with times similiar 5 minute
Step 4:   
          Run for test
          python face-recognition.py
          Note (change direction when load file training  "C:/Users/admin/Desktop/face-recognition-cnn-master/embeddings.npy"  line 113 in code. )

*Note: 
       + khi traning voi 1 image/class  -- 2 images/class -- 3  images/class -4 images/class -- 5 images/class -- 6 images/class. 
         4 images/class have accurately highest.  
       +  with many more image/classes to trainng over 4 then accurately less tend.  --- meaning of META LEARNING.
