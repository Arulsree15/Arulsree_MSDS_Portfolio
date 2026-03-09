# Personalized AI Nutrition Coach – Fine-Tuning GPT

## Project Overview
This project explores building a generative AI-powered nutrition assistant capable of **creating personalized meal plans**, providing **nutritional breakdowns**, and delivering **motivational dietary guidance**. Using OpenAI’s GPT-3.5-turbo, we conducted prompt experiments to evaluate the model’s baseline ability to generate meal plans, handle dietary restrictions, and provide conversational coaching.

The ultimate goal is to **fine-tune a model** that improves dietary decision-making and supports personalized nutrition for users with varying goals, preferences, and restrictions.

## Key Features
- Generate 3-day meal plans customized to goals, diet, and calories.
- Provide macronutrient and nutritional insights.
- Adapt meal plans for restrictions (vegetarian, gluten-free, etc.).
- Offer motivational messages and health education.
- Summarize diet benefits concisely.

## Prompt Experiments
1. 3-day vegetarian meal plan under 1500 calories/day.
2. Explain macronutrient ratios for muscle gain.
3. Adjust meal plans for gluten-free users.
4. Generate motivational messages for healthy eating adherence.
5. Summarize key benefits of the Mediterranean diet (<100 words).

## Fine-Tuning Plan
- **Dataset:** Curated JSONL with user prompts and ideal responses covering nutrition goals, restrictions, and educational explanations.  
- **Base Model:** GPT-3.5-turbo  
- **Process:** Upload dataset via OpenAI API → Supervised fine-tuning → Evaluate with nutrition-specific prompts.  
- **Metrics:** Nutritional accuracy, response coherence, helpfulness, engagement.

## Tools & Technologies
- Python 3.10+  
- Jupyter Notebook  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- OpenAI API  
- Streamlit (deployment)

## Usage
1. Clone the repository:
```bash
git clone https://github.com/your-username/nutrition-ai-finetune.git
cd nutrition-ai-finetune
```

2. Install dependencies:
pip install -r requirements.txt

3. Run Prompt_Experiments.ipynb to test GPT responses.

4. Follow Milestone 3 instructions to fine-tune GPT-3.5-turbo with curated datasets.

5. Deploy the fine-tuned model via Streamlit for interactive nutrition coaching.

Results & Insights

GPT-3.5 generates coherent and mostly accurate meal plans.

Can handle dietary restrictions and provide motivational guidance.

Limitations: portion size precision, consistency, and personalization require fine-tuning.

Fine-tuning with curated datasets will enhance accuracy, personalization, and contextual understanding.

References

Edamam Recipe & Nutrition API

OpenAI Fine-Tuning Guide – GPT-3.5-turbo

USDA FoodData Central

AI in Nutrition Use Cases – MindInventory