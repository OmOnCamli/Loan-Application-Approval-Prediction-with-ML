# Loan-Application-Approval-Prediction-with-ML
Comparison of the performance of 10 different machine learning models trained with synthetic data and data obtained from Kaggle.com after preprocessing (removal of irrelevant or low-information features), selection of the best-performing model, deployment as a service, and making predictions.

## Steps To Follow

1. data.ipynb isimli jupyter notebook dosyasındaki hücreyi çalıştırın ve data.csv'yi üretin.

2. ml_models.ipynb  isimli jupyter notebook dosyasındaki hücreyi çalıştırın ve data.csv ile eğitilen 10 ML modeli arasındaki Accuracy değeri en yüksek olan modeli best_ml_model.joblib olarak kaydedin.

3. Tüm dosyaları tek bir klasörde toplayın ve terminalde "cd" komutu ile bu dizine gidin. ( cd path/to/your/project )

4. loan_prediction.py isimli python dosyasını açın. best_ml_model.joblib 'i kullanarak tahminleme yapabilmek için terminale "streamlit run loan_prediction.py" yazın ve enter'a tıklayın.

5. Uygulama tarayıcı üzerinde açıldıktan sonra tahminleme yapabilirsiniz.
