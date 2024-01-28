from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

from ultralytics import YOLO
model = YOLO('yolov8n.pt')
source = r"..\images\1.png"
results = model(source)  # list of Results objects
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs

finalnum = []

for r in boxes:
    # Get the class IDs tensor for this result
    class_ids = r.cls

    # Get the bounding boxes for this result
    bounding_boxes = r.xyxy

    # Filter indices where the class ID corresponds to "person"
    person_indices = (class_ids == 0).nonzero(as_tuple=True)[0]

    # Extract bounding boxes for the "person" class
    person_boxes = bounding_boxes[person_indices]

    # Check if there are any detections of the "person" class with proper tensor
    if person_boxes.size(0) > 0:
        # Extract the first row of the tensor with proper results
        person_box = person_boxes[0]
        x1 = int(person_box[0])
        y1 = int(person_box[1])
        x2 = int(person_box[2])
        y2 = int(person_box[3])
        picture = Image.open(r"..\images\1.png")
        cropped_image = picture.crop((x1,  y1,  x2, y2))
        # cropped_image.show()
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load the model
        model = load_model(r"..\keras_model.h5", compile=False)

        # Load the labels
        class_names = open(r"..\labels.txt", "r").readlines()

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        image = cropped_image.convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        # print("Confidence Score:" , confidence_score)
        # print(" ")
        class_name_var = (class_name[2:], end="")
        if "Up" in class_name_var:
                finalnum[0] += 1
        else:
                finalnum[1] += 1
print(finalnum)       