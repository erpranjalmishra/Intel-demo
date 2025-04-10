import argparse
import time
from transformers import pipeline

def run_benchmark(device: str = "cpu", iterations: int = 10):
    print(f"Loading model on {device}...")
    qa = pipeline("question-answering", device=0 if device == "gaudi" else -1)

    context = "Intel Gaudi2 is an AI accelerator designed for deep learning and inference tasks."
    question = "What is Gaudi2 used for?"

    print(f"Running {iterations} iterations on {device}...")
    start = time.time()
    for _ in range(iterations):
        qa(question=question, context=context)
    end = time.time()

    print(f"Total time on {device}: {end - start:.2f} seconds")
    print(f"Average time per inference: {(end - start)/iterations:.4f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", choices=["cpu", "gaudi"], default="cpu")
    parser.add_argument("--iterations", type=int, default=10)
    args = parser.parse_args()

    run_benchmark(args.device, args.iterations)
