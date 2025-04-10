# 🧠 Demo 1: Transformer Model Inference on Intel® Gaudi®2

This demo showcases how to run a pre-trained Hugging Face transformer model (BERT) for a question-answering task using **Intel® Gaudi®2 AI accelerators** inside the **Intel® Tiber™ Developer Cloud**.

---

## 🎯 Objective

- Load and run a transformer model using Hugging Face's `pipeline`
- Perform real-time inference for a question-answering task
- Optionally benchmark inference on CPU vs Gaudi2

---

## 📦 Requirements

- Python 3.8+
- `transformers`
- `torch`
- Optional: `optimum-habana` for Gaudi acceleration

Install with:

```bash
pip install transformers torch
# For Gaudi acceleration:
# pip install optimum[habana] --extra-index-url https://developer.intel.com/ipex-whl-stable
