from roboflow import Roboflow

rf = Roboflow(api_key="lF2h2K4AoCyUyvxH0j7J")
dataset = rf.workspace("pozi-vlunk").project("coat-wzayv").version(1).download("yolov5", location="D:/Магистратура учеба/Проекты с Ромой/Проект по одежде/Fashion project/dataset/coat/")