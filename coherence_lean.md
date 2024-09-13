import data.real.basic

-- Definition: Quantum coherence decay
def coherence_decay (gamma t : ℝ) : ℝ := real.exp (-gamma * t)

-- Proposition: Coherence decay is positive for all non-negative gamma and time
theorem coherence_decay_positive (gamma t : ℝ) (h_gamma : gamma ≥ 0) (h_t : t ≥ 0) : coherence_decay gamma t ≥ 0 :=
begin
  unfold coherence_decay,
  apply real.exp_pos,
end

-- Proposition: Coherence decay approaches 0 as t approaches infinity
theorem coherence_decay_limit_zero (gamma : ℝ) (h_gamma : gamma > 0) : 
  filter.tendsto (λ t, coherence_decay gamma t) filter.at_top (nhds 0) :=
begin
  unfold coherence_decay,
  exact real.tendsto_exp_neg_at_top,
end


