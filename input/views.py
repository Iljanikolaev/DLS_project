from django.shortcuts import render
from django import forms
from .models import Input
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

'''
class InputList(ListView):

	model = Input
	template_name = 'input.html'
	context_object_name = 'input'
	#paginate_by = 10

	def get_context_data(self, *, objects_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Изображения'
		return context
'''


def load_images(request):

	if request.method == 'POST':
		form_img = InputForm(request.POST, request.FILES)
		if form_img.is_valid():
			saving = form_img.save()
			return redirect('detection', pk=saving.pk)
		else:
			messages.error(request, 'Файл не является изображением.')
			return redirect('/input/')
	else:
		form_img = InputForm(request.POST, request.FILES)
		with open('classes.txt', encoding = 'utf-8', mode = 'r') as classes_txt:
			classes = classes_txt.read()

		return render(request, 'input_page.html', {'form_img' : form_img, 'classes' : classes})


class InputForm(forms.ModelForm):
	image = forms.ImageField(required=False, label  = 'Изображение' )
	class Meta:
		model = Input
		fields = ['image']



