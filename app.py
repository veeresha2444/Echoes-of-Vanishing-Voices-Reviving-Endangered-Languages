#!/usr/bin/env python
# coding: utf-8

# In[1]:




# In[2]:


# Cell 1: Import dependencies and setup
from flask import Flask, render_template, request, redirect, url_for, session
import os

# Create templates directory if it doesn't exist
if not os.path.exists('templates'):
    os.makedirs('templates')

# Temporary user storage
users = {
    'user@example.com': {
        'name': 'Demo User',
        'password': 'password123'
    }
}

print("Dependencies imported and setup complete")

# In[3]:


# Cell 2: Get Started Now Page HTML
get_started_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Started - Konkani-Lambani-Hindi Learn</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        :root {
            --primary: #4e54c8;
            --secondary: #8f94fb;
            --accent: #ff6b6b;
            --light: #f8f9fa;
            --dark: #343a40;
        }
        
        body {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: var(--dark);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        
        .container {
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .logo {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 30px;
        }
        
        .logo i {
            font-size: 3rem;
            color: white;
        }
        
        .logo h1 {
            font-size: 2.5rem;
            color: white;
        }
        
        .hero {
            text-align: center;
            padding: 40px 20px;
            color: white;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            margin-bottom: 30px;
        }
        
        .hero h2 {
            font-size: 2.8rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto 30px;
        }
        
        .btn {
            display: inline-block;
            padding: 15px 40px;
            background-color: white;
            color: var(--primary);
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            font-size: 1.2rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 极速加速器.2);
        }
        
        .btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 8极速加速器 25px rgba(0, 0, 0, 0.3);
            background-color: #ffeb3b;
        }
        
        @media (max-width: 768px) {
            .hero h2 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <i class="fas fa-language fa-2x"></i>
            <h1>Konkani-Lambani-Hindi Learn</h1>
        </div>
        
        <div class="hero">
            <h2>Start Your Language Journey Today</h2>
            <p>Learn Konkani and Lambani and Hindi with our interactive platform. Translate, practice, and master both languages easily.</p>
            <a href="/login" class="btn">Get Started Now <i class="fas fa-arrow-right"></i></a>
        </div>
    </div>
</body>
</html>
'''

# Save get started page HTML to a file
with open('templates/get_started.html', 'w') as f:
    f.write(get_started_html)
    
print("Get Started page created successfully")

# In[4]:


# Cell 3: Login Page HTML
login_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Konkani-Lambani-Hindi Learn</title>
    <link rel="stylesheet极速加速器 href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        :root {
            --primary: #4e54c8;
            --secondary: #8f94fb;
            --accent: #ff6b6b;
            --light: #f8f9fa;
            --dark: #343a40;
        }
        
        body {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: var(--dark);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .container {
            width: 100%;
            max-width: 400px;
            padding: 20px;
        }
        
        .logo {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 30px;
        }
        
        .logo i {
            font-size: 2.5rem;
            color: white;
        }
        
        .logo h1 {
            font-size: 2rem;
            color: white;
        }
        
        .login-box {
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
        }
        
        .login-box h2 {
            text-align: center;
            color: var(--primary);
            margin-bottom: 20px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
        }
        
        .form-group input {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        
        .login-btn {
            width: 100%;
            padding: 12px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .login-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        
        .demo-credentials {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
            font-size: 0.9rem;
        }
        
        .demo-credentials h3 {
            margin-bottom: 10px;
            color: var(--primary);
        }
        
        .back-link {
            text-align: center;
            margin-top: 20px;
        }
        
        .back-link a {
            color: white;
            text-decoration: none;
        }
        
        .back-link a:hover {
            text-decoration: underline;
        }
        
        .message {
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 5px;
            text-align: center;
        }
        
        .error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <i class="fas fa-language fa-2x"></i>
            <h1>Konkani-Lambani-Hindi Learn</h1>
        </div>
        
        <div class="login-box">
            <h2>Login to Your Account</h2>
            
            {% if error %}
        
            <div class="message error">{{ error }}</div>
            {% endif %}
            
            <form method="POST" action="/login">
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" placeholder="Enter your email" required>
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" placeholder="Enter your password" required>
                </div>
                <button type="submit" class="login-btn">Login</button>
            </form>
            
            <div class="demo-credentials">
                <h3>Demo Credentials:</h3>
                <p>Email: capstone@78.com</p>
                <p>Password: capstone123</p>
            </div>
        </div>
        
        <div class="back-link">
            <a href="/">&larr; Back to Get Started</a>
        </div>
    </div>
</body>
</html>
'''

# Save login page HTML to a file
with open('templates/login.html', 'w') as f:
    f.write(login_html)
    
print("Login page created successfully")

# In[5]:


# Cell 4: Home Page HTML (After Login)
home_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Konkani-Lambani-Hindi Learn</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        :root {
            --primary: #4e54c8;
            --secondary: #8f94fb;
            --accent: #ff6b6b;
            --light: #f8f9fa;
            --dark: #343a40;
        }
        
        body {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: var(--dark);
            min-height: 100vh;
        }
        
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Header Styles */
        header {
            background-color: rgba(255, 255, 255, 0.9);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 15px 0;
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo i {
            color: var(--primary);
        }
        
        .logo h1 {
            font-size: 1.8rem;
            color: var(--primary);
        }
        
        nav ul {
            display: flex;
            list-style: none;
            gap: 20px;
            align-items: center;
        }
        
        nav a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            padding: 5px 10px;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        
        nav a:hover, nav a.active {
            background-color: var(--primary);
            color: white;
        }
        
        .user-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .user-info span {
            font-weight: 500;
        }
        
        .logout-btn {
            background-color: var(--accent);
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 500;
        }
        
        /* Welcome Section */
        .welcome-section {
            background-color: white;
            border-radius: 10px;
            padding: 40px;
            margin: 30px auto;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .welcome-section h2 {
            color: var(--primary);
            margin-bottom: 15px;
        }
        
        .welcome-section p {
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto 30px;
        }
        
        /* Features Grid */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .feature-card {
            background: linear-gradient(to bottom right, white, #f0f4ff);
            border-radius: 10px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
            border: 1px solid #e0e0e0;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        }
        
        .feature-card i {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 15px;
        }
        
        .feature-card h3 {
            color: var(--primary);
            margin-bottom: 10px;
        }
        
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                gap: 15px;
            }
            
            nav ul {
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container header-content">
            <div class="logo">
                <i class="fas fa-language fa-2x"></i>
                <h1>Konkani-Lambani-Hindi Learn</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="/home" class="nav-link active">Home</a></li>
                    <li><a href="/translation" class="nav-link">Translation</a></li>
                    <li><a href="/courses" class="nav-link">Dictonary</a></li>
                    <li><a href="/about" class="nav-link">About</a></li>
                    <li><a href="/contact" class="nav-link">Contact</a></li>
                    <li class="user-info">
                        <span>Welcome, {{ name }}!</span>
                        <a href="/logout" class="logout-btn">Logout</a>
                    </li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main class="container">
        <div class="welcome-section">
            <h2>Welcome to Your Language Learning Journey!</h2>
            <p>Start exploring our tools and resources to learn Konkani and Lambani and Hindi effectively.</p>
        </div>
        
        <div class="features-grid">
            <div class="feature-card">
                <i class="fas fa-exchange-alt"></i>
                <h3>Translation Tool</h3>
                <p>Translate words and phrases between Konkani and Lambani and Hindi instantly</p>
            </div>
            
            <div class="feature-card">
                <i class="fas fa-book"></i>
                <h3>Vocabulary Builder</h3>
                <p>Learn common words and phrases in both languages with flashcards</p>
            </div>
            
            <div class="feature-card">
                <i class="fas fa-gamepad"></i>
                <h3>Interactive Games</h3>
                <p>Play fun games to improve your language skills</p>
            </div>
            
            <div class="feature-card">
                <i class="fas fa-file-audio"></i>
                <h3>Audio Lessons</h3>
                <p>Listen to native speakers for perfect pronunciation</p>
            </div>
            
            <div class="feature-card">
                <i class="fas fa-chalkboard-teacher"></i>
                <h3>Grammar Guide</h3>
                <p>Understand the grammar rules of both languages</p>
            </div>
            
            <div class="feature-card">
                <i class="fas fa-comments"></i>
                <h3>Practice Conversations</h3>
                <p>Practice common dialogues in various situations</p>
            </div>
        </div>
    </main>
</body>
</html>
'''

# Save home page HTML to a file
with open('templates/home.html', 'w') as f:
    f.write(home_html)
    
print("Home page created successfully")

# In[6]:


# Cell 5 : Translation Page HTML (updated to connect backend)
translation_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Translation - Konkani-Lambani-Hindi Learn</title>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',sans-serif}
:root{--p:#4e54c8;--s:#8f94fb}
body{background:linear-gradient(to right,var(--p),var(--s));min-height:100vh}
header{background:#fff;padding:15px;box-shadow:0 2px 10px rgba(0,0,0,.1)}
.container{max-width:1200px;margin:auto;padding:0 20px}
nav ul{display:flex;gap:20px;list-style:none}
nav a{text-decoration:none;color:#333;padding:6px 12px;border-radius:5px}
nav a.active,nav a:hover{background:var(--p);color:#fff}
.page{background:#fff;margin:40px auto;padding:30px;border-radius:10px;max-width:900px}
h2{text-align:center;color:var(--p);margin-bottom:20px}
.language-selection{display:flex;justify-content:center;gap:15px;margin-bottom:20px}
.language-option{border:2px solid var(--p);padding:8px 20px;border-radius:25px;cursor:pointer}
.language-option.active{background:var(--p);color:#fff}
.translation-container{display:flex;gap:20px;flex-wrap:wrap}
.translation-box{flex:1;min-width:300px}
textarea{width:100%;height:150px;padding:12px;border-radius:8px;border:1px solid #ccc;font-size:1rem}
.language-selector{display:flex;justify-content:space-between;margin-bottom:8px}
select{padding:6px 12px}
.btn{display:flex;justify-content:center;gap:10px;margin-top:20px}
button{padding:12px 25px;border:none;border-radius:25px;font-weight:bold;color:#fff;
background:linear-gradient(to right,var(--p),var(--s));cursor:pointer}
button.speak{background:linear-gradient(to right,#ff6b6b,#ff8e8e)}
.status-message{text-align:center;margin-top:10px;padding:10px;border-radius:6px;display:none}
.status-message.success{background:#d4edda;color:#155724;display:block}
.status-message.error{background:#f8d7da;color:#721c24;display:block}
.language-info{text-align:center;margin-top:10px;color:#666}
</style>
</head>

<body>

<header>
<div class="container" style="display:flex;justify-content:space-between;align-items:center">
<h2>Konkani–Lambani–Hindi Learn</h2>
<nav>
<ul>
<li><a href="/home">Home</a></li>
<li><a href="/translation" class="active">Translation</a></li>
<li><a href="/courses">Dictionary</a></li>
<li><a href="/about">About</a></li>
<li><a href="/contact">Contact</a></li>
</ul>
</nav>
</div>
</header>

<main class="container">
<div class="page">

<h2>Language Translation</h2>

<div class="language-selection">
<div class="language-option active" data-lang="konkani">Konkani ↔ Hindi</div>
<div class="language-option" data-lang="lambani">Lambani ↔ Hindi</div>
</div>

<div class="translation-container">
<div class="translation-box">
<div class="language-selector">
<label>From:</label>
<select id="from-language">
<option>Konkani</option>
<option>Hindi</option>
</select>
</div>
<textarea id="source-text" placeholder="Enter text..."></textarea>
</div>

<div class="translation-box">
<div class="language-selector">
<label>To:</label>
<select id="to-language">
<option>Hindi</option>
<option>Konkani</option>
</select>
</div>
<textarea id="translated-text" placeholder="Translation appears here..." readonly></textarea>
</div>
</div>

<div class="btn">
<button id="translate-btn"><i class="fas fa-language"></i> Translate</button>
<button id="speak-btn" class="speak"><i class="fas fa-volume-up"></i> Speak</button>
</div>

<div id="status-message" class="status-message"></div>
<div class="language-info" id="language-info">
Currently translating between Konkani and Hindi
</div>

</div>
</main>

<script>
let currentLanguage="konkani";
let audio=null;

function showStatus(msg,type){
const el=document.getElementById("status-message");
el.textContent=msg;
el.className="status-message "+type;
}

document.querySelectorAll(".language-option").forEach(opt=>{
opt.onclick=()=>{
document.querySelectorAll(".language-option").forEach(o=>o.classList.remove("active"));
opt.classList.add("active");
currentLanguage=opt.dataset.lang;

const from=document.getElementById("from-language");
const to=document.getElementById("to-language");

if(currentLanguage==="konkani"){
from.innerHTML="<option>Konkani</option><option>Hindi</option>";
to.innerHTML="<option>Hindi</option><option>Konkani</option>";
document.getElementById("language-info").textContent=
"Currently translating between Konkani and Hindi";
}else{
from.innerHTML="<option>Lambani</option><option>Hindi</option>";
to.innerHTML="<option>Hindi</option><option>Lambani</option>";
document.getElementById("language-info").textContent=
"Currently translating between Lambani and Hindi";
}

document.getElementById("source-text").value="";
document.getElementById("translated-text").value="";
};
});

document.getElementById("translate-btn").onclick=async()=>{
const text=document.getElementById("source-text").value.trim();
const fromLang=document.getElementById("from-language").value;

if(!text)return showStatus("Enter text","error");

try{
const r=await fetch("/translate",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({text,source_lang:fromLang,language_pair:currentLanguage})});
const d=await r.json();
document.getElementById("translated-text").value=d.translation;
showStatus("Translation successful","success");
}catch{showStatus("Translation failed","error")}
};

document.getElementById("speak-btn").onclick=async()=>{
const text=document.getElementById("translated-text").value.trim();
if(!text)return showStatus("Translate first","error");

try{
const r=await fetch("/speak",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({text:text})
});

if(!r.ok)throw new Error();

const blob=await r.blob();
audio=new Audio(URL.createObjectURL(blob));
audio.play();
showStatus("Speaking...","success");

}catch{
showStatus("Speech failed","error");
}
};
</script>

</body>
</html>

'''

# Save translation page HTML to templates
with open('templates/translation.html', 'w', encoding='utf-8') as f:
    f.write(translation_html)

print("✅ Translation page updated to connect with backend /translate route")


# In[7]:


# Create HTML file with JavaScript search
courses_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dictionary - Konkani-Lambani-Hindi Learn</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        :root {
            --primary: #4e54c8;
            --secondary: #8f94fb;
            --accent: #ff6b6b;
            --dark: #343a40;
        }

        body {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        /* ===== HEADER (SAME AS TRANSLATION PAGE) ===== */
        header {
            background-color: rgba(255, 255, 255, 0.9);
            box-shadow: 0 2px 10px rgba(0,0,0,.1);
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo h1 {
            font-size: 1.8rem;
            color: var(--primary);
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 20px;
        }

        nav a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            padding: 5px 10px;
            border-radius: 5px;
        }

        nav a:hover,
        nav a.active {
            background-color: var(--primary);
            color: white;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 500;
        }

        .logout-btn {
            background-color: var(--accent);
            color: white;
            padding: 6px 12px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.9rem;
        }

        /* ===== DICTIONARY CARD ===== */
        .page {
            background: white;
            border-radius: 10px;
            padding: 30px;
            margin: 30px auto;
            box-shadow: 0 5px 15px rgba(0,0,0,.1);
        }

        .page h2 {
            color: var(--primary);
            text-align: center;
            margin-bottom: 20px;
        }

        .language-tabs {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-bottom: 25px;
        }

        .language-tab {
            padding: 10px 25px;
            border: 2px solid var(--primary);
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
        }

        .language-tab.active {
            background: var(--primary);
            color: white;
        }

        .search-container {
            display: flex;
            gap: 10px;
            margin-bottom: 25px;
        }

        .search-input {
            flex: 1;
            padding: 14px 20px;
            border-radius: 25px;
            border: 1px solid #ddd;
            font-size: 1rem;
        }

        .search-btn {
            padding: 14px 30px;
            border-radius: 25px;
            border: none;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            font-weight: bold;
            cursor: pointer;
        }

        .word-card {
            border: 2px solid #eee;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 12px;
        }

        .source-word {
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--primary);
        }

        .hindi-translation {
            color: #666;
            margin-top: 5px;
        }

        footer {
            margin-top: auto;
            color: white;
            text-align: center;
            padding: 15px 0;
        }
    </style>
</head>

<body>

<header>
    <div class="container header-content">
        <div class="logo">
            <i class="fas fa-language fa-2x" style="color:#4e54c8;"></i>
            <h1>Konkani-Lambani-Hindi Learn</h1>
        </div>

        <nav>
            <ul>
                <li><a href="/home">Home</a></li>
                <li><a href="/translation">Translation</a></li>
                <li><a href="/courses" class="active">Dictionary</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>

        <div class="user-info">
            <span>Welcome, {{ name }}!</span>
            <a href="/logout" class="logout-btn">Logout</a>
        </div>
    </div>
</header>

<main class="container">
    <div class="page">
        <h2>Dictionary Search</h2>

        <div class="language-tabs">
            <div class="language-tab active" data-lang="konkani">Konkani</div>
            <div class="language-tab" data-lang="lambani">Lambani</div>
        </div>

        <div class="search-container">
            <input id="search-input" class="search-input" placeholder="Enter word to search">
            <button class="search-btn" id="search-btn">Search</button>
        </div>

        <div id="results-container">
            <p style="text-align:center;color:#777;">Search for a word to see results</p>
        </div>
    </div>
</main>

<footer>
    <p>© 2026 Konkani-Lambani-Hindi Learning Platform</p>
</footer>

<script>
    let currentLanguage = "konkani";

    document.querySelectorAll(".language-tab").forEach(tab => {
        tab.onclick = () => {
            document.querySelectorAll(".language-tab").forEach(t => t.classList.remove("active"));
            tab.classList.add("active");
            currentLanguage = tab.dataset.lang;
        };
    });

    document.getElementById("search-btn").onclick = searchWords;
    document.getElementById("search-input").onkeypress = e => {
        if (e.key === "Enter") searchWords();
    };

    async function searchWords() {
        const word = document.getElementById("search-input").value.trim();
        const container = document.getElementById("results-container");
        if (!word) return;

        container.innerHTML = "<p>Searching...</p>";

        try {
            const res = await fetch(`/api/search?lang=${currentLanguage}&word=${encodeURIComponent(word)}`);
            const data = await res.json();

            container.innerHTML = "";

            if (!data.results || data.results.length === 0) {
                container.innerHTML = "<p>No results found</p>";
                return;
            }

            data.results.forEach(item => {
                container.innerHTML += `
                    <div class="word-card">
                        <div class="source-word">${item.word}</div>
                        <div class="hindi-translation">Hindi: ${item.hindi}</div>
                    </div>
                `;
            });
        } catch {
            container.innerHTML = "<p>Backend not reachable</p>";
        }
    }
</script>

</body>
</html>

'''
# Create templates directory if it doesn't exist
import os
os.makedirs('templates', exist_ok=True)

# Save HTML file
with open('templates/courses.html', 'w', encoding='utf-8') as f:
    f.write(courses_html)

print("✅ Courses page created successfully in templates/courses.html")
print("🔍 Dictionary search frontend updated!")
print("💡 Now try searching on the /courses page via localtunnel.")

# In[8]:


# Cell 7: About Page HTML
about_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About - Konkani-Lambani-Hindi Learn</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* Include all the CSS from the home page here */
        /* For brevity, I'm not repeating the full CSS */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        :root {
            --primary: #4e54c8;
            --secondary: #8f94fb;
            --accent: #ff6b6b;
            --light: #f8f9fa;
            --dark: #343a40;
        }
        
        body {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: var(--dark);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Header Styles */
        header {
            background-color: rgba(255, 255, 255, 0.9);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo img {
            width: 40px;
            height: 40px;
        }
        
        .logo h1 {
            font-size: 1.8rem;
            color: var(--primary);
        }
        
        nav ul {
            display: flex;
            list-style: none;
            gap: 20px;
        }
        
        nav a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            padding: 5px 10px;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        
        nav a:hover, nav a.active {
            background-color: var(--primary);
            color: white;
        }
        
        /* Page Styles */
        .page {
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            margin: 30px auto;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .page h2 {
            color: var(--primary);
            margin-bottom: 20px;
            text-align: center;
        }
        
        /* About Page Styles */
        .about-content {
            display: flex;
            flex-direction: column;
            gap: 40px;
            margin-top: 30px;
        }
        
        @media (min-width: 992px) {
            .about-content {
                flex-direction: row;
            }
            
            .about-text {
                flex: 2;
            }
            
            .about-stats {
                flex: 1;
            }
        }
        
        .about-text h3 {
            color: var(--primary);
            margin: 20px 0 10px;
        }
        
        .about-text p {
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        .about-stats {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .stat-card {
            background: linear-gradient(to bottom right, #f8f9fa, #ffffff);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }
        
        .stat-card i {
            color: var(--primary);
            margin-bottom: 15px;
        }
        
        .stat-card h4 {
            font-size: 2rem;
            color: var(--primary);
            margin: 10px 0;
        }
        
        .stat-card p {
            color: #6c757d;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                gap: 15px;
            }
            
            nav ul {
                flex-wrap: wrap;
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container header-content">
            <div class="logo">
                <i class="fas fa-language fa-2x" style="color: #4e54c8;"></i>
                <h1>Konkani-Lambani-Hindi Learn</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="/home" class="nav-link">Home</a></li>
                    <li><a href="/translation" class="nav-link">Translation</a></li>
                    <li><a href="/courses" class="nav-link">Courses</a></li>
                    <li><a href="/about" class="nav-link active">About</a></li>
                    <li><a href="/contact" class="nav-link">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- About Page Content -->
    <main class="container">
        <div class="page">
            <h2>About Us</h2>
            <p>Learn more about our mission to make Konkani and Lambani and Hindi learning accessible to everyone.</p>
            
            <div class="about-content">
                <div class="about-text">
                    <h3>Our Mission</h3>
                    <p>We believe that language learning should be engaging, accessible, and effective. Our platform was created to help people learn Konkani and lambani and Hindi through modern, interactive methods that make the process enjoyable and rewarding.</p>
                    
                    <h3>Our Story</h3>
                    <p>Founded in 2026, our platform grew from a personal need to connect with cultural roots through language. What started as a small project has now evolved into a comprehensive learning platform serving thousands of users worldwide.</p>
                    
                    <h3>Our Approach</h3>
                    <p>We combine traditional language learning techniques with modern technology to create an immersive experience. Our courses are designed by language experts and native speakers to ensure authenticity and effectiveness.</p>
                </div>
                
                <div class="about-stats">
                    <div class="stat-card">
                        <i class="fas fa-users fa-3x"></i>
                        <h4>0</h4>
                        <p>Active Learners</p>
                    </div>
                    
                    <div class="stat-card">
                        <i class="fas fa-book fa-3x"></i>
                        <h4>0</h4>
                        <p>Learning Resources</p>
                    </div>
                    
                    <div class="stat-card">
                        <i class="fas fa-globe fa-3x"></i>
                        <h4>0</h4>
                        <p>Countries</p>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2026 Konkani-Lambani-Hindi Learning Platform. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
'''

# Save about page HTML to a file
with open('templates/about.html', 'w') as f:
    f.write(about_html)
    
print("About page created successfully")

# In[9]:


# Cell 8: Contact Page HTML
contact_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact - Konkani-Lambani-Hindi Learn</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        :root {
            --primary: #4e54c8;
            --secondary: #8f94fb;
            --accent: #ff6b6b;
            --light: #f8f9fa;
            --dark: #343a40;
        }
        
        body {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: var(--dark);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Header Styles */
        header {
            background-color: rgba(255, 255, 255, 0.9);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo i {
            color: var(--primary);
            font-size: 2rem;
        }
        
        .logo h1 {
            font-size: 1.8rem;
            color: var(--primary);
        }
        
        nav ul {
            display: flex;
            list-style: none;
            gap: 20px;
            align-items: center;
        }
        
        nav a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            padding: 5px 10px;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        
        nav a:hover, nav a.active {
            background-color: var(--primary);
            color: white;
        }
        
        .user-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .user-info span {
            font-weight: 500;
        }
        
        .logout-btn {
            background-color: var(--accent);
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 500;
        }
        
        /* Page Styles */
        .page {
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            margin: 30px auto;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .page h2 {
            color: var(--primary);
            margin-bottom: 20px;
            text-align: center;
        }
        
        /* Contact Page Styles */
        .contact-container {
            display: flex;
            flex-direction: column;
            gap: 40px;
            margin-top: 30px;
        }
        
        @media (min-width: 992px) {
            .contact-container {
                flex-direction: row;
            }
            
            .contact-info {
                flex: 1;
                padding-right: 20px;
            }
            
            .contact-form {
                flex: 1;
                padding-left: 20px;
                border-left: 1px solid #eee;
            }
        }
        
        .contact-info h3, .contact-form h3 {
            color: var(--primary);
            margin-bottom: 20px;
        }
        
        .contact-item {
            display: flex;
            align-items: flex-start;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .contact-item i {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.2rem;
            margin-top: 5px;
            min-width: 20px;
            text-align: center;
        }
        
        .contact-item h4 {
            margin-bottom: 5px;
        }
        
        .social-links {
            margin-top: 30px;
        }
        
        .social-icons {
            display: flex;
            gap: 15px;
            margin-top: 10px;
        }
        
        .social-icons a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            border-radius: 50%;
            transition: transform 0.3s ease;
            text-decoration: none;
        }
        
        .social-icons a:hover {
            transform: translateY(-3px);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            font-family: inherit;
        }
        
        .form-group textarea {
            resize: vertical;
            min-height: 120px;
        }
        
        .submit-btn {
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
            font-size: 1rem;
        }
        
        .submit-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                gap: 15px;
            }
            
            nav ul {
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .contact-container {
                gap: 30px;
            }
            
            @media (min-width: 992px) {
                .contact-info, .contact-form {
                    padding: 0 15px;
                }
                
                .contact-form {
                    border-left: 1px solid #eee;
                }
            }
        }
        
        footer {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px 0;
            text-align: center;
            margin-top: auto;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container header-content">
            <div class="logo">
                <i class="fas fa-language fa-2x"></i>
                <h1>Konkani-Lambani-Hindi Learn</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="/home" class="nav-link">Home</a></li>
                    <li><a href="/translation" class="nav-link">Translation</a></li>
                    <li><a href="/courses" class="nav-link">Dictonary</a></li>
                    <li><a href="/about" class="nav-link">About</a></li>
                    <li><a href="/contact" class="nav-link active">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Contact Page Content -->
    <main class="container">
        <div class="page">
            <h2>Contact Us</h2>
            <p style="text-align: center; margin-bottom: 30px;">Have questions or feedback? We'd love to hear from you. Get in touch with our team.</p>
            
            <div class="contact-container">
                <div class="contact-info">
                    <h3>Get In Touch</h3>
                    <div class="contact-item">
                        <i class="fas fa-map-marker-alt"></i>
                        <div>
                            <h4>Address</h4>
                            <p>123 Language Street, Learning City, 560001</p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <i class="fas fa-phone"></i>
                        <div>
                            <h4>Phone</h4>
                            <p>+91 9876543210</p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <i class="fas fa-envelope"></i>
                        <div>
                            <h4>Email</h4>
                            <p>info@konkanihindilearn.com</p>
                        </div>
                    </div>
                    
                    <div class="social-links">
                        <h4>Follow Us</h4>
                        <div class="social-icons">
                            <a href="#"><i class="fab fa-facebook-f"></i></a>
                            <a href="#"><i class="fab fa-twitter"></i></a>
                            <a href="#"><i class="fab fa-instagram"></i></a>
                            <a href="#"><i class="fab fa-linkedin-in"></i></a>
                            <a href="#"><i class="fab fa-youtube"></i></a>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form">
                    <h3>Send Message</h3>
                    <form id="contactForm">
                        <div class="form-group">
                            <input type="text" placeholder="Your Name" required>
                        </div>
                        
                        <div class="form-group">
                            <input type="email" placeholder="Your Email" required>
                        </div>
                        
                        <div class="form-group">
                            <input type="text" placeholder="Subject" required>
                        </div>
                        
                        <div class="form-group">
                            <textarea placeholder="Your Message" rows="5" required></textarea>
                        </div>
                        
                        <button type="submit" class="submit-btn">Send Message <i class="fas fa-paper-plane"></i></button>
                    </form>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2026 Konkani-Lambani-Hindi Learning Platform. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Contact form submission
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for your message! We will get back to you soon.');
            this.reset();
        });
    </script>
</body>
</html>
'''
# Save contact page HTML to a file
with open('templates/contact.html', 'w') as f:
    f.write(contact_html)
    
print("Contact page created successfully")

# In[ ]:


import os
import pandas as pd
import re
import difflib
import requests
from flask import (
    Flask, render_template, request,
    redirect, url_for, session,
    jsonify, Response
)

# =====================================================
# 🔹 FLASK APP
# =====================================================
app = Flask(__name__)
app.secret_key = "temporary_demo_key"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =====================================================
# 🔹 SAFE HELPERS (NO CRASH)
# =====================================================
def safe_read_csv(filename):
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        print(f"⚠️ CSV missing: {filename}")
        return pd.DataFrame()
    return pd.read_csv(path)

def safe_sentence_pairs(df, col1, col2):
    if df.empty:
        return []
    df.columns = df.columns.str.strip().str.lower()
    col1, col2 = col1.lower(), col2.lower()

    if col1 not in df.columns or col2 not in df.columns:
        print(f"⚠️ Missing columns: {col1}, {col2} → {df.columns.tolist()}")
        return []

    pairs = []
    for a, b in zip(df[col1], df[col2]):
        if pd.isna(a) or pd.isna(b):
            continue
        a, b = str(a).strip(), str(b).strip()
        if a and b:
            pairs.append((a, b))
    return pairs

def safe_word_pairs(df):
    if df.empty or df.shape[1] < 2:
        return []
    pairs = []
    for a, b in zip(df.iloc[:, 0], df.iloc[:, 1]):
        if pd.isna(a) or pd.isna(b):
            continue
        a, b = str(a).strip(), str(b).strip()
        if a and b:
            pairs.append((a, b))
    return pairs

# =====================================================
# 🔹 LOAD DATASETS (SAFE)
# =====================================================
konkani_df = safe_read_csv("cleaned_data.csv")
lambani_df = safe_read_csv("lambani_sentences-2.csv")

konkani_sentence_data = safe_sentence_pairs(konkani_df, "Konkani", "Hindi")
lambani_sentence_data = safe_sentence_pairs(lambani_df, "Lambani", "Hindi")

konkani_word_df = safe_read_csv("konkani_rule_based_pos words to words.csv")
lambani_word_df = safe_read_csv("lambani_words 200.csv")

konkani_word_data = safe_word_pairs(konkani_word_df)
lambani_word_data = safe_word_pairs(lambani_word_df)

# =====================================================
# 🔹 BOOST WORDS
# =====================================================
konkani_sample_data = [
    ("पाणी", "पानी"),
    ("मित्र", "दोस्त"),
    ("शाळा", "स्कूल"),
    ("हो", "हाँ"),
    ("नाय", "नहीं"),
]

# =====================================================
# 🔹 TRANSLATION MAPS (CRASH-PROOF)
# =====================================================
konkani_translation_data = (
    konkani_sentence_data + konkani_word_data + konkani_sample_data
)
lambani_translation_data = (
    lambani_sentence_data + lambani_word_data
)

konkani_to_hindi = dict(konkani_translation_data)
hindi_to_konkani = {h: k for k, h in konkani_translation_data}

lambani_to_hindi = dict(lambani_translation_data)
hindi_to_lambani = {h: k for k, h in lambani_translation_data}

konkani_word_to_hindi = dict(konkani_word_data)
hindi_to_konkani_word = {h: k for k, h in konkani_word_data}

lambani_word_to_hindi = dict(lambani_word_data)
hindi_to_lambani_word = {h: k for k, h in lambani_word_data}

# =====================================================
# 🔹 DICTIONARY SEARCH
# =====================================================
def search_word(query, language_pair, limit=10):
    query = query.strip()
    results = []

    if language_pair == "konkani":
        forward, reverse = konkani_word_to_hindi, hindi_to_konkani_word
    elif language_pair == "lambani":
        forward, reverse = lambani_word_to_hindi, hindi_to_lambani_word
    else:
        return results

    if query in forward:
        results.append((query, forward[query]))

    if query in reverse:
        results.append((reverse[query], query))

    if not results:
        matches = difflib.get_close_matches(query, forward.keys(), n=limit, cutoff=0.75)
        for m in matches:
            results.append((m, forward[m]))

    return results[:limit]

@app.route("/api/search", methods=["GET"])
def api_search():
    try:
        word = request.args.get("word", "").strip()
        lang = request.args.get("lang", "konkani").lower()
        if not word:
            return jsonify({"results": []})
        return jsonify({
            "results": [{"word": k, "hindi": h} for k, h in search_word(word, lang)]
        })
    except Exception as e:
        print("❌ SEARCH ERROR:", e)
        return jsonify({"results": []})

# =====================================================
# 🔹 TRANSLATION LOGIC
# =====================================================
def clean_text(text):
    return re.sub(r'^[,，]+', '', text).strip()

def split_sentences(text):
    parts = re.split(r'([.?!।])', text)
    return ["".join(parts[i:i+2]).strip()
            for i in range(0, len(parts), 2)
            if parts[i].strip()]

def translate_sentence(text, src, pair):
    maps = {
        ("Konkani", "konkani"): konkani_to_hindi,
        ("Hindi", "konkani"): hindi_to_konkani,
        ("Lambani", "lambani"): lambani_to_hindi,
        ("Hindi", "lambani"): hindi_to_lambani,
    }
    mapping = maps.get((src, pair))
    if not mapping:
        return "❌ Invalid"

    if text in mapping:
        return mapping[text]

    m = difflib.get_close_matches(text, mapping.keys(), 1, 0.7)
    return mapping[m[0]] if m else "❌ Not found"

def translate_text(text, src, pair):
    return " ".join(
        translate_sentence(s, src, pair)
        for s in split_sentences(clean_text(text))
    )

# =====================================================
# 🔹 AUTH & PAGES
# =====================================================
users = {"capstone@78.com": {"name": "Demo User", "password": "capstone123"}}

@app.route("/")
def get_started():
    return render_template("get_started.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        e, p = request.form.get("email"), request.form.get("password")
        if e in users and users[e]["password"] == p:
            session["user"], session["name"] = e, users[e]["name"]
            return redirect(url_for("home"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", name=session["name"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("get_started"))

@app.route("/translation")
def translation():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("translation.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# =====================================================
# 🔹 TRANSLATE API
# =====================================================
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    return jsonify({
        "translation": translate_text(
            text,
            data.get("source_lang", "Konkani"),
            data.get("language_pair", "konkani")
        )
    })

# =====================================================
# 🔹 TEXT TO SPEECH (OPTIONAL)
# =====================================================
@app.route("/speak", methods=["POST"])
def speak():
    text = request.get_json().get("text", "").strip()
    if not text:
        return jsonify({"error": "No text"}), 400

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        return jsonify({"error": "TTS disabled"}), 200

    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    r = requests.post(
        url,
        json={"text": text},
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        },
        timeout=10
    )
    if r.status_code != 200:
        return jsonify({"error": "TTS failed"}), 200

    return Response(r.content, mimetype="audio/mpeg")

# =====================================================
# 🔹 RUN SERVER
# =====================================================
if __name__ == "__main__":
    app.run()



# In[ ]:


# =====================================================
# 🔹 IMPORTS
# =====================================================

# In[ ]:








