import csv
import random

# Example data to generate synthetic research papers
titles = [
    "Deep Learning for NLP", "Machine Learning for Healthcare", "AI in Robotics", 
    "NLP in Social Media", "Computer Vision and its Applications", 
    "Blockchain in Finance", "Natural Language Processing Techniques", 
    "AI in Healthcare", "Quantum Computing for Beginners", "Big Data Analytics"
]

authors = [
    "John Doe", "Jane Smith", "Tom Brown", "Alice Johnson", 
    "Robert Lee", "Emily Clark", "William White", "Sophia Harris", 
    "James Taylor", "Linda Garcia"
]

keywords = [
    "deep learning, NLP", "machine learning, healthcare", "AI, robotics", 
    "NLP, social media", "computer vision, applications", "blockchain, finance", 
    "NLP, machine learning", "AI, healthcare", "quantum computing", "big data"
]

abstracts = [
    "This paper explores deep learning techniques in natural language processing...",
    "Machine learning applications in healthcare, including diagnosis and treatment...",
    "The role of AI in robotics, focusing on autonomous systems...",
    "This research focuses on NLP techniques applied to social media data...",
    "Computer vision methods for various real-world applications in industries...",
    "Blockchain technology's potential in the finance sector, focusing on security...",
    "This paper discusses recent advancements in NLP and its integration with AI...",
    "AI-driven healthcare solutions and their impact on diagnosis and patient care...",
    "Introduction to quantum computing and its future implications in various fields...",
    "Analyzing the significance of big data in the modern business landscape..."
]

# Number of research papers to generate
num_papers = 100

# Create and write the CSV file
with open('researchpapers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Title", "Authors", "Keywords", "Abstract"])
    
    # Generate research papers
    for _ in range(num_papers):
        title = random.choice(titles)
        author = random.choice(authors)
        keyword = random.choice(keywords)
        abstract = random.choice(abstracts)
        
        # Write a row in the CSV file
        writer.writerow([title, author, keyword, abstract])

print(f"{num_papers} research papers generated and saved to 'researchpapers.csv'.")
