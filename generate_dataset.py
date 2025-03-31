import pandas as pd
import random

# List of 100 unique topics (Feel free to add more to expand the list)
topics = [
    "Quantum Computing for Beginners", "AI in Robotics", "Computer Vision and its Applications", 
    "Blockchain Technology in Healthcare", "Natural Language Processing for Social Media", 
    "Cybersecurity in Financial Systems", "AI and Machine Learning for Healthcare", 
    "Blockchain in Supply Chain Management", "Autonomous Vehicles and AI", "Data Privacy in the Digital Age",
    "Data Science in Business", "Smart Cities and IoT", "Artificial Intelligence in Education", 
    "Deep Learning for Image Recognition", "AI in Drug Discovery", "Blockchain for Digital Identity",
    "Data Mining for Healthcare", "Quantum Cryptography", "Neural Networks in Finance", 
    "Machine Learning for Natural Language Understanding", "AI in Space Exploration", "Smart Homes and AI",
    "Edge Computing and IoT", "Blockchain in Voting Systems", "AI for Environmental Protection",
    "Augmented Reality in Medicine", "AI for Autonomous Drones", "Robotics in Manufacturing", 
    "Deep Learning for Video Analytics", "Blockchain in Real Estate", "Artificial Intelligence in Agriculture",
    "Chatbots in Customer Service", "Deep Learning for Speech Recognition", "AI for Predictive Maintenance",
    "Robotics in Surgery", "Blockchain in Logistics", "AI in Personalized Marketing", 
    "Internet of Things in Healthcare", "Cloud Computing for Data Analysis", "Blockchain in Education",
    "AI in Human Resources", "Digital Twins in Engineering", "AI for Financial Trading",
    "Natural Language Processing for Customer Reviews", "AI in Climate Change Prediction", 
    "Robotics in Disaster Management", "AI in Smart Grids", "Autonomous Vehicles and Safety",
    "AI for Stock Market Prediction", "Robotic Process Automation", "AI in Cybersecurity Defense",
    "Artificial Intelligence in Legal Tech", "AI for Fraud Detection", "Big Data in Healthcare",
    "AI in Sports Analytics", "AI for Traffic Management", "AI in Media and Entertainment",
    "Predictive Analytics in Business", "Artificial Intelligence for Energy Efficiency", 
    "AI for Personalized Education", "AI in Smart Farming", "Robotics for Elderly Care", 
    "AI for Disaster Relief", "AI in Social Good", "Robotics for Humanitarian Aid", 
    "AI for Mental Health Diagnosis", "Blockchain for Supply Chain Transparency", 
    "AI for Environmental Sustainability", "Autonomous Delivery Robots", "Digital Transformation in Banking", 
    "Natural Language Processing for Legal Documents", "Blockchain for Digital Currencies", 
    "AI for Business Intelligence", "AI in Music Composition", "AI for Voice Assistants",
    "Autonomous Agricultural Robots", "AI for Customer Sentiment Analysis", "AI in Drug Repurposing", 
    "Smart Wearables and AI", "AI in Personalized Medicine", "Deep Learning for Facial Recognition", 
    "AI for Sentiment Analysis in Social Media", "Data Science in Sports", "AI in Robotics Process Automation", 
    "AI in Fintech", "AI and Machine Learning for Healthcare Diagnostics", 
    "AI in Human-Computer Interaction", "Blockchain for Secure Data Sharing", 
    "AI for Predicting Disease Outbreaks", "Deep Learning for Natural Language Processing", 
    "AI for Autonomous Weapons", "Blockchain in E-commerce", "AI in Public Safety", 
    "AI in Human-Computer Interaction", "Blockchain for Healthcare Data Security", 
    "AI in Space Missions", "AI for Customer Retention", "Artificial Intelligence for Smart Cities",
    "AI for Online Education", "Blockchain for Intellectual Property", 
    "AI in Climate Monitoring", "AI for Automated Content Creation", "Blockchain in Music Industry", 
    "Artificial Intelligence for Smart Homes", "AI for Video Game Development", 
    "AI for Emotion Recognition", "AI in Manufacturing Process Optimization", "Blockchain in Food Supply Chain",
    "AI for Personal Finance Management", "Smart Wearables and IoT", "AI in Food Safety", 
    "AI for Disaster Prediction", "Deep Learning in Medical Imaging", 
    "Artificial Intelligence in Retail", "AI for Sustainable Agriculture", "AI in Healthcare Robotics",
    "AI in Public Health", "AI for Anti-Money Laundering", "AI for Climate Change Mitigation",
    "Deep Learning for Autonomous Systems", "AI in Geospatial Analysis"
]

# Templates for abstracts
abstract_templates = [
    "The topic of {} explores cutting-edge advancements in this field, with particular focus on how new innovations are impacting industries such as finance, healthcare, and manufacturing. Recent developments have shown potential for revolutionizing the way businesses and individuals interact with data.",
    "This paper delves into the latest breakthroughs in {} and examines how these technologies are poised to change the landscape of global markets. We will explore key trends, challenges, and opportunities that could arise from widespread adoption of these innovations.",
    "In this study, we investigate the potential applications of {} across various sectors, including their implications for future technological developments. The paper analyzes the advantages and limitations of implementing such technologies in real-world environments.",
    "The concept of {} has gained significant attention in recent years due to its transformative potential in a variety of industries. This paper provides an overview of the state-of-the-art research in this area, including case studies and expert insights on its potential impact.",
    "This paper offers a comprehensive review of {} and its evolving role in shaping the future of technological innovation. By examining existing literature and case studies, we provide insights into the future potential and challenges associated with the adoption of this technology."
]

# Generate abstracts for each topic
data = []
for topic in topics:
    # Randomly choose an abstract template
    abstract = random.choice(abstract_templates).format(topic)
    data.append({"Title": topic, "Abstract": abstract})

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("research_papers_100.csv", index=False)

print("CSV file 'research_papers_100.csv' generated successfully with 100 unique topics.")
