 Intel AI Workshop: Live Demo Script
🖥️ Demo Title: Running a Hugging Face Transformer Model on Intel® Gaudi®2 in the Tiber™ Developer Cloud
✅ Objectives:
Access Tiber Developer Cloud

Deploy a Hugging Face transformer model (e.g., BERT for question answering)

Compare performance: CPU vs Gaudi2

Explain what’s happening and how attendees can do the same

📋 Step-by-Step Script:
1. Intro
“Let’s dive into Intel’s AI ecosystem and run a real transformer model in the cloud using Intel Gaudi2 – an AI accelerator optimized for deep learning!”

2. Login to Intel Tiber™ Developer Cloud
Go to cloud.intel.com

Sign in using your developer account

Navigate to the Tiber Developer Cloud Dashboard

3. Open a Terminal (JupyterLab or CLI Session)
Launch a terminal inside a Gaudi2 compute environment

Use a pre-installed PyTorch or TensorFlow environment

Mention: “This environment is optimized by Intel for maximum performance”

4. Load and Run a Hugging Face Model
bash
Copy
Edit
# Activate environment
source /workspace/venv/bin/activate

# Install HF Transformers (if not pre-installed)
pip install transformers

# Run simple inference
python3
Inside Python:

python
Copy
Edit
from transformers import pipeline
qa = pipeline("question-answering")
context = "Intel Gaudi2 is designed for deep learning and model acceleration."
qa(question="What is Gaudi2 used for?", context=context)
5. Output
Show the model response

Highlight: “This is real-time inference using Intel’s Gaudi2”

📊 Optional: Benchmark Performance
Use a sample script to benchmark CPU vs Gaudi2:

bash
Copy
Edit
python benchmark.py --device cpu
python benchmark.py --device gaudi
Explain the speed difference and how Intel’s optimization improves performance (up to 10-100x depending on workload).

💬 Wrap-Up
“This is just a glimpse of what you can build using Intel’s AI ecosystem. From running LLMs to training computer vision models, the Tiber Developer Cloud gives you the hardware and tools to make it happen – free for Student Ambassadors.”

