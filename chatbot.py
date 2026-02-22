def chatbot():
    responses = load_responses()

    # load PDF text once
    pdf_text = extract_pdf_text("company_policy.pdf")

    print("Chatbot is ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower()

        if not user_input.strip():
            print("Bot: Please enter something.")
            continue

        if user_input == "exit":
            print("Bot: Goodbye!")
            break

        user_input = preprocess(user_input)

        # check the PDF first
        pdf_reply = search_pdf_answer(user_input, pdf_text)

        if pdf_reply:
            print("Bot:", pdf_reply)
        else:
            reply = get_response(user_input, responses)
            print("Bot:", reply)
