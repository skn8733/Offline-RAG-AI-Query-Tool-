from app.rag_pipeline import RAGPipeline

def main():
    pipeline = RAGPipeline(
        vector_db_path="./vector_db",
        model_path="models/local_model/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf"
    )
    print("Welcome to the AI Query Tool!")
    print("Type your question below or 'exit' to quit.")

    while True:
        query = input("\nYour question: ").strip()
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        if not query:
            print("Please enter a valid question.")
            continue

        try:
            answer = pipeline.ask(query)
            print(f"\nAnswer:\n{answer}")
        except Exception as e:
            print(f"Error during query processing: {e}")

if __name__ == "__main__":
    main()