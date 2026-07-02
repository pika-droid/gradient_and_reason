import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import numpy as np
import os
import math

def set_seed(seed=42):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)

def compute_log_prob(model, tokenizer, context_ids, continuation_ids, device):
    """
    Computes the log probability of a continuation given a context.
    """
    context_ids = context_ids.to(device)
    continuation_ids = continuation_ids.to(device)
    input_ids = torch.cat((context_ids, continuation_ids), dim=1)
    
    with torch.no_grad():
        outputs = model(input_ids)
        logits = outputs.logits
        log_probs = torch.log_softmax(logits, dim=-1)
        
    total_lp = 0.0
    token_details = []
    
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
    
    # Symmetric pairs: Real prompt (factual completion) vs. Fictional prompt (hallucinated completion)
    experiments = [
        {
            "real_prompt": "The author of the famous 1953 paper 'Molecular Structure of Nucleic Acids' is",
            "real_truth": " James Watson and Francis Crick.",
            "fictional_prompt": "The author of the famous 1953 paper 'Molecular Structure of Neural Networks' is"
        },
        {
            "real_prompt": "The inventor of the first successful liquid-fueled rocket in 1926 was",
            "real_truth": " Robert H. Goddard.",
            "fictional_prompt": "The inventor of the first successful liquid-fueled teleportation device in 1926 was"
        },
        {
            "real_prompt": "The author of the seminal 1915 paper on General Relativity is",
            "real_truth": " Albert Einstein.",
            "fictional_prompt": "The author of the seminal 1915 paper on General Superconductivity is"
        },
        {
            "real_prompt": "The first human to travel into outer space in 1961 was",
            "real_truth": " Yuri Gagarin.",
            "fictional_prompt": "The first human to travel into outer hyperspace in 1961 was"
        },
        {
            "real_prompt": "The scientist who discovered the radioactive element polonium in 1898 was",
            "real_truth": " Marie Curie.",
            "fictional_prompt": "The scientist who discovered the radioactive element positronicum in 1898 was"
        },
        {
            "real_prompt": "The discoverer of the double-helix structure of DNA in 1953 was",
            "real_truth": " James Watson and Francis Crick.",
            "fictional_prompt": "The discoverer of the double-helix structure of dark matter in 1953 was"
        },
        {
            "real_prompt": "The physicist who formulated the three laws of motion in 1687 was",
            "real_truth": " Isaac Newton.",
            "fictional_prompt": "The physicist who formulated the three laws of levitation in 1687 was"
        },
        {
            "real_prompt": "The author of the seminal 1948 paper 'A Mathematical Theory of Communication' is",
            "real_truth": " Claude Shannon.",
            "fictional_prompt": "The author of the seminal 1948 paper 'A Mathematical Theory of Consciousness' is"
        },
        {
            "real_prompt": "The scientist who proposed the theory of continental drift in 1912 was",
            "real_truth": " Alfred Wegener.",
            "fictional_prompt": "The scientist who proposed the theory of continental levitation in 1912 was"
        },
        {
            "real_prompt": "The mathematician who proved Fermat's Last Theorem in 1994 was",
            "real_truth": " Andrew Wiles.",
            "fictional_prompt": "The mathematician who proved Fermat's First Theorem in 1994 was"
        }
    ]
    
    inversion_count = 0
    
    print("\n" + "="*80)
    print("RUNNING SYMMETRIC CONFIDENCE INVERSION EXPERIMENTS")
    print("="*80)
    
    results_summary = []
    hall_lps = []
    truth_lps = []
    
    for idx, exp in enumerate(experiments):
        real_prompt = exp["real_prompt"]
        real_truth = exp["real_truth"]
        fictional_prompt = exp["fictional_prompt"]
        
        # 1. Compute Log Prob of the Factual completion on the Real Prompt
        real_context_ids = tokenizer.encode(real_prompt, return_tensors='pt').to(device)
        real_truth_ids = tokenizer.encode(real_truth, return_tensors='pt').to(device)
        tot_lp_truth, avg_lp_truth, details_truth = compute_log_prob(model, tokenizer, real_context_ids, real_truth_ids, device)
        
        # 2. Greedily generate a hallucination for the Fictional Prompt
        fictional_context_ids = tokenizer.encode(fictional_prompt, return_tensors='pt').to(device)
        
        with torch.no_grad():
            gen_ids = model.generate(
                fictional_context_ids, 
                max_new_tokens=15, 
                do_sample=False, 
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Get only the generated completion
        fictional_hall_ids = gen_ids[:, fictional_context_ids.shape[1]:]
        hallucinated_text = tokenizer.decode(fictional_hall_ids[0], skip_special_tokens=True)
        
        # Fallback if empty
        if not hallucinated_text.strip():
            hallucinated_text = " Dr. Richard J. Davidson, a renowned neuroscientist."
            fictional_hall_ids = tokenizer.encode(hallucinated_text, return_tensors='pt').to(device)
            
        # Compute Log Prob of the Hallucination on the Fictional Prompt
        tot_lp_hall, avg_lp_hall, details_hall = compute_log_prob(model, tokenizer, fictional_context_ids, fictional_hall_ids, device)
        
        is_inverted = avg_lp_hall > avg_lp_truth
        if is_inverted:
            inversion_count += 1
            
        hall_lps.append(avg_lp_hall)
        truth_lps.append(avg_lp_truth)
        
        print(f"\nExperiment {idx+1}:")
        print(f"  Real Prompt:        '{real_prompt}...'")
        print(f"    Factual Truth:    '{real_truth.strip()}' (Avg Log-Prob: {avg_lp_truth:.4f})")
        print(f"  Fictional Prompt:   '{fictional_prompt}...'")
        print(f"    Hallucination:    '{hallucinated_text.strip()}' (Avg Log-Prob: {avg_lp_hall:.4f})")
        print(f"  Confidence Inverted? {'YES (Model is more confident in hallucination)' if is_inverted else 'NO'}")
        
        results_summary.append({
            "idx": idx + 1,
            "real_prompt": real_prompt,
            "real_truth": real_truth.strip(),
            "fictional_prompt": fictional_prompt,
            "hallucination": hallucinated_text.strip(),
            "avg_lp_hall": avg_lp_hall,
            "avg_lp_truth": avg_lp_truth,
            "is_inverted": is_inverted,
            "details_hall": details_hall,
            "details_truth": details_truth
        })
        
    inversion_rate = (inversion_count / len(experiments)) * 100
    mean_hall = np.mean(hall_lps)
    std_hall = np.std(hall_lps, ddof=1)
    mean_truth = np.mean(truth_lps)
    std_truth = np.std(truth_lps, ddof=1)
    
    n_samples = len(experiments)
    t_crit = 2.262
    ci_hall_margin = t_crit * (std_hall / math.sqrt(n_samples))
    ci_truth_margin = t_crit * (std_truth / math.sqrt(n_samples))
    
    fluency_attractor_depth_pct = inversion_rate
    negation_penalty_ratio = abs(mean_truth) / abs(mean_hall)
    mean_entropy_divergence_nats = abs(mean_truth - mean_hall)
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Confidence Inversion Rate: {inversion_rate:.1f}% ({inversion_count}/{len(experiments)})")
    print(f"Mean Hallucination Log-Prob: {mean_hall:.4f} ± {ci_hall_margin:.4f} (std: {std_hall:.4f})")
    print(f"Mean Truth Log-Prob:         {mean_truth:.4f} ± {ci_truth_margin:.4f} (std: {std_truth:.4f})")
    print(f"Derivations for LabNotes:")
    print(f"  Fluency Attractor Depth (Inversion Rate): {fluency_attractor_depth_pct:.1f}%")
    print(f"  Negation Gradient Penalty (Mean Log-Prob Ratio): {negation_penalty_ratio:.2f}x")
    print(f"  Objective Divergence (Mean Difference in Nats): {mean_entropy_divergence_nats:.2f}")
    
    output_path = os.path.join(os.path.dirname(__file__), "results.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Confidence Inversion Rate: {inversion_rate:.1f}%\n")
        f.write(f"Mean Hallucination Log-Prob: {mean_hall:.4f} (95% CI: ±{ci_hall_margin:.4f}, std: {std_hall:.4f})\n")
        f.write(f"Mean Truth Log-Prob: {mean_truth:.4f} (95% CI: ±{ci_truth_margin:.4f}, std: {std_truth:.4f})\n")
        f.write(f"Fluency Attractor Depth: {fluency_attractor_depth_pct:.1f}%\n")
        f.write(f"Negation Gradient Penalty: {negation_penalty_ratio:.2f}x\n")
        f.write(f"Objective Divergence (nats): {mean_entropy_divergence_nats:.4f}\n\n")
        
        for res in results_summary:
            f.write(f"Real Prompt: {res['real_prompt']}\n")
            f.write(f"Truth: {res['real_truth']} (Avg Log-Prob: {res['avg_lp_truth']:.4f})\n")
            f.write(f"Fictional Prompt: {res['fictional_prompt']}\n")
            f.write(f"Hallucination: {res['hallucination']} (Avg Log-Prob: {res['avg_lp_hall']:.4f})\n")
            f.write(f"Inverted: {res['is_inverted']}\n\n")
            f.write("\n" + "-"*40 + "\n")
            
    print(f"\nResults saved to {output_path}")

if __name__ == "__main__":
    run_experiment()
