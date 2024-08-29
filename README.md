

# Padawin Bank Web Project
# Bank-Customers-Classification

## Overview

This repository contains the CSS and HTML files for the Padawin Bank web project. 
It includes a main website and a survey page, demonstrating the use of custom fonts, gradients, and responsive design for a modern banking application interface.
The survey uses a Classification model to predict whether a user has or not a deposit at a bank.
Js Was used for handling the server side functionality 


## Project Structure

The project is divided into two main sections:

1. **Main Website**: The primary page showcasing Padawin Bank&#39;s services and a call-to-action button.
2. **Survey Page**: A form-based survey collecting various user details and preferences.

## Technical Details

### CSS

The project&#39;s styles are defined in two CSS files:

1. **`styles.css`**: Applied to the main website.
2. **`styles2.css`**: Applied to the survey page.


## Custom Fonts

Petrona: Custom serif font used for main text.
Inter: Custom sans-srif font used for accent text.

Font Files:

Petrona.ttf: Located at css\fonts\Petrona.ttf
Inter.ttf: Located at css\fonts\Inter.ttf

## Gradients

Background Gradient: radial-gradient(circle at center, #1E0033, #4e0086)
Header Gradient: radial-gradient(circle at center, #FF69B4)
CTA Button Gradient: linear-gradient(to left, #FF69B4, #4e0086)

## JavaScript
```
function nextQuestion(currentId, nextId) {
    document.getElementById(currentId).style.display = &#39;none&#39;;
    document.getElementById(nextId).style.display = &#39;block&#39;;
}
```
## Contribution

This project is licensed under the MIT License - see the LICENSE file for details.
Contact
