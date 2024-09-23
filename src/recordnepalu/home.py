import streamlit as st

def process_document(uploaded_file):
    text = "Sample text from document" 
    category = "policy"  
    return text, category


stored_documents = []

st.title("Document and Record Management System (DRMS)")

st.header("Upload Document")
uploaded_file = st.file_uploader("Choose a document...", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file is not None:
    text, category = process_document(uploaded_file)
    stored_documents.append({"filename": uploaded_file.name, "text": text, "category": category})
    st.success("Document uploaded and processed!")

# Search section
st.header("Search Documents")
search_query = st.text_input("Enter search text")

# Initialize selected categories
if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = {"Policy": False, "Press Release": False, "Education": False, "ID": False}

# Buttons for category selection arranged horizontally
categories = ["Policy", "Press Release", "Education", "ID"]
cols = st.columns(len(categories))

for i, category in enumerate(categories):
    with cols[i]:
        if st.button(category, key=category):
            st.session_state.selected_categories[category] = not st.session_state.selected_categories[category]

# Determine which categories are selected
selected_categories = [cat for cat, selected in st.session_state.selected_categories.items() if selected]

# Filter documents based on search query and selected categories
filtered_documents = []
for doc in stored_documents:
    if (not selected_categories or doc['category'] in selected_categories) and search_query.lower() in doc['text'].lower():
        filtered_documents.append(doc)

# Display stored documents
st.header("Stored Documents")
if filtered_documents:
    for doc in filtered_documents:
        st.subheader(doc["filename"])
        st.write(doc["text"])
        st.write(f"Category: {doc['category']}")
else:
    st.write("No documents found.")
