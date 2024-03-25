# VGG Image Classification

The VGG Image Classification project is a web application developed in Python with the Django framework. It facilitates automatic image classification using the VGG-19 algorithm, providing users with a user-friendly interface to upload images and receive classification results. This README provides comprehensive details on running the project, the structure of the files, and acknowledgments to the contributors.

## Project Description

This project aims to simplify the process of image classification by leveraging the powerful VGG-19 algorithm implemented via TensorFlow Keras. Utilizing pre-trained weights, the application processes images uploaded by users, predicts their classes, and presents the top three predictions with the highest probabilities. Image preprocessing is performed using OpenCV for optimal compatibility and efficiency.

## Running the Project

# DOWNLOAD THE PRETRAINED WEIGHTS AND INCLUDE IT IN THE FOLDER /staticfiles VIA THE LINK : https://drive.google.com/drive/folders/11WizabO4ltvwVofZEHsnmKtFo9XTbo2A

To run the project locally, follow these steps:

1. **Step 1: Create a Virtual Environment**: Set up a Python virtual environment to isolate project dependencies.

2. **Step 2: Install Dependencies**: Activate the virtual environment and install all required packages listed in the `requirements.txt` file using the command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Step 3: Start the Server**: Navigate to the `vgg_19` directory and start the Django development server by running:

   ```bash
   python manage.py runserver
   ```

4. **Step 4: Access the Application**: Open your web browser and go to the provided URL (typically http://localhost:8000) to access the application.

## File Structure

The project directory consists of the following key components:

1. **`staticfiles` Directory**: Contains the VGG-19 model with weights pretrained on ImageNet, essential for image classification.

# DOWNLOAD THE PRETRAINED WEIGHTS AND INCLUDE IT IN THE FOLDER /staticfiles VIA THE LINK : https://drive.google.com/drive/folders/11WizabO4ltvwVofZEHsnmKtFo9XTbo2A

2. **`vgg_19` Directory**: Houses the configuration files and settings for the Django application.

3. **`app` Directory**: Contains the core functionalities of the application:

   - **`templates` Directory**: Stores HTML templates (`classer.html` and `index.html`) styled with Bootstrap for the web interface.

   - **`urls.py`**: Manages URL routing within the application.

   - **`views.py`**: Implements the backend logic of the application, including functions for loading the model, processing images, performing classification, and rendering HTML templates.

## Conclusion

The VGG Image Classification project provides a practical demonstration of utilizing deep learning algorithms for image classification within a web application context. Its intuitive interface and efficient processing, utilizing TensorFlow Keras and OpenCV, make it a valuable tool for various image classification tasks.

---

This README offers an exhaustive description of the VGG Image Classification project, detailing its purpose, installation instructions, file structure, and acknowledgments to the contributors. For further inquiries or collaboration opportunities, please reach out to the author.
