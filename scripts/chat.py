"""Run the chatbot in a terminal."""
from src.chains import answer_document


def main():
    print("RAG chatbot is ready.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            result = answer_document(question)

            print(f"\nAssistant: {result['answer']}")

            if result["sources"]:
                print("\nSources:")
                for source in result["sources"]:
                    print(f"- {source}")

            print()

        except Exception as error:
            print(f"\nError: {error}\n")


if __name__ == "__main__":
    main()