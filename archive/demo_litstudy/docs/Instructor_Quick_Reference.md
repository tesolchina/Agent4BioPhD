# AI Agent Demo: Quick Reference for Instructors

## Pre-Demo Checklist

### Setup (1-2 days before)
- [ ] Clone motifmatchr repository
- [ ] Have Badia-i-Mompel paper accessible
- [ ] Test AI agent access
- [ ] Prepare example datasets (small ATAC-seq peaks BED file)
- [ ] Ensure R/Bioconductor environment working
- [ ] Test one example workflow end-to-end

### Environment Check
```bash
# Verify R installation
R --version  # Should be >= 4.0

# In R, check key packages
R -e "library(motifmatchr); library(GenomicRanges); library(TFBSTools)"

# Test AI agent
# Ask: "Explain what motifmatchr does in one paragraph"
```

---

## Demo Flow Options

### Option A: 1-Hour Fast Track
**Focus**: Show the "wow factor" of agent capabilities

**Timing**:
- 0-10 min: Introduction + motivation
- 10-25 min: **Phase 1** - Literature to code connection
- 25-45 min: **Phase 3.1** - Complete scATAC-seq workflow
- 45-55 min: Live Q&A with agent
- 55-60 min: Discussion + next steps

**Key Moments**:
- Agent reads paper and explains motifmatchr's role
- Agent designs complete workflow with biological reasoning
- Agent handles real data format issues on the fly

---

### Option B: 2-Hour Deep Dive
**Focus**: Understanding + application

**Timing**:
- 0-15 min: Introduction
- 15-45 min: **Phases 1-2** - Foundation (literature + codebase)
- 45-75 min: **Phase 3** - Research scenarios (pick 2)
- 75-105 min: **Phase 4.1** - Validation strategies
- 105-120 min: Discussion + hands-on time

**Key Moments**:
- Trace code execution across R-C++ boundary
- Design workflow for student's actual research question
- Set up validation with ChIP-seq data

---

### Option C: 3-Hour Workshop
**Focus**: Complete research cycle

**Timing**:
- 0-15 min: Introduction
- 15-50 min: **Phases 1-2** - Foundation
- 50-90 min: **Phase 3** - All scenarios
- 90-120 min: **Phase 4** - Critical evaluation
- 120-160 min: **Phase 5** - End-to-end research scenario
- 160-180 min: Hands-on + Q&A

**Key Moments**:
- All of the above plus:
- Benchmark against ground truth
- Design complete differentiation time course analysis
- Generate publication-ready figures

---

## Live Demo Scripts

### Demo Script 1: Literature-Code Bridge (15 min)

**Setup**: Have paper and motifmatchr repo open

**Script**:
```
[Instructor]: "Let's start with a common research scenario. 
I'm reading this Nature Reviews paper about GRN inference, 
and they mention motifmatchr. I want to understand how to use it 
and why it's preferred over other methods."

[To Agent]: "Read the Badia-i-Mompel et al 2023 paper, specifically 
Box 1 about motif matcher algorithms. Then explore the motifmatchr 
repository. Explain:
1. What biological problem does motif matching solve?
2. How does motifmatchr implement this?
3. Why might I choose motifmatchr over FIMO or HOMER?
4. What are the key limitations I should know about?"

[Wait for response, highlight key points]

[To Agent - follow-up]: "In the paper they mention p-value thresholds 
for motif matching. How does this work in motifmatchr specifically? 
What p-value should I use if I'm looking for rare pioneer TF binding 
events vs. common TFs?"

[Discussion with students about biological reasoning]
```

**Expected Duration**: Agent reads + responds in 2-3 min, discussion 5 min, follow-up 3 min, wrap 2 min

---

### Demo Script 2: Parameter Deep Dive (15 min)

**Setup**: Have motifmatchr vignette open

**Script**:
```
[Instructor]: "Parameters matter in bioinformatics, but defaults 
aren't always right. Let's understand motifmatchr parameters."

[To Agent]: "I'm analyzing ATAC-seq peaks from two cell types: 
neurons (GC-rich genome regions) and adipocytes (AT-rich regions). 
Help me understand motifmatchr parameters:

1. Background frequency: Why does this matter? How should I set it 
   differently for GC-rich vs AT-rich regions?
   
2. P-value threshold: I'm looking for SOX2 (known) and potential 
   novel pioneer TFs (unknown). What thresholds for each?
   
3. PWM vs PFM input: What's the difference and when does it matter?

4. Pseudocounts: When would I change from default 0.8?

For each parameter, explain the biological reasoning, not just 
the technical definition."

[Discussion: Have students think about their own data]

[To Agent - follow-up]: "Create a decision tree I can use to choose 
these parameters based on my biological question and data type."
```

