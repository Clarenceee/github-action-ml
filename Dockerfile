# Use the TensorFlow Serving base image
FROM tensorflow/serving:latest

# Add custom model to the image
COPY model/img_classifier /models/img_classifier

# Set environment variable to specify the model name
ENV MODEL_NAME=img_classifier

# Expose the default TensorFlow Serving port
EXPOSE 8501
