from django.shortcuts import render
from input.models import Input
from .models import Detection
import torch
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render, redirect

from yolov5.hubconf import _create



def detection_obj(request, pk):

	try:
		last_upload = Input.objects.get(pk=pk)
	except:
		return redirect('/input/')
	try:
		last_detection_id = Detection.objects.latest('id').id
	except:
		last_detection_id = 0

	if last_upload.id > last_detection_id:
		model = _create(name='yolov5s', pretrained=True, channels=3, classes=80, autoshape=True, verbose=True)
		results = model('media/' + str(last_upload.image))
		results_img = Image.fromarray(results.render()[0])

		results_img_io =BytesIO()
		results_img.save(results_img_io, format='PNG')

		image_file = InMemoryUploadedFile(results_img_io, None, str(last_upload.id) + '_detect.png','image/png', results_img_io.getbuffer().nbytes, None)
		pred_str = results.pandas().xyxy[0].name.value_counts().to_string(dtype=False)
		if pred_str == 'Series([], )':
			pred_str = 'Распознанных обектов нет.'
		detection = Detection(list_detection = pred_str)
		detection.image_with_detection_obj.save(str(last_upload.id) + '_detect.png', image_file)

		return render(request, 'detection_page.html', {'detection_obj' : detection, 'pred_str' : pred_str, 'input_img' : last_upload})
	else:
		detection = Detection.objects.get(pk=pk)
		upload_num = Input.objects.get(pk=pk)
		
		return render(request, 'detection_page.html', {'detection_obj' : detection, 'pred_str' : detection.list_detection, 'input_img' : upload_num})



