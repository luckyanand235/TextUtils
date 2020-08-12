# Created File
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
# 	return HttpResponse("<h1>Hello Lucky</h1> <a href='http://luckyanand235.github.io'>Resume</a>")

# def about(request):
# 	return HttpResponse("About Lucky")

def index(request):
	return render(request, 'index.html')

	# return HttpResponse("Home")


def analyze(request):
	# Get the text 
	djtext = request.POST.get('text', 'default')

	# check the checkbox value
	removepunc = request.POST.get('removepunc', 'off')
	fullcaps = request.POST.get('fullcaps', 'off')
	newlineremover = request.POST.get('newlineremover', 'off')
	extraspaceremover = request.POST.get('extraspaceremover', 'off')
	# check if check box value is on
	if removepunc == 'on':
		punctuations = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
		analyzed = ""
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char


		params = {'purpose' : 'Removed Punctuations', 'analyzed_text': analyzed}
	# analyze this text
		return render(request, 'analyze.html', params)
	
	elif fullcaps == 'on':
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		
		params = {'purpose' : 'Changed to upper case', 'analyzed_text': analyzed}
		return render(request, 'analyze.html', params)

	elif newlineremover == 'on':
		analyzed = ""
		for char in djtext:
			if char != "\n" and char !="\r":
				analyzed = analyzed + char


		params = {'purpose' : 'Removed New lines', 'analyzed_text': analyzed}
	# analyze this text
		return render(request, 'analyze.html', params)

	elif extraspaceremover == 'on':
		analyzed = ""
		for index, char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index + 1] == " "):
				analyzed = analyzed + char


		params = {'purpose' : 'Removed New lines', 'analyzed_text': analyzed}
	# analyze this text
		return render(request, 'analyze.html', params)
	else:
		return HttpResponse("Error")




