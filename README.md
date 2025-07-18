# ♻️ RecycleVision – Waste Image Classifier

RecycleVision is an AI-powered web application that helps users identify waste as **Recyclable**, **Compostable**, or **Non-Recyclable** by simply uploading an image. It leverages the **Clarifai General Image Recognition API** and is built using **Streamlit** for a clean and intuitive interface.

## 🌍 SDG Alignment
Aligned with **United Nations Sustainable Development Goal 12 (SDG 12): Responsible Consumption and Production**, RecycleVision promotes better waste disposal awareness.

---

## 🔧 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **AI API**: Clarifai Pre-trained General Model  
- **Libraries**: Streamlit, PIL, Requests, OS, IO

---

## 🚀 Features

- Upload image of waste item (JPG, PNG, JPEG)  
- Automatically classifies waste into:  
  - ♻️ Recyclable  
  - 🌿 Compostable  
  - 🚯 Non-Recyclable  
- Simple, fast, and accurate  
- No machine learning training required  

---

## 🗂️ Project Structure

RecycleVision/
├── app/
│ └── app.py
├── src/
│ ├── predict.py
│ └── category_mapper.py
├── static/
│ └── temp.jpg
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/your-username/RecycleVision.git
cd RecycleVision

2.Install dependencies
pip install -r requirements.txt

3.Run the Streamlit app
streamlit run app/app.py



API Configuration
This project uses the Clarifai API. To use it:

Create a free account on Clarifai

Generate a PAT (Personal Access Token)

Add the token in src/predict.py where indicated



Example Use Case
Upload image of a plastic bottle → App returns: Recyclable

Upload image of a banana peel → App returns: Compostable



Model Info
Model Used: Clarifai General Image Recognition Model

No Training Required: Uses pre-trained model from Clarifai

Accuracy: 85–98% confidence range based on tests

Speed: Response within 2 seconds