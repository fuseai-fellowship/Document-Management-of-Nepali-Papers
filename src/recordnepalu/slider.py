import streamlit as st

# Check if we are on the "slider" page based on URL query parameters
query_params = st.query_params
if query_params.get("page", ["main"])[0] == "slider":

    # Ensure session state is initialized for document navigation
    if 'doc_index' not in st.session_state:
        st.session_state.doc_index = 0  # Default to the first document if not set

    # Retrieve the stored documents array
    documents = st.session_state.stored_documents

    # Search bar to filter documents by filename
    search_query = st.text_input("Search Documents by Name")

    # Filter documents based on the search query
    filtered_documents = []
    for doc in documents:
        if search_query.lower() in doc['filename'].lower():
            filtered_documents.append(doc)

    # If no documents match the search, default to showing all
    if not filtered_documents:
        filtered_documents = documents

    # Ensure the index remains within bounds after filtering
    st.session_state.doc_index = min(st.session_state.doc_index, len(filtered_documents) - 1)

    # Display the current document
    current_doc = filtered_documents[st.session_state.doc_index]

    # Display the document (image, text, etc.)
    st.image(current_doc["image_path"], caption=current_doc['filename'], use_column_width=True)
    st.write(f"Category: {current_doc['category']}")

    # Previous and Next buttons for navigation
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Previous", disabled=st.session_state.doc_index == 0):
            st.session_state.doc_index -= 1

    with col3:
        if st.button("Next", disabled=st.session_state.doc_index == len(filtered_documents) - 1):
            st.session_state.doc_index += 1

    # Show the current document index and the total count
    st.write(f"Document {st.session_state.doc_index + 1} of {len(filtered_documents)}")

    # Back button to return to the main document list
    if st.button("Back to Document List"):
        # Set the page back to main
        st.query_params["page"] = "main"  # Update the query parameters
