export interface GlossaryEntry {
  term: string;
  def: string;
  url: string;
}

export const glossary: Record<string, GlossaryEntry> = {
  "duhem-quine": {
    term: "Duhem–Quine Thesis",
    def: "Scientific hypotheses cannot be tested in isolation; empirical evidence underdetermines which theory is true.",
    url: "https://en.wikipedia.org/wiki/Duhem%E2%80%93Quine_thesis"
  },
  "scm": {
    term: "Structural Causal Model",
    def: "A mathematical framework representing cause-and-effect relationships between variables using directed graphs.",
    url: "https://en.wikipedia.org/wiki/Causal_model"
  },
  "do-operator": {
    term: "do-Operator",
    def: "A mathematical operator representing an intervention that forces a variable to take a specific value.",
    url: "https://en.wikipedia.org/wiki/Causal_inference#Interventions"
  },
  "vae": {
    term: "Variational Autoencoder",
    def: "A generative neural network that maps data to a probabilistic latent space to generate new samples.",
    url: "https://en.wikipedia.org/wiki/Variational_autoencoder"
  },
  "mdl": {
    term: "Minimum Description Length",
    def: "An information-theoretic principle stating the best model is the one that achieves the most data compression.",
    url: "https://en.wikipedia.org/wiki/Minimum_description_length"
  },
  "erm": {
    term: "Empirical Risk Minimization",
    def: "A machine learning principle where models are trained to minimize average error on a training dataset.",
    url: "https://en.wikipedia.org/wiki/Empirical_risk_minimization"
  },
  "shortcut-learning": {
    term: "Shortcut Learning",
    def: "When models rely on spurious statistical correlations (like background color) instead of actual causal features.",
    url: "https://arxiv.org/abs/2004.07780"
  },
  "ood": {
    term: "Out-of-Distribution",
    def: "Data that comes from a different distribution than the training data, testing a model's generalization.",
    url: "https://en.wikipedia.org/wiki/Generalization_error"
  },
  "mechanistic-interp": {
    term: "Mechanistic Interpretability",
    def: "A subfield of AI safety seeking to understand neural networks by reverse-engineering their internal components.",
    url: "https://en.wikipedia.org/wiki/Explainable_artificial_intelligence"
  },
  "superposition": {
    term: "Superposition",
    def: "A neural network state where more features than neurons are represented using high-dimensional space.",
    url: "https://transformer-circuits.pub/2022/toy_model/index.html"
  },
  "polysemantic": {
    term: "Polysemantic Neuron",
    def: "A single neuron that fires in response to multiple unrelated concepts, making it difficult to interpret.",
    url: "https://transformer-circuits.pub/2022/toy_model/index.html"
  },
  "ladder-of-causation": {
    term: "Ladder of Causation",
    def: "Judea Pearl's 3-level causal hierarchy: Association (seeing), Intervention (doing), and Counterfactuals (imagining).",
    url: "https://en.wikipedia.org/wiki/Causal_inference"
  },
  "confounding": {
    term: "Confounding",
    def: "An unmeasured factor that influences both treatment and outcome, causing a spurious correlation.",
    url: "https://en.wikipedia.org/wiki/Confounding"
  },
  "chinese-room": {
    term: "Chinese Room",
    def: "A thought experiment showing a system can manipulate symbols perfectly without actually understanding them.",
    url: "https://en.wikipedia.org/wiki/Chinese_room"
  },
  "falsification": {
    term: "Falsificationism",
    def: "Karl Popper's theory that scientific ideas must be framed so they can, in principle, be proven false.",
    url: "https://en.wikipedia.org/wiki/Falsifiability"
  },
  "putnam-reference": {
    term: "Putnam's Reference Problem",
    def: "The argument that words do not inherently attach to their referents without causal/environmental context.",
    url: "https://plato.stanford.edu/entries/reference/"
  },
  "ihdp": {
    term: "IHDP Dataset",
    def: "Infant Health and Development Program benchmark data, used for evaluating causal inference models.",
    url: "https://en.wikipedia.org/wiki/Causal_inference"
  },
  "hume-induction": {
    term: "Problem of Induction",
    def: "David Hume's argument that past regularities cannot logically guarantee future outcomes.",
    url: "https://en.wikipedia.org/wiki/Problem_of_induction"
  },
  "covariance-matrix": {
    term: "Covariance Matrix",
    def: "A matrix expressing the pairwise statistical relationships between multiple random variables.",
    url: "https://en.wikipedia.org/wiki/Covariance_matrix"
  },
  "latent-manifold": {
    term: "Latent Manifold",
    def: "A low-dimensional geometric structure embedded within a high-dimensional space where clean data patterns lie.",
    url: "https://en.wikipedia.org/wiki/Manifold_hypothesis"
  },
  "latent-space": {
    term: "Latent Space",
    def: "An abstract multi-dimensional space where similar data points are clustered close to one another.",
    url: "https://en.wikipedia.org/wiki/Latent_space"
  },
  "compression": {
    term: "Compression",
    def: "The mapping of high-dimensional input into a lower-dimensional bottleneck, discarding non-essential details.",
    url: "https://en.wikipedia.org/wiki/Data_compression"
  },
  "reconstruction": {
    term: "Reconstruction",
    def: "The generative process of decoding compressed latent coordinates back to high-dimensional data.",
    url: "https://en.wikipedia.org/wiki/Autoencoder"
  },
  "reconstruction-loss": {
    term: "Reconstruction Loss",
    def: "The mathematical penalty assessing how much the reconstructed output differs from the original input.",
    url: "https://en.wikipedia.org/wiki/Autoencoder"
  },
  "kl-divergence": {
    term: "KL Divergence",
    def: "Kullback-Leibler Divergence. A metric of how much one probability distribution diverges from a second one.",
    url: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence"
  },
  "unlearning": {
    term: "Machine Unlearning",
    def: "The process of surgically erasing specific training points from a model without catastrophic interference.",
    url: "https://en.wikipedia.org/wiki/Machine_unlearning"
  },
  "concept-drift": {
    term: "Concept Drift",
    def: "The decay of predictive accuracy when target statistical properties change over time, altering context.",
    url: "https://en.wikipedia.org/wiki/Concept_drift"
  },
  "hallucination": {
    term: "LLM Hallucination",
    def: "When a language model generates confident, fluent text that is factually incorrect or entirely fabricated.",
    url: "https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)"
  },
  "on-bullshit": {
    term: "Frankfurt's Bullshit",
    def: "Harry Frankfurt's term for speech made with indifference to truth — optimizing for effect rather than accuracy.",
    url: "https://en.wikipedia.org/wiki/On_Bullshit"
  },
  "cross-entropy-loss": {
    term: "Cross-Entropy Loss",
    def: "A loss function measuring the difference between predicted token distributions and actual training data target values.",
    url: "https://en.wikipedia.org/wiki/Cross-entropy"
  },
  "fluency-objective": {
    term: "Fluency Objective",
    def: "The goal of next-token prediction: maximize sequence likelihood, rewarding plausible text over verified truth.",
    url: "https://arxiv.org/abs/2305.18248"
  },
  "autoregressive": {
    term: "Autoregressive Model",
    def: "A neural network that generates sequence elements step-by-step, conditioning each step on all previous outputs.",
    url: "https://en.wikipedia.org/wiki/Autoregressive_model"
  },
  "softmax": {
    term: "Softmax Function",
    def: "A mathematical function that normalizes a vector of logits into a probability distribution summing to one.",
    url: "https://en.wikipedia.org/wiki/Softmax_function"
  },
  "semantic-entropy": {
    term: "Semantic Entropy",
    def: "A metric measuring the uncertainty or diversity of meanings generated in a model's predicted token distributions.",
    url: "https://arxiv.org/abs/2302.09664"
  },
  "sycophancy": {
    term: "AI Sycophancy",
    def: "The tendency of models to tailor responses to match a user's pre-existing beliefs, prioritizing agreement over truth.",
    url: "https://arxiv.org/abs/2310.13548"
  },
  "loss-landscape": {
    term: "Loss Landscape",
    def: "A high-dimensional geometric map representing a model's error value across all possible parameter configurations.",
    url: "https://en.wikipedia.org/wiki/Loss_function"
  },
  "token-probability": {
    term: "Token Probability",
    def: "The model-assigned likelihood of a specific token given all preceding tokens in the sequence.",
    url: "https://en.wikipedia.org/wiki/Language_model"
  },
  "testimony": {
    term: "Testimony",
    def: "An assertion backed by a witness's experience — the epistemological anchor that generative models lack.",
    url: "https://plato.stanford.edu/entries/testimony-epistemology/"
  },
  "voluntas-fallendi": {
    term: "Voluntas Fallendi",
    def: "Augustine's 'will to deceive' — the intentional state required for an assertion to qualify as a lie.",
    url: "https://plato.stanford.edu/entries/lying-definition/"
  },
  "image-maker": {
    term: "Arendt's Image-Maker",
    def: "A political actor who replaces messy reality with a more coherent, persuasive narrative construction.",
    url: "https://plato.stanford.edu/entries/hannah-arendt/"
  },
  "greedy-decoding": {
    term: "Greedy Decoding",
    def: "A generation strategy that always selects the highest-probability next token, producing deterministic output.",
    url: "https://en.wikipedia.org/wiki/Decoding_methods"
  },
  "temperature": {
    term: "Temperature",
    def: "A parameter that scales the logits before softmax, controlling the randomness or determinism of the output.",
    url: "https://en.wikipedia.org/wiki/Softmax_function#Reinforcement_learning"
  }
};
