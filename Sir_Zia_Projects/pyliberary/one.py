import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF for PDF text extraction
import speech_recognition as sr
import json
import os

# Configure Gemini API
genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc")

# File to store books
LIBRARY_FILE = "library.txt"

# Load existing books
def load_books():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save books
def save_books(books):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

# Summarize text using Gemini API
def summarize_text(text):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Summarize this text in 5 sentences: {text[:2000]}")
    return response.text

# Book Recommendation using Gemini API
def get_book_recommendation(book_genre):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Suggest a book for someone who likes {book_genre} genre.")
    return response.text

# Speech Recognition (Voice Assistant)
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening for voice command...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand the command."

# Streamlit UI
st.title("📚 AI-Powered Personal Library Manager")
books = load_books()

# Add a new book
st.header("➕ Add a Book")
with st.form("add_book_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1800, max_value=2025, step=1)
    genre = st.text_input("Genre")
    read_status = st.radio("Have you read this book?", ["Yes", "No"])
    submitted = st.form_submit_button("Add Book")
    if submitted:
        book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status == "Yes"}
        books.append(book)
        save_books(books)
        st.success("✅ Book added successfully!")

# Search for a book
st.header("🔍 Search for a Book")
search_query = st.text_input("Enter book title or author to search:")
if st.button("Search"):
    results = [book for book in books if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
    if results:
        for book in results:
            st.write(f"📖 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
    else:
        st.warning("No matching books found.")

# Display all books
st.header("📖 Library Collection")
if books:
    for book in books:
        st.write(f"📕 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
else:
    st.info("Your library is empty. Add books to see them here.")

# Remove a book
st.header("🗑 Remove a Book")
remove_title = st.text_input("Enter book title to remove:")
if st.button("Remove Book"):
    books = [book for book in books if book["title"].lower() != remove_title.lower()]
    save_books(books)
    st.success(f"✅ '{remove_title}' removed from library!")

# Display statistics
st.header("📊 Library Statistics")
total_books = len(books)
read_books = sum(1 for book in books if book["read"])
percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

st.write(f"📚 **Total Books:** {total_books}")
st.write(f"📖 **Books Read:** {read_books}")
st.write(f"📈 **Percentage Read:** {percentage_read:.2f}%")

# PDF Summarization
st.header("📂 Upload a Book (PDF) for AI Summarization")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    st.success("✅ PDF uploaded successfully!")
    pdf_text = extract_text_from_pdf(uploaded_file)
    if st.button("Summarize Book"):
        summary = summarize_text(pdf_text)
        st.subheader("📑 AI-Generated Summary:")
        st.write(summary)

# Voice Assistant Feature
st.header("🎙 AI Voice Assistant")
if st.button("Start Listening"):
    voice_command = recognize_speech()
    st.write(f"🎤 You said: {voice_command}")