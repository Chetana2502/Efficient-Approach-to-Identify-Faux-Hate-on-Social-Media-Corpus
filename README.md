# An Efficient Approach to Identify Faux Hate on Social Media Corpus

## 📌 Project Overview
Hate speech detection on social media has become a critical task due to the rapid spread of harmful and offensive content. While modern deep learning models are effective at identifying explicit hate speech, they often struggle to distinguish **faux hate** — strongly worded, sarcastic, or emotionally charged language that does not target protected groups or promote discrimination.

This project proposes an **ensemble-based, context-aware approach** to accurately identify real hate speech while reducing false positives caused by faux hate. By combining multiple transformer-based language models and applying confidence-aware decision logic, the system aims to improve fairness, interpretability, and reliability in automated content moderation.

---

## 🎯 Objectives
- Detect hate speech in social media text with high precision and recall  
- Minimize false positives caused by faux hate  
- Capture contextual, semantic, and intent-based cues rather than relying on keywords  
- Evaluate multiple transformer models and their ensemble performance  
- Design a modular and scalable detection pipeline suitable for real-world moderation  

---

## 🧠 Key Concepts
- **Hate Speech**: Language targeting individuals or groups based on protected characteristics such as race, religion, gender, or ethnicity.
- **Faux Hate**: Aggressive or offensive language that mimics hate speech but lacks discriminatory intent and targets actions, ideologies, or behaviors instead.
- **Ensemble Learning**: Combining predictions from multiple models to improve robustness and reduce misclassification.

---

## 🏗️ System Architecture
The system follows a modular pipeline:

1. **Data Collection**
   - Social media text collected from platforms such as Twitter (X), Reddit, YouTube, blogs, and forums
   - Only publicly available content is used

2. **Preprocessing**
   - Text normalization and cleaning
   - Noise removal (URLs, symbols, excessive punctuation)
   - Preservation of contextual and emotional cues
   - Minimal normalization to retain sarcasm and intent

3. **Model Inference**
   - Fine-tuned transformer-based models:
     - DistilBERT
     - RoBERTa
     - XLM-RoBERTa
     - LaBSE
   - Each model independently predicts hate or non-hate labels

4. **Ensemble Decision Module**
   - Aggregation of predictions using decision-level strategies
   - Confidence-aware logic to handle borderline faux-hate cases

5. **Output**
   - Final hate / non-hate classification
   - Optional confidence scores for interpretability

---

## 📊 Dataset Description
- ~8,600 curated text samples
- Collected from multiple social media platforms
- Includes explicit hate, neutral content, and faux hate cases
- Annotated manually based on intent, target, severity, and context
- Designed to reflect real-world language including sarcasm, slang, and emotional expression

---

## ⚙️ Technologies Used
- **Programming Language**: Python  
- **Libraries & Frameworks**:
  - Transformers (HuggingFace)
  - PyTorch
  - Scikit-learn
  - Pandas, NumPy
  - Selenium (for data scraping)
- **Models**:
  - DistilBERT
  - RoBERTa
  - XLM-RoBERTa
  - LaBSE

---

## 📈 Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  

Special emphasis is placed on reducing **false positives**, particularly for faux hate cases.

---

## 🔒 Ethical Considerations
- Only publicly available data is used
- No personally identifiable information (PII) is stored or shared
- The system is designed to support moderation, not replace human judgment
- Focus on fairness and freedom of expression

---

## 🚀 Future Enhancements
- Multilingual and multimodal hate detection (text + image/video)
- Conversational context modeling
- Explainability modules for model decisions
- Real-time API deployment for moderation systems

---

## 👩‍💻 Author
**Chetana Muddulur**, **Keerthi V T**, **Muktha S Patil**, **Preethi D**

Computer Science & Engineering  
JSS Academy of Technical Education, Bengaluru  

---

## 📜 License
This project is developed for academic and research purposes as part of a major project submission.
