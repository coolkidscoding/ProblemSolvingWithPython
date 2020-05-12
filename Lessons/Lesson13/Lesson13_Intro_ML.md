# <center>**[Cool Kids Coding School](https://www.coolkidscodingschool.com)**</center>

---

## Problem Solving with Python<br> Lesson 13: Introduction to Machine Learning and Tools 

![alt text][logo]

[logo]: ./images/ckcslogo.png

---

> 1.0 What is Machine Learning?

Machine learning is a tool for turning information into knowledge. In the past 50 years, there has been an explosion of data. This mass of data is useless unless we analyse it and find the patterns hidden within. Machine learning techniques are used to automatically find the valuable underlying patterns within complex data that we would otherwise struggle to discover. The hidden patterns and knowledge about a problem can be used to predict future events and perform all kinds of complex decision making.

Machine Learning is a subcategory of Artificial Intelligence.  Artificial Intelligence has to do with the efforts to assign human like decision making qualities to machines.  Some of the categories of AI are Machine Learning, Computer Vision, Natural Language Processing, etc.  

In this class we will focus on Machine Learning which is the creation and study of algorithms that use data to make decisions.  These algorithms "learn" from data.

![alt text][ml]

[ml]: ./images/machine_learning_deep_learning.png

Every time we Google something, listen to a song or even take a photo, Machine Learning is becoming part of the engine behind it, constantly learning and improving from every interaction. It’s also behind world-changing advances like detecting cancer, creating new drugs and self-driving cars.

The reason that Machine Learning is exciting, is because it is a step away from all our previous rule-based systems of:

if(x = y): 
    do z

There are multiple forms of Machine Learning; supervised, unsupervised , semi-supervised and reinforcement learning. Each form of Machine Learning has differing approaches, but they all follow the same underlying process and theory. 

![alt text][ml_types]

[ml_types]: ./images/learning.jpeg

> 2.0 Terminology

+ Dataset: A set of data examples, that contain features important to solving the problem.
+ Features: Important pieces of data that help us understand a problem. These are fed in to a Machine Learning algorithm to help it learn.
+ Model: The representation (internal model) of a phenomenon that a Machine Learning algorithm has learnt. It learns this from the data it is shown during training. The model is the output you get after training an algorithm. For example, a decision tree algorithm would be trained and produce a decision tree model.

> 3.0 Process

+ Data Collection: Collect the data that the algorithm will learn from.
+ Data Preparation: Format and engineer the data into the optimal format, extracting important features and performing dimensionality reduction.
+ Training: Also known as the fitting stage, this is where the Machine Learning algorithm actually learns by showing it the data that has been collected and prepared.
+ Evaluation: Test the model to see how well it performs.
+ Tuning: Fine tune the model to maximise it’s performance.

> 4.0 Machine Learning Approaches

There are many approaches that can be taken when conducting Machine Learning. They are usually grouped into the areas listed below. Supervised and Unsupervised are well established approaches and the most commonly used.

### Supervised Learning
In supervised learning, the goal is to learn the mapping (the rules) between a set of inputs and outputs.

For example, the inputs could be the weather forecast, and the outputs would be the visitors to the beach. The goal in supervised learning would be to learn the mapping that describes the relationship between temperature and number of beach visitors.

![alt text][supervised]

[supervised]: ./images/supervised_learning.png

### Unsupervised Learning
In unsupervised learning, only input data is provided in the examples. There are no labelled example outputs to aim for. But it may be surprising to know that it is still possible to find many interesting and complex patterns hidden within data without any labels.

An example of unsupervised learning in real life would be sorting different colour coins into separate piles. Nobody taught you how to separate them, but by just looking at their features such as colour, you can see which colour coins are associated and cluster them into their correct groups.

![alt text][unsupervised]

[unsupervised]: ./images/unsupervised_learning.png


> 5.0 Tools

![alt text][numpy]

[numpy]: ./images/numpy.jpeg

#### NumPy
NumPy is a very popular python library for large multi-dimensional array and matrix processing, with the help of a large collection of high-level mathematical functions. It is very useful for fundamental scientific computations in Machine Learning. It is particularly useful for linear algebra, Fourier transform, and random number capabilities. High-end libraries like TensorFlow uses NumPy internally for manipulation of Tensors.

#### Pandas
![alt text][pandas]

[pandas]: ./images/pandas.png
Pandas is a popular Python library for data analysis. It is not directly related to Machine Learning. As we know that the dataset must be prepared before training. In this case, Pandas comes handy as it was developed specifically for data extraction and preparation. It provides high-level data structures and wide variety tools for data analysis. It provides many inbuilt methods for groping, combining and filtering data.

#### Matplotlib
![alt text][matplotlib]

[matplotlib]: ./images/matplotlib.png
Matpoltlib is a very popular Python library for data visualization. Like Pandas, it is not directly related to Machine Learning. It particularly comes in handy when a programmer wants to visualize the patterns in the data. It is a 2D plotting library used for creating 2D graphs and plots. A module named pyplot makes it easy for programmers for plotting as it provides features to control line styles, font properties, formatting axes, etc. It provides various kinds of graphs and plots for data visualization, viz., histogram, error charts, bar chats, etc.

---

## **Any Questions?**

### **for any questions contact hw_help@coolkidscodingschool.com**
