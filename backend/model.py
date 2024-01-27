from tensorflow.keras.models import load_model

# Specify the complete file path including the filename
model_path = r".\CNNRNN_Model2.h5"

# Save the model
CNNRNN_Model2.save(model_path)

from PIL import Image
import numpy as np
from skimage.transform import resize
from tensorflow.keras.models import load_model

def predict_image(classifier, image):
    # Resize the image to the expected size (30x30x30) and convert it to RGB
    resized_image = resize(image, (30, 30, 30))
    rgb_image = np.stack((resized_image,) * 3, axis=-1)

    # Normalize the image
    normalized_image = rgb_image / 127.5 - 1

    # Use the model to predict the image class
    class_probabilities = classifier.predict(np.expand_dims(normalized_image, axis=0))

    # Return the predicted class probabilities
    return class_probabilities


# Load the image
image = Image.open(r"C:\Users\Rahul\Desktop\Thumbs_up_and_down_Dataset\val\WIN_20180907_16_07_10_Pro_Thumbs Down_new\WIN_20180907_16_07_10_Pro_00034.png")
# Convert the image to a NumPy array
image_array = np.array(image)

# Load the model
imported_model = load_model(r"C:\Users\Rahul\Desktop\MODELS\CNNRNN_Model2.h5")

# Now you can use the imported model
predictor = predict_image(imported_model, image_array)
print(predictor)


# Extract probabilities for classes 3 and 4
class_3_prob = predictor[0][3]
class_4_prob = predictor[0][4]

# Check which class has the maximum probability
if class_3_prob > class_4_prob:
    print("Class 3 has the maximum probability.")
elif class_4_prob > class_3_prob:
    print("Class 4 has the maximum probability.")
else:
    print("Both classes 3 and 4 have the same probability.")

