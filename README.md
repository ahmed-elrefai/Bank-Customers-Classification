

# Padawin Bank Web Project
# Bank-Customers-Classification

## Overview

This repository contains the CSS and HTML files for the Padawin Bank web project. It includes a main website and a survey page, demonstrating the use of custom fonts, gradients, and responsive design for a modern banking application interface.

## Project Structure

The project is divided into two main sections:

1. **Main Website**: The primary page showcasing Padawin Bank&#39;s services and a call-to-action button.
2. **Survey Page**: A form-based survey collecting various user details and preferences.

## Technical Details

### CSS

The project&#39;s styles are defined in two CSS files:

1. **`styles.css`**: Applied to the main website.
2. **`styles2.css`**: Applied to the survey page.

#### Common Font Definitions

```css
@font-face {
    font-family: &#39;Petrona&#39;;
    src: url(C:\Projects\BankingWebAi\css\fonts\Petrona.ttf) format(&#39;truetype&#39;);
}

@font-face {
    font-family: &#39;Inter&#39;;
    src: url(C:\Projects\BankingWebAi\css\fonts\Inter.ttf) format(&#39;truetype&#39;);
}

Global Styles
:root {
    --primary-color: #4B0082; /* Main color */
    --secondary-color: #FF69B4; /* Accent color */
    --text-color: #FFFFFF; /* Text color */
    --background-color: #1E0033; /* Background color */
    --font-main: &#39;Petrona&#39;, sans-serif; /* Main font */
    --font-accent: &#39;Inter&#39;, serif; /* Accent font */
    --background-gradient: radial-gradient(circle at center, #1E0033, #4e0086); /* Background gradient */
    --header-gradient: radial-gradient(circle at center, #FF69B4); /* Header gradient */
    --cta-button-gradient: linear-gradient(to left, #FF69B4, #4e0086); /* CTA button gradient */
}

body {
    font-family: var(--font-main);
    background: var(--background-gradient);
    color: var(--text-color);
    margin: 0;
    padding: 0;
}

header {
    background: var(--header-gradient);
    padding: 1rem;
    text-align: center;
    color: var(--text-color);
    border-bottom: 2px solid rgba(255, 255, 255, 0.2); /* Optional: subtle border */
}

HTML Files
Main Website (index.html)
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Padawin Bank&lt;/title&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;styles.css&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;header&gt;
        &lt;nav&gt;
            &lt;h1&gt;Padawin Bank&lt;/h1&gt;
            &lt;button class=&quot;login-btn&quot;&gt;Log In&lt;/button&gt;
        &lt;/nav&gt;
    &lt;/header&gt;
    &lt;main&gt;
        &lt;section class=&quot;hero&quot;&gt;
            &lt;h1&gt;Padawin Bank&lt;/h1&gt;
            &lt;h2&gt;Take Control Over Finance&lt;/h2&gt;
            &lt;p&gt;Step into a world of financial security and growth. We are here to guide you every step of the way.&lt;/p&gt;
        &lt;/section&gt;
        &lt;section class=&quot;services&quot;&gt;
            &lt;h2&gt;Discover Our Services&lt;/h2&gt;
            &lt;div class=&quot;service-grid&quot;&gt;
                &lt;div class=&quot;service-item&quot;&gt;
                    &lt;h3&gt;Banking Solutions&lt;/h3&gt;
                    &lt;p&gt;We offer a wide range of banking solutions to meet your individual needs, from savings and checking accounts to investment options and loans.&lt;/p&gt;
                &lt;/div&gt;
                &lt;div class=&quot;service-item&quot;&gt;
                    &lt;h3&gt;Personalized Services&lt;/h3&gt;
                    &lt;p&gt;Experience personalized banking services tailored to your specific requirements. Our dedicated team provides expert advice and support.&lt;/p&gt;
                &lt;/div&gt;
                &lt;div class=&quot;service-item&quot;&gt;
                    &lt;h3&gt;Digital Tools&lt;/h3&gt;
                    &lt;p&gt;Manage your finances effortlessly with our user-friendly digital tools. Access your accounts, transfer funds, and more with just a few clicks.&lt;/p&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;a href=&quot;index2.html&quot; class=&quot;cta-button&quot;&gt;Take me to survey page&lt;/a&gt;
        &lt;/section&gt;
    &lt;/main&gt;
    &lt;footer&gt;
        &lt;p&gt;&amp;copy; 2024 Padawin Bank. All rights reserved.&lt;/p&gt;
    &lt;/footer&gt;
&lt;/body&gt;
&lt;/html&gt;

Survey Page (index2.html)
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Padawin Bank Survey&lt;/title&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;styles2.css&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;header&gt;
        &lt;h1&gt;Padawin Bank Survey&lt;/h1&gt;
    &lt;/header&gt;
    &lt;main&gt;
        &lt;form id=&quot;survey-form&quot;&gt;
            &lt;!-- Survey questions and form elements --&gt;
            &lt;div class=&quot;question&quot; id=&quot;q1&quot;&gt;
                &lt;label for=&quot;age&quot;&gt;Age:&lt;/label&gt;
                &lt;input type=&quot;number&quot; id=&quot;age&quot; name=&quot;age&quot; min=&quot;18&quot; max=&quot;200&quot; required&gt;
                &lt;button type=&quot;button&quot; onclick=&quot;nextQuestion(&#39;q1&#39;, &#39;q2&#39;)&quot;&gt;Next&lt;/button&gt;
            &lt;/div&gt;
            &lt;!-- Additional questions --&gt;
            &lt;div class=&quot;question&quot; id=&quot;thank-you&quot; style=&quot;display:none;&quot;&gt;
                &lt;h2&gt;Thank You!&lt;/h2&gt;
                &lt;p&gt;We appreciate your participation in our survey.&lt;/p&gt;
            &lt;/div&gt;
        &lt;/form&gt;
    &lt;/main&gt;
    &lt;script src=&quot;survey.js&quot;&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```
Custom Fonts

Petrona: Custom serif font used for main text.
Inter: Custom sans-serif font used for accent text.

Font Files:

Petrona.ttf: Located at css\fonts\Petrona.ttf
Inter.ttf: Located at css\fonts\Inter.ttf

## Gradients

Background Gradient: radial-gradient(circle at center, #1E0033, #4e0086)
Header Gradient: radial-gradient(circle at center, #FF69B4)
CTA Button Gradient: linear-gradient(to left, #FF69B4, #4e0086)

## JavaScript
```
The survey page uses survey.js for managing form interactions. Ensure this file is included in your project.
// Example function to navigate between survey questions
function nextQuestion(currentId, nextId) {
    document.getElementById(currentId).style.display = &#39;none&#39;;
    document.getElementById(nextId).style.display = &#39;block&#39;;
}
```
## Contribution

This project is licensed under the MIT License - see the LICENSE file for details.
Contact
