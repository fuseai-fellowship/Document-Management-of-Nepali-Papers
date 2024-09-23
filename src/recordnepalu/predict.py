











def predict(text, tokenizer, model, max_length, device):
    text = preprocess_text(text)
    model.eval()
    with torch.no_grad():
        encoded_input = tokenizer.encode(text, max_length)
        input_ids = torch.tensor(encoded_input, dtype=torch.long).unsqueeze(0).to(device)
        attention_mask = (input_ids != tokenizer.vocab['<PAD>']).long().to(device)

        outputs = model(input_ids, attention_mask)
        _, predicted_class = torch.max(outputs, 1)

        return predicted_class.item()