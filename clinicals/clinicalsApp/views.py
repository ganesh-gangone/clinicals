from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from clinicalsApp.models import *
from clinicalsApp.forms import ClinicalDataForm
from django.urls import reverse_lazy
# Create your views here.
class PatientListView(ListView):
    model = Patient
class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstname','lastname','age')

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstname','lastname','age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')
    

def addclincaldata(request,**kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/addclinicaldata.html',{'form':form,'patient':patient})

def analyze(request,**kwargs):
    data = ClinicalData.objects.filter(patient_id = kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentname == 'hw':
            h_and_w = eachEntry.componentvalue.split('/')
            if len(h_and_w) > 1:
                hgt_to_ft = float(h_and_w[0])*0.4536
                BMI = float(h_and_w[1])/(hgt_to_ft * hgt_to_ft)
                bmiEntry = ClinicalData()
                bmiEntry.componentname = 'BMI'
                bmiEntry.componentvalue = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request,'clinicalsApp/report.html',{'data':responseData})