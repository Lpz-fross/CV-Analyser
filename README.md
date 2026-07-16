# CV & Job Description Analyser

An AI-powered tool that analyses how well a CV matches 
a job description — built with Python and the 
Anthropic Claude API.

## What it does

Paste any CV and job description into the tool and get 
back a structured analysis including:

- A match score out of 10
- Specific skills and experience that match the role
- Gaps and missing requirements with severity ratings
- 5 actionable CV improvement suggestions tailored to 
  the specific role
- A cover letter angle based on the candidate's profile
- An honest verdict on whether to apply

## Why I built this

I built this as part of my AI portfolio while 
transitioning into an AI-focused role. As a job seeker 
myself, I wanted a tool that gives genuinely specific 
feedback rather than generic career advice — so every 
output is grounded in the actual content of the CV and 
job description provided.

## How it works

The tool uses a structured prompt sent to Claude 
via the Anthropic API. The prompt engineers Claude 
to act as an expert career coach and output its 
analysis in a consistent six-section format. Results 
are automatically saved to timestamped text files so 
no analysis is ever lost.

## How to run it

**Requirements:**
- Python 3.8 or higher
- An Anthropic API key (get one at console.anthropic.com)

**Setup:**

1. Clone this repository
   git clone https://github.com/Lpz-fross/cv-analyser

2. Install dependencies
   pip install anthropic python-dotenv

3. Create a .env file in the root folder
   ANTHROPIC_API_KEY=your-api-key-here

4. Add your CV as a .txt file named my_cv.txt

5. Add a job description as a .txt file named 
   job_description.txt

6. Run the tool
   python analyser.py

## Project structure

analyser.py        — Main script and Claude API logic
menu.py            — Interactive terminal menu
README.md          — This file
.env               — Your API key (never shared)
.gitignore         — Keeps .env off GitHub
outputs/           — Saved analysis results

## What I learned

Building this taught me three things that did not come 
from courses alone:

Prompt structure matters more than prompt length. A 
well-structured six-section output format produced far 
more consistent and usable results than asking Claude 
to give detailed feedback in an open-ended way.

Designing for failure is as important as designing for 
success. I added specific error messages for missing 
files, empty files, and authentication problems so the 
tool fails helpfully rather than crashing confusingly.

Separation of concerns makes code easier to improve. 
Splitting the menu logic into menu.py and the analysis 
logic into analyser.py means either can be changed 
without breaking the other.

## Built with

- Python 3.x
- Anthropic Claude API
- python-dotenv

## About

Built by Leon Fordyce-Ross as Project 3 of an AI skills 
portfolio.

See the full portfolio at: (https://app.notion.com/p/AI-Portfolio-Leon-Fordyce-Ross-3917a277efdc803c9a31e58636e88cff?source=copy_link)

Connect with me on LinkedIn: www.linkedin.com/in/leon-fordyce-ross
