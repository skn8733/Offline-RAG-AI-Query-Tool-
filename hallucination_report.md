# Hallucination Report

## Summary

While testing the RAG-based query tool, I observed that the model sometimes hallucinates details—particularly when multiple experts had similar but distinct roles at Uber (e.g., former managers vs. executives). In some cases, the model inferred relationships or facts that were not explicitly stated in the transcript excerpts.

This is likely due to the limitations of using a quantized model (Mistral 7B Q4_K_M), the 2048-token context window, and the model’s tendency to fill in gaps when information is missing or ambiguous.

## Steps Taken to Reduce Hallucinations

- I enforced strict system prompts instructing the model to only answer using the transcript content.
- I added a fallback response: _"The answer is not available in the provided transcript."_
- I chunked transcripts into smaller pieces to optimize retrieval and increase context relevance.
- I kept the temperature low to minimize creative completions.

## How Accuracy Can Be Improved

To further improve accuracy and reduce hallucinations:

- Enhance retrieval by using better embeddings or re-ranking methods.
- Add metadata filtering (e.g., expert role or transcript ID) to scope the search.
- Use a larger or more accurate model (e.g., LLaMA 3 8B or higher precision Mistral).
- Include citations or timestamps for transparency on where the answer came from.

## Limitations

- Quantized models sacrifice some accuracy for performance.
- 2048-token context window can truncate relevant information.
- The model is still prone to guessing when the retrieved context is insufficient or ambiguous.

Overall, the tool works effectively within the constraints, but accuracy can be improved with smarter retrieval and a more robust model.
