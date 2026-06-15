# AI-Powered E-Commerce CRM System

An Intelligent CRM system for E-Commerce with Machine Learning integration. Built as a Final Year Project.

### **🚀 Key Features**
- **Customer Management**: Complete CRUD operations for customer data
- **AI Churn Prediction**: ML model to predict customers likely to leave
- **Sentiment Analysis**: Analyze customer feedback using TF-IDF + NLP
- **Sales Dashboard**: Real-time analytics and charts with Chart.js
- **Order & Inventory Tracking**: Manage orders, products, and stock levels

### **🛠️ Tech Stack**
- **Backend**: Python, Django
- **Machine Learning**: Scikit-learn, Pandas, TF-IDF Vectorizer
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **Database**: SQLite3
- **Charts**: Chart.js

### **🤖 ML Models Included**
1. `tfidf_vectorizer.pkl` - Text vectorization for sentiment analysis
2. `churn_features.csv` - Dataset for churn prediction model
3. `customer_messages.csv` - Customer feedback data

### **⚡ How to Run Locally**
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
