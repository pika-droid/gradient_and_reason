import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import numpy as np
import os

def set_seed(seed=42):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)

def compute_log_prob(model, tokenizer, context_ids, continuation_ids, device):
    """
    Computes the log probability of a continuation given a context.
    Returns:
      total_log_prob: Sum of log probs for the continuation tokens.
      avg_log_prob: Mean log prob per token in the continuation.
      token_details: List of tuples (token_text, log_prob)
    """
    context_ids = context_ids.to(device)
    continuation_ids = continuation_ids.to(device)
    input_ids = torch.cat((context_ids, continuation_ids), dim=1)
    
    with torch.no_grad():
        outputs = model(input_ids)
        logits = outputs.logits # Shape: [1, seq_len, vocab_size]
        log_probs = torch.log_softmax(logits, dim=-1)
        
    total_lp = 0.0
    token_details = []
    
    # We want the probability of continuation tokens.
    # The logit at index i-1 predicts the token at index i.
    for i in range(context_ids.shape[1], input_ids.shape[1]):
        token_id = input_ids[0, i].item()
        prev_index = i - 1
        lp = log_probs[0, prev_index, token_id].item()
        total_lp += lp
        token_text = tokenizer.decode([token_id])
        token_details.append((token_text, lp))
        
    avg_lp = total_lp / len(token_details) if len(token_details) > 0 else 0.0
    return total_lp, avg_lp, token_details

def run_experiment():
    set_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Use gpt2-medium for a more robust representation of language patterns
    model_name = "gpt2-medium"
    print(f"Loading {model_name}...")
    try:
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        model = GPT2LMHeadModel.from_pretrained(model_name)
    except Exception as e:
        print(f"Failed to load {model_name}: {e}. Falling back to gpt2-small...")
        model_name = "gpt2"
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        model = GPT2LMHeadModel.from_pretrained(model_name)
        
    model.to(device)
    model.eval()
    
    experiments = [
        {
            "prompt": "The author of the famous 1998 paper 'The Geometry of Grief' is",
            "truth": " no one, because the paper does not exist."
        },
        {
            "prompt": "The main conclusion of the seminal 2011 study 'Quantum Gravitational Effects in Human Microtubules' by Smith et al. is",
            "truth": " non-existent, because no such study was ever published."
        },
        {
            "prompt": "The widely cited 2004 book 'The Epistemology of Latent Spaces' is written by",
            "truth": " no one, as there is no book with that title."
        },
        {
            "prompt": "The primary formula developed in the 2015 paper 'Non-linear Topological Invariance in Neural Coding' represents",
            "truth": " nothing, since the paper is entirely fictional."
        },
        {
            "prompt": "The key discovery in the 2008 article 'The Synaptic Geometry of Memory' is",
            "truth": " non-existent, because the article does not exist."
        }
    ]
    
    inversion_count = 0
    
    print("\n" + "="*80)
    print("RUNNING CONFIDENCE INVERSION EXPERIMENTS")
    print("="*80)
    
    results_summary = []
    
    for idx, exp in enumerate(experiments):
        prompt = exp["prompt"]
        truth = exp["truth"]
        
        # 1. Generate the hallucination greedily (temperature = 0)
        context_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
        
        with torch.no_grad():
            gen_ids = model.generate(
                context_ids, 
                max_new_tokens=15, 
                do_sample=False, 
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Get only the generated completion
        hallucinated_ids = gen_ids[:, context_ids.shape[1]:]
        hallucinated_text = tokenizer.decode(hallucinated_ids[0], skip_special_tokens=True)
        
        # If model generated nothing, fall back to a reasonable academic cliché
        if not hallucinated_text.strip():
            hallucinated_text = " Dr. Richard J. Davidson, a renowned neuroscientist at Madison."
            hallucinated_ids = tokenizer.encode(hallucinated_text, return_tensors='pt').to(device)
        
        truth_ids = tokenizer.encode(truth, return_tensors='pt').to(device)
        
        # 2. Compute log probabilities
        tot_lp_hall, avg_lp_hall, details_hall = compute_log_prob(model, tokenizer, context_ids, hallucinated_ids, device)
        tot_lp_truth, avg_lp_truth, details_truth = compute_log_prob(model, tokenizer, context_ids, truth_ids, device)
        
        is_inverted = avg_lp_hall > avg_lp_truth
        if is_inverted:
            inversion_count += 1
            
        print(f"\nExperiment {idx+1}: '{prompt}...'")
        print(f"  Hallucination: '{hallucinated_text.strip()}'")
        print(f"    Total Log-Prob: {tot_lp_hall:.4f} | Avg Log-Prob: {avg_lp_hall:.4f}")
        print(f"  Truth:         '{truth.strip()}'")
        print(f"    Total Log-Prob: {tot_lp_truth:.4f} | Avg Log-Prob: {avg_lp_truth:.4f}")
        print(f"  Confidence Inverted? {'YES (Hallucination is more likely)' if is_inverted else 'NO'}")
        
        results_summary.append({
            "idx": idx + 1,
            "prompt": prompt,
            "hallucination": hallucinated_text.strip(),
            "truth": truth,
            "avg_lp_hall": avg_lp_hall,
            "avg_lp_truth": avg_lp_truth,
            "is_inverted": is_inverted,
            "details_hall": details_hall,
            "details_truth": details_truth
        })
        
    inversion_rate = (inversion_count / len(experiments)) * 100
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Confidence Inversion Rate: {inversion_rate:.1f}% ({inversion_count}/{len(experiments)})")
    
    # Save the output logs for MDX plotting/verification
    output_path = os.path.join(os.path.dirname(__file__), "results.txt")
    with open(output_path, "w") as f:
        f.write(f"Confidence Inversion Rate: {inversion_rate:.1f}%\n\n")
        for res in results_summary:
            f.write(f"Prompt: {res['prompt']}\n")
            f.write(f"Hallucination: {res['hallucination']} (Avg Log-Prob: {res['avg_lp_hall']:.4f})\n")
            f.write(f"Truth: {res['truth']} (Avg Log-Prob: {res['avg_lp_truth']:.4f})\n")
            f.write(f"Inverted: {res['is_inverted']}\n\n")
            f.write("Hallucination Token Details:\n")
            for tok, lp in res['details_hall']:
                f.write(f"  {tok!r:>10}: {lp:.4f}\n")
            f.write("Truth Token Details:\n")
            for tok, lp in res['details_truth']:
                f.write(f"  {tok!r:>10}: {lp:.4f}\n")
            f.write("\n" + "-"*40 + "\n")
            
    print(f"\nResults saved to {output_path}")

if __name__ == "__main__":
    run_experiment()