**Expected Duration**: Initial response 3 min, discussion 5 min, decision tree 2 min, examples 5 min

---

### Demo Script 3: Complete Workflow Design (25 min)

**Setup**: Prepare example peak files or use simulated data

**Script**:
```
[Instructor]: "Now for the real test - can the agent help design 
a complete analysis workflow?"

[To Agent]: "I have scATAC-seq data from 5 cell clusters during 
neural differentiation. I want to identify TFs driving each stage. 
Help me design and implement:

1. Complete workflow overview:
   - Input: Cluster-specific peaks (BED format)
   - Steps: ???
   - Output: Ranked TF candidates per cluster
   
2. Practical implementation:
   - Which motif database? (I work with human)
   - How to define background peaks?
   - Statistical test for enrichment?
   
3. Code that:
   - Reads peaks for each cluster
   - Runs motifmatchr efficiently
   - Tests enrichment vs background
   - Filters by TF expression (I have matching scRNA-seq)
   - Creates visualization
   
4. Validation strategy:
   - How do I know results are credible?
   - What's a good positive control?
   
5. Biological interpretation:
   - What if I find known developmental TFs? (good!)
   - What if I find unexpected TFs? (interesting!)
   - Next experimental steps?"

[Let agent generate workflow, review with students]

[Optionally run code on example data]

[Discussion]: "What design choices did the agent make? 
Are there alternatives? What would you change?"
```

**Expected Duration**: Agent workflow design 5 min, code generation 5 min, review 5 min, discussion 10 min

---

### Demo Script 4: Critical Evaluation (20 min)

**Setup**: Have example predictions ready (can be simulated)

**Script**:
```
[Instructor]: "We've made predictions. Now the crucial part - 
are they reliable?"

[To Agent]: "I ran motifmatchr on my ATAC peaks and predicted 
100 TFs bind. But I have ChIP-seq for 5 of them as ground truth. 
Help me:

1. Design validation experiment:
   - How do I compare predictions to ChIP-seq?
   - What metrics? (PPV, sensitivity, F1?)
   - How to define 'true positive'?
   
2. Write code to:
   - Overlap motif predictions with ChIP peaks
   - Calculate performance per TF
   - Identify systematic biases
   
3. Interpret results:
   - What if precision is 30%? Is that good or bad?
   - Why might certain TF families predict poorly?
   - Can I improve predictions?
   
4. Next steps:
   - Filter false positives using RNA-seq?
   - Add epigenetic features?
   - Focus on high-confidence predictions only?
   
Make sure to explain what benchmarking can and can't tell us 
about biological reality."

[Discussion]: "What are the limitations of this validation? 
What other approaches exist?"
```

**Expected Duration**: Agent response 5 min, code review 5 min, discussion 10 min

---

## Handling Common Questions

### Q: "Isn't this just asking AI to write code? How is this different?"

**A**: Great question! Let me show you. [Do side-by-side comparison]

**Traditional approach**:
```
Student: "Write R code to match motifs in peaks"
AI: [gives generic matchMotifs() example]
Student: [copies code, doesn't understand parameters]
```

**Agent approach**:
```
Student: "I want to find TFs driving differentiation. I have ATAC-seq 
peaks from 5 timepoints. Help me design analysis."

Agent: [Asks clarifying questions about biological system]
Agent: [Explains GRN inference framework from paper]
Agent: [Designs workflow with biological reasoning for each step]
Agent: [Generates code with parameter choices explained]
Agent: [Suggests validation strategies]
Agent: [Helps interpret results biologically]
```

**Key differences**:
- Starts with biology, not syntax
- Teaches concepts, not just commands
- Makes informed choices, explains why
- Includes validation and interpretation
- Builds research skills, not just code skills

---

### Q: "Can't students just use ChatGPT?"

**A**: They absolutely can and should! But this teaches them *how* to use it effectively:

**Ineffective use**:
- "Write motif matching code" → Generic solution
- Takes output at face value
- No biological context
- Doesn't validate results

