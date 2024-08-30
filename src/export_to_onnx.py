from ultralytics import YOLO

# yolov8s_model = YOLO('yolov8s_1280/weights/best.pt')
# # Export the model to onnx
# yolov8s_model.export(format='onnx', nms=True, imgsz=1280, opset=12)

yolov8n_model = YOLO('yolov8n_1280/weights/best.pt')
# Export the model to onnx
yolov8n_model.export(format='onnx', nms=True, imgsz=1280, opset=12)
