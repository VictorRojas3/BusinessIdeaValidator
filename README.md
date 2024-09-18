# BusinessIdeaValidator
This is part of a solution for the IBM TechXchange Hackathon build with watsonx that helps entrepreneurs in Mexico validate their business ideas

## Overview

The **Business Idea Validator** is a tool designed to help entrepreneurs in Mexico evaluate the viability of their business ideas. By leveraging **IBM Watsonx.ai**, this tool provides users with automated insights on their ideas, offering a structured analysis that includes strengths, weaknesses, competition, scope, and recommendations. The solution is entirely in Spanish, tailored for local entrepreneurs, making the process of validating business concepts faster, more accessible, and data-driven.

## Key Features

- **Tailored for Entrepreneurs in Mexico**: Focused on Spanish-speaking entrepreneurs to improve accessibility and relevance.
- **Automated Business Idea Analysis**: Powered by **IBM Watsonx.ai** for market and risk analysis.
- **Comprehensive Feedback**: Provides insights on strengths, weaknesses, competitors, market scope, and actionable recommendations.
- **Scalable Solution**: Part of the **EmprendeHub** platform, designed to support entrepreneurs at every stage of their journey.

## How It Works

1. **Input**: Users submit their business idea by starting with "Mi negocio es de..." and providing a detailed description.
2. **Processing**: The input is analyzed using **IBM Watsonx.ai**, leveraging NLP and data-driven insights.
3. **Output**: The tool returns a detailed report on the idea’s strengths, weaknesses, market competition, and potential scope, as well as recommendations for improvement.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/VictorRojas3/BusinessIdeaValidator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd BusinessIdeaValidator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your browser and go to `http://localhost:5000` to start using the tool.

## Prerequisites

- Python 3.12
- Flask
- IBM Watsonx.ai credentials

## Technology Stack

- **Backend**: Flask
- **AI & NLP**: IBM Watsonx.ai
- **Frontend**: HTML, CSS
- **Deployment**: Localhost (for development purposes)
