# Word Embeddings Debiasing

This repository contains a Jupyter notebook implementation exploring word embeddings and bias mitigation techniques. It demonstrates how to load and work with pre-trained GloVe word vectors, perform word analogies, and apply debiasing methods like **neutralization** and **equalization** to reduce gender and other biases in embeddings.

This project is based on a lab from the **Deep Learning Specialization** course by Andrew Ng on Coursera.

## Features
- Loading and preprocessing GloVe word vectors
- Word analogy solving (e.g., king - man + woman = queen)
- Bias detection and visualization
- Neutralization: Projecting neutral words onto the orthogonal space to the bias axis
- Equalization: Balancing gender-specific word pairs for fair representations

## References
- Based on research by Bolukbasi et al. on debiasing word embeddings.
- Based on a lab from the [Deep Learning Specialization](https://learn.deeplearning.ai/specializations/deep-learning) course by Andrew Ng (Coursera)
