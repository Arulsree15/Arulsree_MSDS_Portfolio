# Install necessary libraries
!pip install transformers datasets peft

from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model
from datasets import load_dataset

# Load base model and tokenizer
model_name = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Prepare LoRA configuration
lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# Apply LoRA to the model
model = get_peft_model(model, lora_config)

# Example prompt-response pairs for training
data = [
    {"prompt": "Create a 3-day vegetarian meal plan for weight loss. Include calorie and macronutrient breakdowns for each meal.",
     "response": "Day 1: Breakfast: Oatmeal with berries (300 kcal, 10g protein, 50g carbs, 5g fat)..."},
    # Add more prompt-response pairs here
]

# Convert to HuggingFace dataset format
from datasets import Dataset
dataset = Dataset.from_list([{"text": f"User: {item['prompt']}\nAI: {item['response']}"} for item in data])

# Tokenize dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=2,
    save_steps=10,
    save_total_limit=2,
    logging_steps=5,
    learning_rate=2e-4,
    fp16=True,
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# Train the model
trainer.train()

# Inference example
prompt = "Suggest a high-protein breakfast for someone allergic to nuts and gluten."
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))