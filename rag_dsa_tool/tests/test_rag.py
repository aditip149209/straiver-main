from rag_dsa_tool.retrieval.retriever import query_rag
from langchain_community.llms.ollama import Ollama

EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false') Does the actual response match the expected response? 
"""

def test_binary_search():
    assert query_and_validate(
        question="What is the time complexity of binary search in a sorted array? (Answer with the Big O notation only)",
        expected_response="O(log n)",
    )

def test_linked_list_cycle():
    assert query_and_validate(
        question="Which algorithm is commonly used to detect a cycle in a linked list? (Answer with the algorithm name only)",
        expected_response="Floyd's Tortoise and Hare",
    )

def test_quick_sort_worst_case():
    assert query_and_validate(
        question="What is the worst-case time complexity of quick sort? (Answer with the Big O notation only)",
        expected_response="O(n^2)",
    )


def test_stack_usage():
    assert query_and_validate(
        question="Which data structure is used for function call management in recursion? (Answer with the data structure name only)",
        expected_response="Stack",
    )

def query_and_validate(question: str, expected_response: str):
    response_text = query_rag(question)
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response, actual_response=response_text
    )

    model = Ollama(model="mistral")
    evaluation_results_str = model.invoke(prompt)
    evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

    print(prompt)

    if "true" in evaluation_results_str_cleaned:
        # Print response in Green if it is correct.
        print("\033[92m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    elif "false" in evaluation_results_str_cleaned:
        # Print response in Red if it is incorrect.
        print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return False
    else:
        raise ValueError(
            f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
        )

def main():
    test_binary_search()
    test_linked_list_cycle()
    test_quick_sort_worst_case()
    test_stack_usage()


if __name__ == "__main__":
    main()