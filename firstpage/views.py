from django.shortcuts import render
from django.http import HttpResponse
import ktrain

# Create your views here.

z= ktrain.load_predictor('./models/bert')
model = ktrain.get_predictor(z.model, z.preproc)

# reloadModel = joblib.load('./models/bert')

def index(request):
	context = {'a' : "Hello"}
	return render(request, 'index.html', context)
	# return HttpResponse({'a' : 1})

def predictNews(request):
	if request.method=="POST":
		print(request.POST.dict())
		news = request.POST.get('news')
		result = model.predict(news)
		print(result)
		if(result == '0'):
			answer = "FALSE"
		elif(result == '1'):
			answer = "TRUE"
	context = {'a' : answer}
	return render(request, 'index.html', context)