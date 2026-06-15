from django.shortcuts import render, redirect
from .forms import CustomerForm, MessageForm, ChurnFeatureForm, PurchaseForm
from .models import Customer, ProductPurchase, CustomerMessage, ChurnFeature
from .forms import MessageForm
import joblib
import os
from django.conf import settings
import csv


def base(request):
    return render(request, 'crm/base.html')

tfidf = joblib.load(r"crm\ml_models\tfidf_vectorizer.pkl")
sentiment_model = joblib.load(r"crm\ml_models\sentiment_model.pkl")

def predict_sentiment(request):
    sentiment = ''
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['message_text']
            vector = tfidf.transform([text])
            pred = sentiment_model.predict(vector)[0]
            sentiment = pred
    else:
        form = MessageForm()
        
    return render(request, 'crm/predict_sentiment.html', {'form': form, 'sentiment': sentiment})

def dataset_view(request):
    dataset_path = os.path.join(settings.MEDIA_ROOT, 'ecommerce_datasets', 'customer_messages.csv')

    data = []

    try:
        with open(dataset_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        data = None

    return render(request, 'crm/dataset.html', {'data': data})


# Add Customer
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomerForm()
    return render(request, 'crm/add_customer.html', {'form': form})

# Add Message
def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MessageForm()
    return render(request, 'crm/add_message.html', {'form': form})

# Add Churn Feature
def add_churn_feature(request):
    if request.method == 'POST':
        form = ChurnFeatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ChurnFeatureForm()
    return render(request, 'crm/add_churn.html', {'form': form})

# Add Purchase
def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PurchaseForm()
    return render(request, 'crm/add_purchase.html', {'form': form})

# Generic success page
def success(request):
    return render(request, 'crm/success.html')


def view_customers(request):
    customers = Customer.objects.all()
    return render(request, 'crm/view_customers.html', {'customers': customers})

def view_messages(request):
    messages = CustomerMessage.objects.all()
    return render(request, 'crm/view_messages.html', {'messages': messages})

def view_purchases(request):
    purchases = ProductPurchase.objects.all()
    return render(request, 'crm/view_purchases.html', {'purchases': purchases})

def view_churn_features(request):
    churn_data = ChurnFeature.objects.all()
    return render(request, 'crm/view_churn.html', {'churn_data': churn_data})
