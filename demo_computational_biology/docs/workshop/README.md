# AI Agent for Bioinformatics Demo - Documentation

This directory contains materials for demonstrating AI agent capabilities in bioinformatics research, using motifmatchr as a case study.

## Files

### AI_Agent_Demo_Plan.md
Comprehensive plan for workshops and self-paced learning showing how AI agents can:
- Bridge scientific literature and code implementation
- Explore complex codebases across multiple languages
- Design research-relevant workflows
- Provide biological interpretation and statistical guidance
- Enable critical evaluation and method validation

## Key Philosophy

**This is NOT about having AI write code for you.**

**This IS about:**
- Understanding computational methods deeply
- Connecting literature concepts to implementations
- Designing biologically sound workflows
- Critical thinking about method limitations
- Learning computational biology best practices

## Target Audience

Biology PhD students with programming experience who want to:
- Accelerate their computational research
- Understand (not just use) bioinformatics tools
- Design novel analyses
- Make informed methodological choices
- Develop computational thinking skills

## motifmatchr Context

**motifmatchr** is an R/Bioconductor package for fast transcription factor binding motif matching. It's featured in:
- Badia-i-Mompel et al. (2023) *Nature Reviews Genetics*
- Used in modern gene regulatory network (GRN) inference workflows
- Integrates with single-cell ATAC-seq and ChIP-seq pipelines

## Quick Start

### For Instructors
1. Review `AI_Agent_Demo_Plan.md` 
2. Choose phases based on time available:
   - 1 hour: Phases 1-2 (Foundation)
   - 2 hours: Add Phase 3 (Applications)  
   - 3 hours: Add Phases 4-5 (Advanced + Research Scenario)

3. Prepare by having AI agent:
   - Read the Badia-i-Mompel paper
   - Explore motifmatchr codebase
   - Generate example workflows for your chosen scenarios

### For Students
1. Start with Phase 1: Literature-code connection
2. Work through example prompts in each phase
3. Adapt scenarios to your own research questions
4. Focus on understanding, not just running code

## Example Quick Wins

### Win 1: Understanding the Algorithm (15 min)
Ask agent to trace how `matchMotifs()` works from R call to C++ MOODS library, explaining each step and why it's fast.

### Win 2: Parameter Selection (10 min)
Ask agent to explain what p-value threshold to use for your specific biological question (pioneer TFs vs. abundant TFs).

### Win 3: Workflow Design (20 min)
Ask agent to design complete scATAC-seq to TF prediction pipeline with biological reasoning for each step.

### Win 4: Critical Evaluation (15 min)
Ask agent to help benchmark motifmatchr predictions against ChIP-seq ground truth and identify failure modes.

## What Makes This "Agent-like"?

| Traditional Code Generation | AI Agent Approach |
|---------------------------|-------------------|
| "Write code to match motifs" | "Help me design a motif analysis that addresses my biological question" |
| Gives you code | Gives you code + biological context + validation strategy |
| One-shot output | Iterative refinement with teaching |
| You must know what to ask | Agent helps you figure out what to ask |
| Syntax-focused | Science-focused |

## Learning Outcomes

After working through this material, students should be able to:

1. **Conceptual Understanding**
   - Explain role of motif matching in GRN inference
   - Understand algorithm trade-offs (speed, accuracy, features)
   - Connect computational parameters to biological meaning

2. **Practical Skills**
   - Design multi-step bioinformatics workflows
   - Choose appropriate tools and parameters
   - Integrate multiple data types
   - Validate computational predictions

3. **Critical Thinking**
   - Evaluate method limitations
   - Design benchmarking experiments
   - Identify when predictions need experimental validation
   - Generate testable hypotheses

4. **Research Independence**
   - Navigate unfamiliar codebases
   - Read and implement from methods papers
   - Contribute to open source tools
   - Design novel analyses

## Common Pitfalls to Avoid

❌ **Just asking for code** - You'll get syntax but not understanding  
✅ **Ask for explanation + code** - You'll learn the reasoning

❌ **Accepting outputs uncritically** - AI can make mistakes  
✅ **Ask agent to validate and explain** - Builds critical thinking

❌ **Using defaults without understanding** - Parameters matter!  
✅ **Ask why defaults were chosen** - Learn when to change them

❌ **Treating agent as search engine** - Misses the teaching opportunity  
✅ **Have conversations with agent** - Ask follow-ups, test understanding

## Tips for Effective AI Agent Use

### Good Prompts Include:
- **Context**: "I'm analyzing scATAC-seq from..."
- **Goal**: "I want to identify TF drivers of..."
- **Constraints**: "I have 10,000 peaks and limited compute..."
- **Level**: "Explain as if I understand R but new to motif analysis..."
- **Verification**: "How can I validate these predictions?"

### Great Follow-Up Questions:
- "Why did you choose that approach over alternatives?"
- "What are the assumptions and when do they break?"
- "How would this change if I had [different data type]?"
- "What could go wrong and how do I check?"
- "What experiments would validate this?"

### Effective Workflow:
1. **Explore**: Have agent explain concepts and tools
2. **Design**: Collaborate on analysis strategy
3. **Implement**: Generate code with biological context
4. **Validate**: Check results make biological sense
5. **Iterate**: Refine based on results and new questions
6. **Document**: Have agent help write methods section

## Real Student Testimonials (Hypothetical for Demo)

> "I was stuck trying to figure out which motif database to use. The agent didn't just tell me 'use JASPAR' - it explained coverage, accuracy, and when each database is appropriate for my organism and TFs of interest." - PhD Student, Developmental Biology

> "Instead of spending days reading documentation, the agent walked me through the motifmatchr source code, explaining the R-C++ interface and why certain design decisions were made. Now I can actually extend it for my needs." - PhD Student, Computational Biology

> "The agent helped me design a validation strategy using my ChIP-seq data. It showed me the predictions were good for some TF families but poor for others, and explained why. That biological insight was invaluable." - PhD Student, Epigenetics

## Next Steps

After completing this demo:
1. Apply to your own research data
2. Explore related tools (chromVAR, SCENIC+, Pando)
3. Design novel integration of multiple data types
4. Consider contributing improvements to motifmatchr
5. Share your workflows with the community

## Resources

### Core Papers
- **Badia-i-Mompel et al. (2023)** Nature Reviews Genetics - GRN inference review
- **motifmatchr** documentation and vignettes
- **MOODS algorithm** - Korhonen et al. (2009)

### Related Methods
- SCENIC+ for GRN inference
- chromVAR for TF activity
- ArchR/Signac for scATAC-seq

### Databases
- JASPAR, HOCOMOCO, CIS-BP for TF motifs
- ChIP-Atlas for validation data

## Contributing

Have you developed an interesting scenario or use case? Consider contributing:
1. Write up your research question
2. Document your agent-assisted workflow
3. Share biological insights gained
4. Submit as case study for others to learn from

## Questions?

This is a living document. Feedback and suggestions welcome!

---

**Remember**: The goal is not to replace your thinking, but to amplify it. Use AI agents to handle technical complexity so you can focus on biological insight and experimental design.