**Effective use** (what we teach):
- Frames biological question clearly
- Asks for reasoning and alternatives
- Requests validation strategies
- Iterates based on results
- Learns transferable principles

We're teaching **AI literacy** in research context.

---

### Q: "What if the AI makes mistakes?"

**A**: Excellent observation! This is why we emphasize:

1. **Critical evaluation** (Phase 4) - Always validate!
2. **Multiple sources** - Compare to documentation, papers
3. **Biological sanity checks** - Do results make sense?
4. **Reproducibility** - Can you verify the approach?

**Demo this**:
```
[To Agent]: "You suggested using p-value 0.00005. But what if 
I change it to 0.001? Explain the tradeoff and help me 
decide which is better for my specific question."
```

AI mistakes are teaching opportunities about critical thinking.

---

### Q: "Won't students become dependent on AI?"

**A**: That's why our approach focuses on **understanding**, not just **using**:

We teach students to:
- Ask "why" not just "how"
- Understand method assumptions and limitations
- Design validation experiments
- Make independent methodological decisions
- Contribute improvements to tools

The agent is a **tutor**, not a **crutch**.

**Analogy**: Learning to drive with GPS
- Bad: Blindly follow directions, don't learn roads
- Good: Understand routes, can navigate without it

We teach the "good" approach.

---

## Backup Plans

### If Agent is Slow
- Pre-generate key responses
- Have screenshots of example interactions
- Use recorded demo videos
- Switch to synchronous Q&A mode

### If Code Doesn't Run
- Have pre-run outputs ready
- Use screenshots of expected results
- Focus on design and reasoning rather than execution
- Use this as teaching moment about debugging

### If Students Are Lost
- Start with simpler scenario
- Do more step-by-step walkthrough
- Increase interaction/discussion time
- Provide handout with key concepts

### If Students Are Advanced
- Jump to Phase 4-5 (advanced topics)
- Let them design their own scenarios
- Have agent help with their actual research data
- Discuss contributing to open source

---

## Post-Demo Survey Questions

Quick assessment (5 questions, 2 min):

1. **Understanding**: "On a scale 1-5, how well do you understand what motifmatchr does and when to use it?"

2. **Confidence**: "How confident are you designing a motif analysis workflow for your own research?"

3. **Value**: "What was most valuable: 
   - [ ] Seeing literature-to-code connection
   - [ ] Understanding parameters biologically
   - [ ] Complete workflow design
   - [ ] Validation strategies
   - [ ] Other: ___"

4. **AI Agent**: "Did this demo change how you think about using AI in research?"

5. **Next Steps**: "What would you want to try next?"

---

## Follow-Up Resources

### Send to students after demo:
- [ ] Link to AI_Agent_Demo_Plan.md (full document)
- [ ] Example prompts they can adapt
- [ ] motifmatchr documentation links
- [ ] Badia-i-Mompel paper
- [ ] Office hours for personalized help
- [ ] Slack/Discord channel for questions

### For motivated students:
- [ ] Challenge: "Design analysis for your own data"
- [ ] Advanced scenarios from Phase 4-5
- [ ] Contributing to motifmatchr
- [ ] Related tools (chromVAR, SCENIC+)

---

## Troubleshooting

### "The agent doesn't understand my biological question"
**Solution**: Add more context, be specific about organism, cell type, experimental design

### "Code fails with error message"
**Solution**: Copy error to agent, ask to debug. Teaches error handling!

### "Results don't make biological sense"
**Solution**: Perfect teaching moment! Work with agent to diagnose:
- Wrong parameters?
- Data quality issues?
- Method limitations?
- Need validation?

### "Student says 'I could have Googled this'"
**Solution**: Show the integration aspect - not just finding answers, but:
- Connecting multiple sources
- Adapting to specific context
- Iterative refinement
- Biological reasoning throughout

---

## Success Indicators

You know the demo worked if students:

✅ Ask "why" questions about parameters  
✅ Propose their own research scenarios  
✅ Discuss biological interpretation, not just code  
✅ Question/validate agent suggestions  
✅ Connect concepts across papers/tools  
✅ Excited about applying to their research  
✅ Understand both capabilities AND limitations  

---

## Contact for Questions

[Add your contact info here]

---

**Remember**: The goal is teaching computational biology research skills, with AI as a powerful teaching assistant. Focus on the learning, not just the technology!
