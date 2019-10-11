from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import RecordForm
from .models import Record



def upload_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('record_list')
    else:
        form = RecordForm()
        return render(request, 'myfirstapp/upload_record.html/',
                      {'form': form})

def record_list(request):
    records = Record.objects.all()
    return render(request, 'myfirstapp/record_list.html/',
                  {'records': records})



class RecordListView(ListView):
    queryset = Record.objects.order_by('list')
    template_name = 'myfirstapp/class_record_list.html/'
    context_object_name = 'records'



class RecordUpdateView(UpdateView):
    model = Record
    fields = ['title', 'category', 'description', 'list', 'picture']
    template_name = 'myfirstapp/class_record_update.html/'



class RecordDetailView(DetailView):
    model = Record
    template_name = 'myfirstapp/class_record_detail.html/'
    context_object_name = 'record'



class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'myfirstapp/class_record_delete.html/'
    context_object_name = 'record'
    success_url = reverse_lazy('class_record_list')










