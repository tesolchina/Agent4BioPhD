# AI Agent Workshop: Hands-On Exercises

## How to Use This Document

Each exercise is designed to help you learn both:
1. **Computational concepts** - How motif matching works
2. **AI agent skills** - How to effectively collaborate with AI

**Format**:
- 📚 **Background**: What you need to know
- 🎯 **Your Goal**: What you're trying to accomplish  
- 💡 **Starter Prompt**: How to begin (but adapt it!)
- 🤔 **Think About**: Critical thinking questions
- ✅ **Success Criteria**: How you know you succeeded

---

## Exercise 1: Literature to Code Translation

**Time**: 15-20 minutes  
**Difficulty**: ⭐ Beginner

### 📚 Background
The Badia-i-Mompel et al. (2023) paper explains that GRN inference requires TF binding prediction. They list several motif matcher algorithms in Box 1.

### 🎯 Your Goal
Understand how the biological concepts in the paper map to motifmatchr's implementation.

### 💡 Starter Prompt
```
I'm reading Box 1 in Badia-i-Mompel et al 2023 about motif matcher 
algorithms. Help me connect the paper to motifmatchr:

1. What is the biological problem being solved?
2. How does motifmatchr's algorithm (MOODS) work conceptually?
3. The paper mentions different algorithms have different "modeling" 
   approaches - what does motifmatchr model differently from FIMO?
4. When would I choose motifmatchr over other options?

Include specific examples from both the paper and the code.
```

### 🤔 Think About
- Why do we need computational prediction instead of just doing ChIP-seq for all TFs?
- What biological assumptions are we making when we use motif matching?
- What could cause false positives? False negatives?

