def predict(image_path, model, encoder):
  image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  resized = cv2.resize(image, image_shape[:2])
  prediction = model.predict(resized.reshape(-1, img_size, img_size, img_dimension))
  label_encoded = [np.argmax(prediction)]
  label = encoder.inverse_transform(label_encoded)[0]
  print("Predicted label: ",label)
  cv2_imshow(image)
