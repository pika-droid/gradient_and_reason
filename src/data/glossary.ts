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
  }
};
