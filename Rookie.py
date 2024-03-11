# Predefined list of questions and answers
qa_list = [
    {"question": "What is your college name?", "answer": "My College name is R.V.S College of Engineering. It is in Dindigul."},
    {"question": "What is your department name?", "answer": "I'm a Computer Science Engineering Student which holds the pinnacle of future."},
    {"question": "Who is the founder of your college?", "answer": "The Founder of R.V.S College of Engineering is Ratnavel Subramaniam."},
    # Add more questions and answers as you needed
]

# Function to retrieve answer based on question
def get_answer(question):
    for item in qa_list:
        if item["question"].lower() == question.lower():
            return item["answer"]
    return "Didn't I told you ask simple question you mf?"
    # return "Sorry, I don't have an answer to that question."

# Main function
def main():
    while True:
        # Take user input for question
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        
        # Retrieve answer
        answer = get_answer(question)
        
        # Display answer
        print("Answer: ", answer)

# Call main function
if __name__ == "__main__":
    print("Manual:")
    print("1. Always ends the question with '?'\n2. I'm a Rookie. Don't be mean to me while asking question. IDK every Fuckin thing.\n3. Ask easy and simple Question.")
    main()
