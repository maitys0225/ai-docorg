# Using DeepSeek API to Tag Local PDFs

1. **Install Required Libraries:**
   - Ensure you have `requests` and `psycopg2` installed:
     ```sh
     pip install requests psycopg2
     ```

2. **DeepSeek API Script:**
   - Create a Python script to interact with the DeepSeek API and process PDFs.

3. **Database Configuration:**
   - Ensure you have a PostgreSQL database set up with the table `tbl_Ai_doc_orgcols`.

4. **Sample Python Script:**
   - Use the following script to process PDFs and insert tags into the database:
     ```python
     // filepath: /Users/maitys/repos/ai-docorg/deepseek/process_pdfs.py
     import requests
     import psycopg2

     # DeepSeek API endpoint
     DEEPSEEK_API_URL = "https://api.deepseek.com/analyze"

     # Database connection details
     DB_HOST = "your_db_host"
     DB_NAME = "your_db_name"
     DB_USER = "your_db_user"
     DB_PASS = "your_db_password"

     def analyze_pdf(file_path):
         with open(file_path, 'rb') as f:
             response = requests.post(DEEPSEEK_API_URL, files={'file': f})
             response.raise_for_status()
             return response.json()

     def insert_tags_into_db(doc_id, tags):
         conn = psycopg2.connect(
             host=DB_HOST,
             dbname=DB_NAME,
             user=DB_USER,
             password=DB_PASS
         )
         cur = conn.cursor()
         for tag in tags:
             cur.execute(
                 "INSERT INTO tbl_Ai_doc_orgcols (doc_id, tag) VALUES (%s, %s)",
                 (doc_id, tag)
             )
         conn.commit()
         cur.close()
         conn.close()

     def main():
         pdf_path = "path/to/your/local.pdf"
         doc_id = "unique_document_id"

         # Analyze the PDF and get tags
         tags = analyze_pdf(pdf_path)

         # Insert tags into the database
         insert_tags_into_db(doc_id, tags)

     if __name__ == "__main__":
         main()
     ```

5. **Run the Script:**
   - Execute the script to process your PDF and store tags in the database:
     ```sh
     python /Users/maitys/repos/ai-docorg/deepseek/process_pdfs.py
     ```
