# Nutrition Search Tool

Nutrition information is critical information for general health upkeep, especially for individuals suffering from Type 1 and Type 2 diabetes who continuously monitor their blood glucose concentration. The Big Ideas Lab at Duke is coming up with lots of tools to help nutritionists, clinicians, and individuals use general technology, wearable devices, and machine learning to improve health. This nutrition search tool builds on Joshua D'Arcy's food2vec tool that uses word embeddings from the Google  News Corpus to estimate nutrition information based on cosine similarity.


This is a search engine for nutrition information of food items. Its backend is a python API running on a Google server through Flask. Upon submitting a search for a food item, the request is relayed to the server, which retrieves the food item's nutrition information. If the food item(s) cannot be narrowed down to one time, the server will retrieve nutrition information for all the most similar items. If the item does not exist and there are no highly similar items, an error message will be displayed.

To power up the server, this tutorial was followed. Joshua D'Arcy's food2vec code was downloaded, and all instructions to kick start the project were followed. Four extra files: app.yaml, main.py, requests.text, and actualAPI.py were needed to power-up the server, and a simple .html file is used to display the webpage.
