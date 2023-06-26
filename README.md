## Emoji-Based-Hate-Speech-Detection-on-Social-Media
This project focuses on enhancing hate speech detection for emoji-based hate speech on social media.
To complete this project we will need the following steps:
### Scraped raw social media messages
We mainly focus on scraping social media messages from TikTok and YouTube.
This process contains in the folder **Crawling_Data/**.
### Annotation scheme
The process of annotation had been done by two annotators, so the document annotation guide is needed, and it is in **Readme/ Social_Media_Comments_Annotation_Guide.pdf**. After that, we could explore the statistic result of annotation agreement in **Annotation/annotation_agreement.ipynb** as well as any interesting statistic of data in **Analysis_Data/stats.ipynb**.
#### Dataset
In this **Dataset/** folder we could find all the data used to build a model. This folder consists of three different subfolders **Annotation_Dataset/** which contain the new final data that have been scraped, and annotated. **Kirk_Dataset/** contains the dataset from Kirk, Hannah et al. (July 2022), and **Raw_Dataset/**.
### Train Model
#### Train Machine Learning Model
Every machine learning training model has been done in **Test_models/** folder. This folder also consists of the model-trained file as well.
#### Train Deep Learning Model
This process has been done in **Training_deep_model/**. This folder consists of 3 files in order to train the binary model, and multiclass model(for different types of messages), and we could test the model prediction for new messages in **Training_deep_model/test_binary_model.ipynb**.
### Model
Every trained model and other needed model such as FastText pre-trained embedding model have been put in this **Model/** folder. However, some model files are too big so we cannot put them all in this GitHub but we could find them in this drive https://drive.google.com/drive/folders/1QxCGA8utdAZNqD8bzA90FJuImKL4UUYh?usp=sharing.
### Project Report
Additionally, we could find our report document at this link https://www.overleaf.com/7996372421xcnmbnkwryrp.