### ✅ Success Criteria
- [ ] You can explain the biological problem in your own words
- [ ] You understand the MOODS algorithm conceptually (don't need math details)
- [ ] You can list 2-3 strengths and weaknesses of motif matching
- [ ] You know when motifmatchr is the right tool choice

### 📝 Reflection
Write 2-3 sentences: "Before this exercise I thought ___. Now I understand ___."

---

## Exercise 2: Parameter Detective

**Time**: 20-25 minutes  
**Difficulty**: ⭐⭐ Intermediate

### 📚 Background
The `matchMotifs()` function has several parameters: p-value threshold, background frequencies, PWM vs PFM, etc. These aren't arbitrary - they reflect biological reality.

### 🎯 Your Goal
Understand what each parameter means biologically and how to choose appropriate values.

### 💡 Starter Prompt
```
I need to understand motifmatchr parameters for my research. I'm 
analyzing ATAC-seq peaks from [YOUR CELL TYPE]. For each parameter, 
explain both the technical meaning AND biological interpretation:

1. p.cutoff (default 0.00005)
   - What does this represent biologically?
   - When would I use 0.0001 vs 0.00001?
   - What's the trade-off?

2. bg (background frequencies)
   - Why does this matter for my [GC-rich/AT-rich] regions?
   - Should I use "genome", "even", or custom?
   
3. PWMatrix vs PFMatrix input
   - What's the difference?
   - When does this choice matter?

4. Pseudocounts (in PWM conversion)
   - What are these for?
   - When would I change from default 0.8?

Give me a decision framework for each parameter based on common research scenarios.
```

### 🤔 Think About
- If you're looking for rare pioneer TF binding events vs abundant TFs, how do parameters differ?
- How would your parameter choices differ for enhancer regions vs promoter regions?
- What if you're comparing across species with different GC content?

### ✅ Success Criteria
- [ ] You can explain each parameter to a labmate
- [ ] You know when to deviate from defaults
- [ ] You understand the biological consequences of parameter choices
- [ ] You can justify your parameter choices for YOUR data

### 🎓 Advanced Challenge
Ask the agent: "Create a parameter selection quiz with 5 scenarios where I choose appropriate parameters and you explain if I'm right/wrong and why."

---

## Exercise 3: Design Your Own Workflow

**Time**: 30-40 minutes  
**Difficulty**: ⭐⭐⭐ Advanced

### 📚 Background
Real research requires integrating multiple steps: data QC, motif matching, statistical testing, biological filtering, interpretation.

### 🎯 Your Goal
Design a complete workflow for a research question similar to yours.

### 💡 Starter Prompt (Customize!)
```
I'm studying [YOUR BIOLOGICAL SYSTEM]. I have:
- scATAC-seq: [describe: # cells, # clusters/timepoints, conditions]
- scRNA-seq: [matched or separate?]
- Optional: [ChIP-seq, other data]

My research question: [e.g., "Which TFs drive cell fate X vs Y?"]

Help me design a complete workflow:

1. PLANNING:
   - What are the analysis steps from raw peaks to TF candidates?
   - What tools/databases do I need?
   - What are potential pitfalls in my specific case?

2. IMPLEMENTATION STRATEGY:
   - Should I use pseudobulk or single-cell level analysis?
   - Which motif database for [my organism]?
   - How to define "background" peaks for enrichment testing?
   - How to integrate RNA-seq for filtering?

3. STATISTICAL APPROACH:
   - What test for enrichment? (Fisher's exact? Binomial? Other?)
   - Multiple testing correction strategy?
   - How to handle multiple clusters/timepoints?

4. VALIDATION PLAN:
   - How do I know results are credible?
   - What are good positive controls?
   - What follow-up experiments would confirm findings?

5. INTERPRETATION:
   - What would "success" look like?
   - How to distinguish true drivers vs passengers?
   - What makes a TF finding "interesting" vs "expected"?
```

### 🤔 Think About
- What are the biological assumptions in your workflow?
- Where could things go wrong?
- How would you validate unexpected findings?
- What would you do if results disagree with literature?

### ✅ Success Criteria
- [ ] You have a step-by-step workflow with rationale for each step
- [ ] You've identified potential problems and solutions
- [ ] You have a validation strategy
- [ ] You can execute at least part of the workflow (with example data)
- [ ] You understand biological interpretation of expected outputs

### 🎓 Advanced Challenge
Ask the agent to:
1. Critique your workflow - what might be improved?
2. Generate actual code for key steps
3. Help you create a methods section draft
4. Suggest relevant papers to cite

---

## Exercise 4: Critical Evaluation

**Time**: 25-30 minutes  
**Difficulty**: ⭐⭐⭐ Advanced

### 📚 Background
Computational predictions are hypotheses, not facts. You must validate and understand limitations.

### 🎯 Your Goal
Learn to critically evaluate motif matching results.

### 💡 Starter Prompt
```
I ran motifmatchr and predicted 100 TFs bind to my peaks. 
Help me critically evaluate these results:

1. VALIDATION STRATEGY:
   - I have ChIP-seq for 5 of these TFs. How do I compare?
   - What metrics should I calculate? (precision, recall, F1?)
   - How do I define a "true positive"?
   - Write code to perform this validation

2. INTERPRET PERFORMANCE:
   - If precision is 30%, is that good, acceptable, or poor?
   - Why might it be impossible to get 90% precision?
   - What if precision varies widely across the 5 TFs?

3. IDENTIFY SYSTEMATIC BIASES:
   - Which types of TFs might be predicted poorly? Why?
   - How does peak quality affect accuracy?
   - Are there genomic regions where method fails?

4. IMPROVE PREDICTIONS:
   - Can I filter false positives using RNA-seq expression?
   - Would adding DNase footprinting help?
   - Should I adjust p-value thresholds per TF family?
   - What about ensemble approaches?

5. BIOLOGICAL REALITY:
   - Even with ChIP-seq "ground truth", what might we be missing?
   - Why might a predicted site without ChIP peak still be real?
   - Why might a ChIP peak without motif still be meaningful?
```

### 🤔 Think About
- What does it mean if a TF's motif is present but ChIP-seq shows no binding?
- What does it mean if ChIP-seq shows binding but no motif is present?
- How do you balance false positives vs false negatives for your research question?
- When do you trust predictions enough to do experiments?

### ✅ Success Criteria
- [ ] You can design and execute a validation experiment
- [ ] You understand what validation can and cannot tell you
- [ ] You've identified method limitations for your use case
- [ ] You have strategies to improve predictions
- [ ] You can interpret results in biological context

### 🎓 Advanced Challenge
"Compare motifmatchr to an alternative method (e.g., FIMO) on the same data. Which performs better? Why? When might the alternative be preferred?"

---

## Exercise 5: Real Research Application

**Time**: 60+ minutes  
**Difficulty**: ⭐⭐⭐⭐ Expert

### 📚 Background
Apply everything you've learned to your actual research data (or realistic simulated data).

### 🎯 Your Goal
Complete analysis from data to biological insights, with AI agent as collaborator.

### 💡 Starter Prompt (Highly Customized!)
```
I need help with a real research project:

BACKGROUND:
- Biological system: [describe]
- Research question: [specific question]
- Data available: [list all data types, sample sizes, conditions]
- Current challenges: [what you're stuck on]

HELP ME:
1. Refine my research question to be computationally tractable
2. Design complete workflow with justification for each step
3. Identify potential problems specific to my data
4. Generate code for analysis pipeline
5. Create visualization strategy
6. Plan validation experiments
7. Interpret results biologically
8. Draft methods section

Throughout: Teach me the reasoning, don't just give answers.
```

### 🤔 Think About (Project-Specific)
- What assumptions am I making?
- What could go wrong?
- How will I know if results are correct?
- What makes a finding publishable?
- What are the next experiments?

### ✅ Success Criteria
- [ ] You have a complete, executable analysis pipeline
- [ ] You understand every step and can justify choices
- [ ] You've identified limitations and planned validation
- [ ] You can interpret results in biological context
- [ ] You've learned transferable skills for future projects
- [ ] You can explain your approach to your PI/lab

### 🎓 Advanced Challenge
1. **Reproducibility**: Create a documented workflow others can follow
2. **Robustness**: Test how results change with different parameters
3. **Communication**: Write up results as if for a paper/presentation
4. **Extension**: Identify what additional data would strengthen conclusions
5. **Contribution**: Could you contribute your workflow as a vignette?

---

## Bonus Exercise: Teaching Others

**Time**: 20 minutes  
**Difficulty**: ⭐⭐⭐ (Teaching is learning!)

### 🎯 Your Goal
Solidify your understanding by teaching someone else (or explaining to AI agent).

### 💡 Activity
Ask the AI agent to roleplay as a confused student:

```
Act as a biology PhD student who is confused about [TOPIC YOU LEARNED]. 
I'm going to explain it to you. Ask me clarifying questions like a 
real student would. Push back if my explanation isn't clear. Help me 
refine my explanation.

Topic I'm teaching: [e.g., "Why p-value threshold matters for motif matching"]
```

### ✅ Success Criteria
- [ ] You can explain without looking at notes
- [ ] You can answer "why" questions
- [ ] You can give examples and analogies
- [ ] You can identify when you still have gaps in understanding

---

## Reflection Questions

After completing exercises, reflect on:

### About Computational Biology:
1. What biological concept did you understand differently than before?
2. What surprised you about how motif matching works?
3. What limitations of computational predictions did you not appreciate before?

### About AI Agents:
1. What kinds of prompts worked best for learning?
2. When did you need to push back or verify agent suggestions?
3. How did your prompts improve as you learned?

### About Your Research:
1. How will you apply these skills to your own work?
2. What research questions can you now tackle that you couldn't before?
3. What additional skills do you need to develop?

---

## Quick Reference: Effective Prompting

### Good Prompt Structure:
```
CONTEXT: [Your biological system and data]
GOAL: [What you want to accomplish]
CONSTRAINTS: [Limitations, resources]
LEVEL: [Your background knowledge]
REQUEST: [Specific help needed]
VERIFICATION: [How to validate]
```

### Effective Follow-Ups:
- "Why did you choose X over Y?"
- "What are the assumptions and when do they break?"
- "How would this change if [different scenario]?"
- "What could go wrong and how do I check?"
- "Show me an example with real data"

### Red Flags (Agent Might Be Wrong):
- Suggests outdated methods without explaining why
- Doesn't mention limitations or assumptions
- Gives code without biological context
- Recommends overly complex approach when simple would work
- Can't explain the "why" behind suggestions

**When uncertain, ask for sources or alternative approaches!**

---

## Resources

### Getting Help:
- [Your instructor/TA contact]
- [Course forum/Slack]
- motifmatchr documentation: [link]
- Bioconductor support: [link]

### Going Deeper:
- Badia-i-Mompel et al. 2023 (full paper)
- MOODS algorithm paper
- Related tools: chromVAR, SCENIC+, Pando
- TF motif databases: JASPAR, HOCOMOCO

### Your Own Research:
- Apply to your data
- Join bioinformatics journal club
- Contribute to open source tools
- Share your workflows

---

## Completion Certificate

When you've completed exercises 1-4 and feel confident:

**I, [YOUR NAME], have completed the AI Agent for Bioinformatics workshop.**

**I can now:**
- [ ] Connect literature concepts to computational implementations
- [ ] Understand and explain motif matching algorithms
- [ ] Choose appropriate parameters based on biological questions
- [ ] Design complete analysis workflows
- [ ] Critically evaluate computational predictions
- [ ] Effectively collaborate with AI agents as research tools
- [ ] Apply these skills to my own research

**Next steps in my computational biology journey:**
1. [Your goal]
2. [Your goal]
3. [Your goal]

**Date**: ___________  
**Signature**: ___________

---

*Remember: The goal isn't to become a coding expert overnight. It's to develop computational thinking and effective AI collaboration skills that accelerate your biology research.*

**You've got this! 🧬💻🤖**
